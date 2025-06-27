import click
from rich.console import Console

from ..common.utils import handle_client_errors


@click.command("version")
@click.help_option("-h", "--help")
@click.pass_context
@handle_client_errors("inspect version")
def inspect_version(ctx):
    """Show available providers on distribution endpoint"""
    client = ctx.obj["client"]
    console = Console()
    version_response = client.inspect.version()
    console.print(version_response)
