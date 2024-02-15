"""Command line interface executable of pyqueuesimu."""

import typer
from rich import print

from pyqueuesimu import (
    generate_inter_arrival_times,
    generate_service_times,
    get_arrival_times,
    get_departure_times,
)

app = typer.Typer()


@app.command()
def pyqueuesimu_cli(
    arrival_rate: float,
    service_rate: float,
    observation_duration: float = 60,
) -> None:
    """Run the queue simulation.

    Args:
        arrival_rate: parameter of the exponential law that the arrival time follows.
        service_rate: parameter of the exponential law that the service time follows.
        observation_duration: how long the observation should last.
    """
    time_between_arrivals = generate_inter_arrival_times(
        arrival_rate, observation_duration
    )
    print(f"Time between arrivals: {time_between_arrivals}")
    arrival_times = get_arrival_times(time_between_arrivals)
    print(f"Arrival times: {arrival_times}")
    service_times = generate_service_times(service_rate, len(arrival_times))
    print(f"Service times: {service_times}")
    departure_times = get_departure_times(arrival_times, service_times)
    print(f"Departure times: {departure_times}")
