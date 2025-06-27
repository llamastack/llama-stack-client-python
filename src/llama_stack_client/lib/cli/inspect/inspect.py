import click

from .version import inspect_version


@click.group()
@click.help_option("-h", "--help")
def inspect():
    """Inspect server configuration."""


# Register subcommands
inspect.add_command(inspect_version)
