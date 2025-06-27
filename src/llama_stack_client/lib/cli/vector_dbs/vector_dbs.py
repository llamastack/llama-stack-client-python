# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from typing import Optional

import click
import yaml
from rich.console import Console
from rich.table import Table

from ..common.utils import handle_client_errors


@click.group()
@click.help_option("-h", "--help")
def vector_dbs():
    """Manage vector databases."""


@click.command("list")
@click.help_option("-h", "--help")
@click.pass_context
@handle_client_errors("list vector dbs")
def list(ctx):
    """Show available vector dbs on distribution endpoint"""

    client = ctx.obj["client"]
    console = Console()
    vector_dbs_list_response = client.vector_dbs.list()

    if vector_dbs_list_response:
        table = Table()
        # Add our specific columns
        table.add_column("identifier")
        table.add_column("provider_id")
        table.add_column("provider_resource_id")
        table.add_column("vector_db_type")
        table.add_column("params")

        for item in vector_dbs_list_response:
            # Create a dict of all attributes
            item_dict = item.__dict__

            # Extract our main columns
            identifier = str(item_dict.pop("identifier", ""))
            provider_id = str(item_dict.pop("provider_id", ""))
            provider_resource_id = str(item_dict.pop("provider_resource_id", ""))
            vector_db_type = str(item_dict.pop("vector_db_type", ""))
            # Convert remaining attributes to YAML string for params column
            params = yaml.dump(item_dict, default_flow_style=False)

            table.add_row(identifier, provider_id, provider_resource_id, vector_db_type, params)

        console.print(table)


@vector_dbs.command()
@click.help_option("-h", "--help")
@click.argument("vector-db-id")
@click.option("--provider-id", help="Provider ID for the vector db", default=None)
@click.option("--provider-vector-db-id", help="Provider's vector db ID", default=None)
@click.option(
    "--embedding-model",
    type=str,
    help="Embedding model (for vector type)",
    default="all-MiniLM-L6-v2",
)
@click.option(
    "--embedding-dimension",
    type=int,
    help="Embedding dimension (for vector type)",
    default=384,
)
@click.pass_context
@handle_client_errors("register vector db")
def register(
    ctx,
    vector_db_id: str,
    provider_id: Optional[str],
    provider_vector_db_id: Optional[str],
    embedding_model: Optional[str],
    embedding_dimension: Optional[int],
):
    """Create a new vector db"""
    client = ctx.obj["client"]

    response = client.vector_dbs.register(
        vector_db_id=vector_db_id,
        provider_id=provider_id,
        provider_vector_db_id=provider_vector_db_id,
        embedding_model=embedding_model,
        embedding_dimension=embedding_dimension,
    )
    if response:
        click.echo(yaml.dump(response.dict()))


@vector_dbs.command()
@click.help_option("-h", "--help")
@click.argument("vector-db-id")
@click.pass_context
@handle_client_errors("delete vector db")
def unregister(ctx, vector_db_id: str):
    """Delete a vector db"""
    client = ctx.obj["client"]
    client.vector_dbs.unregister(vector_db_id=vector_db_id)
    click.echo(f"Vector db '{vector_db_id}' deleted successfully")


# Register subcommands
vector_dbs.add_command(list)
vector_dbs.add_command(register)
vector_dbs.add_command(unregister)
