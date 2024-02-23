"""Command line interface executable of pyqueuesimu."""

import matplotlib.pyplot as plt
import typer
from rich import print

from pyqueuesimu import (
    compute_confidence_interval_95_percents,
    generate_inter_arrival_times,
    generate_service_times,
    get_arrival_times,
    get_average_number_of_clients,
    get_average_service_time,
    get_average_waiting_time,
    get_clients_times,
    get_departure_times,
    get_incoming_throughput,
    get_outgoing_throughput,
    get_server_occupancy_rate,
    get_waiting_times,
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
    arrival_times = get_arrival_times(time_between_arrivals)
    service_times = generate_service_times(service_rate, len(arrival_times))
    departure_times = get_departure_times(arrival_times, service_times)
    print(f"Time between arrivals: {time_between_arrivals}")
    print(f"Arrival times: {arrival_times}")
    print(f"Service times: {service_times}")
    print(f"Departure times: {departure_times}")
    show_stats(arrival_times, departure_times, service_times, observation_duration)


@app.command()
def cli_confidence_interval_on_stats_95_percent(
    arrival_rate: float,
    service_rate: float,
    observation_duration: float = 60,
) -> None:
    """Compute stats on the queue simulation with confidence interval of 95%.

    Arrival rate and service rate follows an exponential law based on the given
    average values.

    Args:
        arrival_rate: number of client arrival per time unit.
        service_rate: average number of clients per time units that are served.
        observation_duration: how long the observation should last.
    """
    stats_average_waiting_time = []
    stats_average_service_time = []
    stats_average_number_of_clients = []
    stats_server_occupancy_rate = []
    stats_incoming_throughput = []
    stats_outgoing_throughput = []
    for _ in range(100):
        time_between_arrivals = generate_inter_arrival_times(
            arrival_rate, observation_duration
        )
        arrival_times = get_arrival_times(time_between_arrivals)
        service_times = generate_service_times(service_rate, len(arrival_times))
        departure_times = get_departure_times(arrival_times, service_times)
        waiting_times = get_waiting_times(arrival_times, departure_times, service_times)

        stats_average_waiting_time.append(get_average_waiting_time(waiting_times))
        stats_average_service_time.append(get_average_service_time(service_times))
        clients_in_system_times = get_clients_times(
            arrival_times, departure_times, observation_duration
        )
        stats_average_number_of_clients.append(
            get_average_number_of_clients(clients_in_system_times)
        )
        stats_server_occupancy_rate.append(
            get_server_occupancy_rate(clients_in_system_times)
        )
        stats_incoming_throughput.append(
            get_incoming_throughput(arrival_times, observation_duration)
        )
        stats_outgoing_throughput.append(
            get_outgoing_throughput(departure_times, observation_duration)
        )

    print(
        "Confidence interval for average waiting time: "
        f"{compute_confidence_interval_95_percents(stats_outgoing_throughput)}"
    )
    print(
        "Confidence interval for average service time: "
        f"{compute_confidence_interval_95_percents(stats_average_service_time)}"
    )
    print(
        "Confidence interval for average number of clients: "
        f"{compute_confidence_interval_95_percents(stats_average_number_of_clients)}"
    )
    print(
        "Confidence interval for average occupancy rate: "
        f"{compute_confidence_interval_95_percents(stats_server_occupancy_rate)}"
    )
    print(
        "Confidence interval for incoming throughput: "
        f"{compute_confidence_interval_95_percents(stats_incoming_throughput)}"
    )
    print(
        "Confidence interval for outgoing throughput: "
        f"{compute_confidence_interval_95_percents(stats_outgoing_throughput)}"
    )


@app.command()
def gui(
    arrival_rate: float,
    service_rate: float,
    observation_duration: float = 60,
    time_unit: str = "",
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
    show_stats(
        arrival_times, departure_times, service_times, observation_duration, time_unit
    )


@app.command()
def gui_example(k: int = 2, observation_duration: float = 60) -> None:
    """Run the queue simulation with GUI and coherent values based on the given k.

    The arrival rate is (324 - 24*k) requests/second and a service takes
    (0.5 * k + 1) ms/request.
    """
    arrival_rate = 324 - 24 * k
    service_rate = 1 / ((0.5 * k + 1) / 1000)
    gui(arrival_rate, service_rate, observation_duration, time_unit="seconds")


def show_stats(
    arrival_times: list[float],
    departure_times: list[float],
    service_times: list[float],
    observation_duration: float,
    time_unit: str = "",
) -> None:
    """Show some statistics about the execution."""
    waiting_times = get_waiting_times(arrival_times, departure_times, service_times)
    average_waiting_time = get_average_waiting_time(waiting_times)
    average_service_time = get_average_service_time(service_times)
    clients_in_system_times = get_clients_times(
        arrival_times, departure_times, observation_duration
    )
    average_number_of_clients_in_system = get_average_number_of_clients(
        clients_in_system_times
    )
    server_occupancy_rate = get_server_occupancy_rate(clients_in_system_times)
    incoming_throughput = get_incoming_throughput(arrival_times, observation_duration)
    outgoing_throughput = get_outgoing_throughput(departure_times, observation_duration)

    print(f"Average waiting time: {average_waiting_time} {time_unit}")
    print(f"Average service time: {average_service_time} {time_unit}")
    print(f"Average number of clients in system: {average_number_of_clients_in_system}")
    print(f"Server occupancy rate: {server_occupancy_rate}")
    print(f"Incoming throughput: {incoming_throughput}")
    print(f"Outgoing throughput: {outgoing_throughput}")
