import click

from .list import list_providers
from .inspect import inspect_provider


@click.group()
@click.help_option("-h", "--help")
def providers():
    """Manage API providers."""


# Register subcommands
providers.add_command(list_providers)
providers.add_command(inspect_provider)
