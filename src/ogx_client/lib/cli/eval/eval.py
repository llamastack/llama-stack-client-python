import click

from .run_scoring import run_scoring
from .run_benchmark import run_benchmark


@click.group()
@click.help_option("-h", "--help")
def eval():
    """Run evaluation tasks."""


# Register subcommands
eval.add_command(run_benchmark)
eval.add_command(run_scoring)
