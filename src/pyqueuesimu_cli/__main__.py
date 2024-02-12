"""Command line interface executable of pyqueuesimu."""
import typer
from rich import print


app = typer.Typer()


@app.command()
def pyqueuesimu_cli() -> None:
    """Run the queue simulation."""
    print("hello world!")
