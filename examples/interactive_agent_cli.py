#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
"""Interactive CLI for exploring agent turn/step events with server-side tools.

Usage:
    python interactive_agent_cli.py [--model MODEL] [--base-url URL]
"""

import argparse
import io
import json
import os
import sys
import time
from pathlib import Path
from typing import Optional
from uuid import uuid4

from openai import OpenAI
from llama_stack_client import Agent, AgentEventLogger


CACHE_DIR = Path(os.path.expanduser("~/.cache/interactive-agent-cli"))
CACHE_DIR.mkdir(parents=True, exist_ok=True)
CACHE_FILE = CACHE_DIR / "vector_store.json"


def load_cached_vector_store() -> Optional[str]:
    try:
        with CACHE_FILE.open("r", encoding="utf-8") as fh:
            payload = json.load(fh)
        return payload.get("vector_store_id")
    except FileNotFoundError:
        return None
    except Exception as exc:  # pragma: no cover - defensive
        print(f"⚠️  Failed to load cached vector store info: {exc}", file=sys.stderr)
        return None


def save_cached_vector_store(vector_store_id: str) -> None:
    try:
        with CACHE_FILE.open("w", encoding="utf-8") as fh:
            json.dump({"vector_store_id": vector_store_id}, fh)
    except Exception as exc:  # pragma: no cover - defensive
        print(f"⚠️  Failed to cache vector store id: {exc}", file=sys.stderr)


def ensure_vector_store(client: OpenAI) -> str:
    cached_id = load_cached_vector_store()
    if cached_id:
        # Verify the vector store still exists on the server
        existing = client.vector_stores.list().data
        if any(store.id == cached_id for store in existing):
            print(f"📚 Reusing cached knowledge base (vector store {cached_id})")
            return cached_id
        else:
            print("⚠️  Cached vector store not found on server; creating a new one.")

    return setup_knowledge_base(client)


def setup_knowledge_base(client: OpenAI) -> str:
    """Create a vector store with interesting test knowledge."""
    print("📚 Setting up knowledge base...")

    # Create interesting test content
    knowledge_content = """
    # Project Phoenix Documentation

    ## Overview
    Project Phoenix is a next-generation distributed systems platform launched in 2024.

    ## Key Components
    - **Phoenix Core**: The main orchestration engine
    - **Phoenix Mesh**: Service mesh implementation
    - **Phoenix Analytics**: Real-time data processing pipeline

    ## Authentication
    - Primary auth method: OAuth 2.0 with JWT tokens
    - Token expiration: 24 hours
    - Refresh token validity: 7 days

    ## Architecture
    The system uses a microservices architecture with:
    - API Gateway on port 8080
    - Auth service on port 8081
    - Data service on port 8082

    ## Team
    - Lead Architect: Dr. Sarah Chen
    - Security Lead: James Rodriguez
    - DevOps Lead: Maria Santos

    ## Deployment
    - Production: AWS us-east-1
    - Staging: AWS us-west-2
    - Development: Local Kubernetes cluster
    """

    # Upload file
    file_payload = io.BytesIO(knowledge_content.encode("utf-8"))
    uploaded_file = client.files.create(
        file=("project_phoenix_docs.txt", file_payload, "text/plain"),
        purpose="assistants",
    )

    # Create vector store
    vector_store = client.vector_stores.create(
        name=f"phoenix-kb-{uuid4().hex[:8]}",
        extra_body={
            "provider_id": "faiss",
            "embedding_model": "nomic-ai/nomic-embed-text-v1.5",
        },
    )

    # Add file to vector store
    vector_store_file = client.vector_stores.files.create(
        vector_store_id=vector_store.id,
        file_id=uploaded_file.id,
    )

    # Wait for ingestion
    print("  Indexing documents...", end="", flush=True)
    deadline = time.time() + 60.0
    while vector_store_file.status != "completed":
        if vector_store_file.status in {"failed", "cancelled"}:
            raise RuntimeError(f"Vector store ingestion failed: {vector_store_file.status}")
        if time.time() > deadline:
            raise TimeoutError("Vector store file ingest timed out")
        time.sleep(0.5)
        vector_store_file = client.vector_stores.files.retrieve(
            vector_store_id=vector_store.id,
            file_id=vector_store_file.id,
        )
        print(".", end="", flush=True)

    print(" ✓")
    print(f"  Vector store ID: {vector_store.id}")
    print()
    save_cached_vector_store(vector_store.id)
    return vector_store.id


def print_banner():
    """Print a nice banner."""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║        🤖  Interactive Agent Explorer  🔍                    ║
║                                                              ║
║  Explore agent turn/step events with server-side tools      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
    print(banner)


def create_agent_with_tools(client, model, vector_store_id):
    """Create an agent with file_search and other server-side tools."""
    tools = [
        {
            "type": "file_search",
            "vector_store_ids": [vector_store_id],
        }
    ]

    instructions = """You are a helpful AI assistant with access to a knowledge base about Project Phoenix.

When answering questions:
1. ALWAYS search the knowledge base first using file_search
2. Provide specific details from the documentation
3. If information isn't in the knowledge base, say so clearly
4. Be concise but thorough

Available tools:
- file_search: Search the Project Phoenix documentation
"""

    agent = Agent(
        client=client,
        model=model,
        instructions=instructions,
        tools=tools,
    )

    return agent


def interactive_loop(agent):
    """Run the interactive query loop with nice event logging."""
    session_id = agent.create_session(f"interactive-{uuid4().hex[:8]}")
    print(f"📝 Session created: {session_id}\n")

    print("💬 Type your questions (or 'quit' to exit, 'help' for suggestions)")
    print("─" * 70)
    print()

    while True:
        try:
            # Get user input
            user_input = input("\n🧑 You: ").strip()

            if not user_input:
                continue

            if user_input.lower() in {"quit", "exit", "q"}:
                print("\n👋 Goodbye!")
                break

            if user_input.lower() == "help":
                print("\n💡 Try asking:")
                print("  • What is Project Phoenix?")
                print("  • Who is the lead architect?")
                print("  • What ports does the system use?")
                print("  • How long do JWT tokens last?")
                print("  • Where is the production environment deployed?")
                continue

            # Create message
            messages = [
                {
                    "type": "message",
                    "role": "user",
                    "content": [{"type": "input_text", "text": user_input}],
                }
            ]

            print()
            print("🤖 Assistant:", end=" ", flush=True)

            # Stream response with event logging
            event_logger = AgentEventLogger()

            for chunk in agent.create_turn(messages=messages, session_id=session_id, stream=True):
                # Log the event
                for log_msg in event_logger.log([chunk]):
                    print(log_msg, end="", flush=True)

            print()  # New line after response

        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}", file=sys.stderr)
            print("   Please try again or type 'quit' to exit", file=sys.stderr)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Interactive agent CLI with server-side tools",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s
  %(prog)s --model openai/gpt-4o
  %(prog)s --base-url http://localhost:8321/v1
        """,
    )
    parser.add_argument(
        "--model",
        default="openai/gpt-4o",
        help="Model to use (default: openai/gpt-4o)",
    )
    parser.add_argument(
        "--base-url",
        default="http://localhost:8321/v1",
        help="Llama Stack server URL (default: http://localhost:8321/v1)",
    )

    args = parser.parse_args()

    print_banner()
    print(f"🔧 Configuration:")
    print(f"  Model: {args.model}")
    print(f"  Server: {args.base_url}")
    print()

    # Create client
    print("🔌 Connecting to server...")
    try:
        client = OpenAI(base_url=args.base_url)
        models = client.models.list()
        identifiers = [model.identifier for model in models]
        if args.model not in identifiers:
            print(f"  ✗ Model {args.model} not found", file=sys.stderr)
            print(f"  Available models: {', '.join(identifiers)}", file=sys.stderr)
            sys.exit(1)

        print("  ✓ Connected")
        print()
    except Exception as e:
        print(f"  ✗ Failed to connect: {e}", file=sys.stderr)
        print(f"\n  Make sure the server is running at {args.base_url}", file=sys.stderr)
        sys.exit(1)

    # Setup knowledge base
    try:
        print("🔍 Setting up knowledge base...")
        vector_store_id = ensure_vector_store(client)
    except Exception as e:
        print(f"❌ Failed to setup knowledge base: {e}", file=sys.stderr)
        sys.exit(1)

    # Create agent
    print("🤖 Creating agent with tools...")
    try:
        agent = create_agent_with_tools(client, args.model, vector_store_id)
        print("  ✓ Agent ready")
        print()
    except Exception as e:
        print(f"  ✗ Failed to create agent: {e}", file=sys.stderr)
        sys.exit(1)

    # Run interactive loop
    interactive_loop(agent)


if __name__ == "__main__":
    main()
