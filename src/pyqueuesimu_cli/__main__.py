"""Command line interface executable of pyqueuesimu."""
import typer
from rich import print

from pyqueuesimu import depart_process_simulation
from pyqueuesimu import poisson_process_simulation


app = typer.Typer()


@app.command()
def pyqueuesimu_cli() -> None:
    """Run the queue simulation."""
    print("hello world!")
    T = poisson_process_simulation()
    TS = depart_process_simulation(T)
    print(T)
    print(TS)