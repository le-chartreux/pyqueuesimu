"""Command line interface executable of pyqueuesimu."""
import typer
from rich import print

from pyqueuesimu import depart_process_simulation
from pyqueuesimu import poisson_process_simulation


app = typer.Typer()


@app.command()
def pyqueuesimu_cli(
    constant_arrival_rate: float,
    exponential_service_law_parameter: float,
    observation_duration: float = 60
) -> None:
    """Run the queue simulation.

    Args:
        - constant_arrival_rate: inter-arrival time of clients.
        - exponential_service_law_parameter: parameter of the exponential law that
            the service time follows.
        - observation_duration: how long the observation should last.
    """
    print(f"The inter-arrival time of clients is {constant_arrival_rate}.")
    print(f"The service time follows an exponential law of parameter {exponential_service_law_parameter}.")
