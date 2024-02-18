"""Command line interface executable of pyqueuesimu."""
import matplotlib.pyplot as plt
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
def cli(
    arrival_rate: float,
    service_rate: float,
    observation_duration: float = 60,
) -> None:
    """Run the queue simulation and output to command line.

    Arrival rate and service rate follows an exponential law based on the given
    average values.

    Args:
        arrival_rate: number of client arrival per time unit.
        service_rate: average number of clients per time units that are served.
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


@app.command()
def gui(
    arrival_rate: float,
    service_rate: float,
    observation_duration: float = 60,
    time_unit: str = ""
) -> None:
    """Run the queue simulation and output to a graphical interface (plot).

    Arrival rate and service rate follows an exponential law based on the given
    average values.

    Args:
        arrival_rate: number of client arrival per time unit.
        service_rate: average number of clients per time units that are served.
        observation_duration: how long the observation should last.
        time_unit: optional parameter to indicate the time unit (only aesthetic).
    """
    time_between_arrivals = generate_inter_arrival_times(
        arrival_rate, observation_duration
    )
    arrival_times = get_arrival_times(time_between_arrivals)
    service_times = generate_service_times(service_rate, len(arrival_times))
    departure_times = get_departure_times(arrival_times, service_times)
    plt.plot(arrival_times, label="Arrivals")
    plt.plot(departure_times, label="Departures")
    plt.xlabel("Client number")
    plt.ylabel(f"Time {f'({time_unit})' if time_unit else ''}")
    plt.title("Arrival and Departure of Clients")
    plt.legend()
    plt.show()


@app.command()
def gui_example(k: int = 2, observation_duration: float = 60) -> None:
    """Run the queue simulation with GUI and coherent values based on the given k.

    The arrival rate is (324 - 24*k) requests/second and a service takes
    (0.5 * k + 1) ms/request.
    """
    arrival_rate = 324 - 24*k
    service_rate = 1 / ((0.5 * k + 1) / 1000)
    gui(arrival_rate, service_rate, observation_duration, time_unit="seconds")
