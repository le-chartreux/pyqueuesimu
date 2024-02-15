"""Command line interface executable of pyqueuesimu."""

import typer
from rich import print

from pyqueuesimu import (
    generate_inter_events_times_exponential,
    get_arrival_times_from_time_between_arrivals,
)

app = typer.Typer()


@app.command()
def pyqueuesimu_cli(
    constant_arrival_rate: float,
    exponential_service_law_parameter: float,
    observation_duration: float = 60,
) -> None:
    """Run the queue simulation.

    Args:
        constant_arrival_rate: inter-arrival time of clients.
        exponential_service_law_parameter: parameter of the exponential law that
            the service time follows.
        observation_duration: how long the observation should last.
    """
    time_between_arrivals = generate_inter_events_times_exponential(
        constant_arrival_rate, observation_duration
    )
    print(f"Time between arrivals: {time_between_arrivals}")
    arrival_times = get_arrival_times_from_time_between_arrivals(time_between_arrivals)
    print(f"Arrival times: {arrival_times}")
