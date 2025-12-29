"""Console script for disinformation_classification_pietervanbrakel."""

import typer
from rich.console import Console

from disinformation_classification_pietervanbrakel import utils

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for disinformation_classification_pietervanbrakel."""
    console.print("Replace this message by putting your code into "
               "disinformation_classification_pietervanbrakel.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
