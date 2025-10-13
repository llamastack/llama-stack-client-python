# Examples

This directory contains example scripts and interactive tools for exploring the Llama Stack Client Python SDK.

## Interactive Agent CLI

`interactive_agent_cli.py` - An interactive command-line tool for exploring agent turn/step events with server-side tools.

### Features

- 🔍 **File Search Integration**: Automatically sets up a vector store with sample knowledge base
- 📊 **Event Streaming**: See real-time turn/step events as the agent processes your queries
- 🎯 **Server-Side Tools**: Demonstrates file_search and other server-side tool execution
- 💬 **Interactive REPL**: Chat-style interface for easy exploration

### Prerequisites

1. Start a Llama Stack server with OpenAI provider:
   ```bash
   cd ~/local/llama-stack
   source ../stack-venv/bin/activate
   export OPENAI_API_KEY=<your-key>
   llama stack run ci-tests --port 8321
   ```

2. Install the client (from repository root):
   ```bash
   cd /Users/ashwin/local/new-stainless/llama-stack-client-python
   uv sync
   ```

### Usage

Basic usage (uses defaults: openai/gpt-4o, localhost:8321):
```bash
cd examples
uv run python interactive_agent_cli.py
```

With custom options:
```bash
uv run python interactive_agent_cli.py --model openai/gpt-4o-mini --base-url http://localhost:8321
```

### Example Session

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║        🤖  Interactive Agent Explorer  🔍                    ║
║                                                              ║
║  Explore agent turn/step events with server-side tools      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝

🔧 Configuration:
  Model: openai/gpt-4o
  Server: http://localhost:8321

🔌 Connecting to server...
  ✓ Connected

📚 Setting up knowledge base...
  Indexing documents....... ✓
  Vector store ID: vs_abc123

🤖 Creating agent with tools...
  ✓ Agent ready

💬 Type your questions (or 'quit' to exit, 'help' for suggestions)
──────────────────────────────────────────────────────────────

🧑 You: What is Project Phoenix?

🤖 Assistant:

  ┌─── Turn turn_abc123 started ───┐
  │                                 │
  │  🧠 Inference Step 0 started    │
  │  🔍 Tool Execution Step 1       │
  │     Tool: knowledge_search      │
  │     Status: server_side         │
  │  🧠 Inference Step 2            │
  │  ✓ Response: Project Phoenix... │
  │                                 │
  └─── Turn completed ──────────────┘

Project Phoenix is a next-generation distributed systems platform launched in 2024...
```

### What You'll See

The tool uses `AgentEventLogger` to display:
- **Turn lifecycle**: TurnStarted → TurnCompleted
- **Inference steps**: When the model is thinking/generating text
- **Tool execution steps**: When server-side tools (like file_search) are running
- **Step metadata**: Whether tools are server-side or client-side
- **Real-time streaming**: Text appears as it's generated

### Sample Questions

Type `help` in the interactive session to see suggested questions, or try:
- "What is Project Phoenix?"
- "Who is the lead architect?"
- "What ports does the system use?"
- "How long do JWT tokens last?"
- "Where is the production environment deployed?"

### Exit

Type `quit`, `exit`, `q`, or press `Ctrl+C` to exit.
