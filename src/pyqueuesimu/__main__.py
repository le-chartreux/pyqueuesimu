"""Command line interface executable of pyqueuesimu."""

import matplotlib.pyplot as plt
import typer
from rich import print

from pyqueuesimu import (
    generate_inter_arrival_times,
    generate_service_times,
    get_arrival_times,
    get_average_number_of_clients,
    get_average_service_time,
    get_average_waiting_time,
    get_confidence_interval_95_percents,
    get_cumulated_time_for_each_number_of_clients,
    get_departure_times,
    get_departure_times_limited_buffer,
    get_incoming_throughput,
    get_loss_rate,
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
    buffer_size: int = -1,
) -> None:
    """Run the queue simulation and output to command line.

    Arrival rate and service rate follows an exponential law based on the given
    average values.

    Args:
        arrival_rate: number of client arrival per time unit.
        service_rate: average number of clients per time units that are served.
        observation_duration: how long the observation should last.
        buffer_size: size of the buffer. If the number of clients is greater than the
            buffer size + 1 (because of the client that is currently serviced), the
            next clients to arrive will be lost (value of None). If negative value,
            unlimited buffer.
    """
    time_between_arrivals, arrival_times, service_times, departure_times = (
        _generate_simulation(
            arrival_rate, service_rate, observation_duration, buffer_size
        )
    )
    print(f"Time between arrivals: {time_between_arrivals}")
    print(f"Arrival times: {arrival_times}")
    print(f"Service times: {service_times}")
    print(f"Departure times: {departure_times}")
    _show_stats(
        arrival_times, departure_times, service_times, observation_duration, buffer_size
    )


@app.command()
def cli_confidence_interval_on_stats_95_percent(
    arrival_rate: float,
    service_rate: float,
    observation_duration: float = 60,
    buffer_size: int = -1,
) -> None:
    """Compute stats on the queue simulation with confidence interval of 95%.

    Arrival rate and service rate follows an exponential law based on the given
    average values.

    Args:
        arrival_rate: number of client arrival per time unit.
        service_rate: average number of clients per time units that are served.
        observation_duration: how long the observation should last.
        buffer_size: size of the buffer. If the number of clients is greater than the
            buffer size + 1 (because of the client that is currently serviced), the
            next clients to arrive will be lost (value of None). If negative value,
            unlimited buffer.
    """
    stats_average_waiting_time = []
    stats_average_service_time = []
    stats_average_number_of_clients = []
    stats_server_occupancy_rate = []
    stats_incoming_throughput = []
    stats_outgoing_throughput = []
    for _ in range(100):
        _, arrival_times, service_times, departure_times = _generate_simulation(
            arrival_rate, service_rate, observation_duration, buffer_size
        )

        waiting_times = get_waiting_times(arrival_times, departure_times, service_times)

        stats_average_waiting_time.append(get_average_waiting_time(waiting_times))
        stats_average_service_time.append(get_average_service_time(service_times))
        cumulated_time_for_each_number_of_clients = (
            get_cumulated_time_for_each_number_of_clients(
                arrival_times, departure_times, observation_duration
            )
        )
        stats_average_number_of_clients.append(
            get_average_number_of_clients(cumulated_time_for_each_number_of_clients)
        )
        stats_server_occupancy_rate.append(
            get_server_occupancy_rate(cumulated_time_for_each_number_of_clients)
        )
        stats_incoming_throughput.append(
            get_incoming_throughput(arrival_times, observation_duration)
        )
        stats_outgoing_throughput.append(
            get_outgoing_throughput(departure_times, observation_duration)
        )

    print(
        "Confidence interval for average waiting time: "
        f"{get_confidence_interval_95_percents(stats_outgoing_throughput)}"
    )
    print(
        "Confidence interval for average service time: "
        f"{get_confidence_interval_95_percents(stats_average_service_time)}"
    )
    print(
        "Confidence interval for average number of clients: "
        f"{get_confidence_interval_95_percents(stats_average_number_of_clients)}"
    )
    print(
        "Confidence interval for average occupancy rate: "
        f"{get_confidence_interval_95_percents(stats_server_occupancy_rate)}"
    )
    print(
        "Confidence interval for incoming throughput: "
        f"{get_confidence_interval_95_percents(stats_incoming_throughput)}"
    )
    print(
        "Confidence interval for outgoing throughput: "
        f"{get_confidence_interval_95_percents(stats_outgoing_throughput)}"
    )


@app.command()
def gui(
    arrival_rate: float,
    service_rate: float,
    observation_duration: float = 60,
    time_unit: str = "",
    buffer_size: int = -1,
) -> None:
    """Run the queue simulation and output to a graphical interface (plot).

    Arrival rate and service rate follows an exponential law based on the given
    average values.

    Args:
        arrival_rate: number of client arrival per time unit.
        service_rate: average number of clients per time units that are served.
        observation_duration: how long the observation should last.
        time_unit: optional parameter to indicate the time unit (only aesthetic).
        buffer_size: size of the buffer. If the number of clients is greater than the
            buffer size + 1 (because of the client that is currently serviced), the
            next clients to arrive will be lost (value of None). If negative value,
            unlimited buffer.
    """
    _, arrival_times, service_times, departure_times = _generate_simulation(
        arrival_rate, service_rate, observation_duration, buffer_size
    )
    plt.plot(arrival_times, label="Arrivals")
    plt.plot(departure_times, label="Departures")
    # Identify and highlight lost clients
    for i, value in enumerate(departure_times):
        if value is None:
            plt.axvspan(i - 0.1, i + 0.1, color="red", alpha=0.1)
    plt.xlabel("Client number")
    plt.ylabel(f"Time {f'({time_unit})' if time_unit else ''}")
    plt.title("Arrival and Departure of Clients")
    plt.legend()
    plt.show()
    _show_stats(
        arrival_times,
        departure_times,
        service_times,
        observation_duration,
        buffer_size,
        time_unit,
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


def _show_stats(
    arrival_times: list[float],
    departure_times: list[float],
    service_times: list[float],
    observation_duration: float,
    buffer_size: int,
    time_unit: str = "",
) -> None:
    """Show some statistics about the execution."""
    if buffer_size >= 0:
        _show_stats_with_buffer(
            arrival_times,
            departure_times,
            service_times,
            observation_duration,
            buffer_size,
            time_unit,
        )
    else:
        _show_stats_without_buffer(
            arrival_times,
            departure_times,
            service_times,
            observation_duration,
            time_unit,
        )


def _show_stats_with_buffer(
    arrival_times: list[float],
    departure_times: list[float],
    service_times: list[float],
    observation_duration: float,
    buffer_size: int,
    time_unit: str = "",
) -> None:
    """Show some statistics about the execution when a buffer size is set."""
    del arrival_times  # unused for now
    del service_times  # unused for now
    del observation_duration  # unused for now
    del buffer_size  # unused for now
    del time_unit  # unused for now
    loss_rate = get_loss_rate(departure_times)
    print(f"Loss rate: {loss_rate}")


def _show_stats_without_buffer(
    arrival_times: list[float],
    departure_times: list[float],
    service_times: list[float],
    observation_duration: float,
    time_unit: str,
) -> None:
    """Show some statistics about the execution when no buffer size is set."""
    waiting_times = get_waiting_times(arrival_times, departure_times, service_times)
    average_waiting_time = get_average_waiting_time(waiting_times)
    average_service_time = get_average_service_time(service_times)
    cumulated_time_for_each_number_of_clients = (
        get_cumulated_time_for_each_number_of_clients(
            arrival_times, departure_times, observation_duration
        )
    )
    average_number_of_clients = get_average_number_of_clients(
        cumulated_time_for_each_number_of_clients
    )
    server_occupancy_rate = get_server_occupancy_rate(
        cumulated_time_for_each_number_of_clients
    )
    incoming_throughput = get_incoming_throughput(arrival_times, observation_duration)
    outgoing_throughput = get_outgoing_throughput(departure_times, observation_duration)

    print(f"Average waiting time: {average_waiting_time} {time_unit}")
    print(f"Average service time: {average_service_time} {time_unit}")
    print(f"Average number of clients: {average_number_of_clients}")
    print(f"Server occupancy rate: {server_occupancy_rate}")
    print(f"Incoming throughput: {incoming_throughput}")
    print(f"Outgoing throughput: {outgoing_throughput}")


def _generate_simulation(
    arrival_rate: float,
    service_rate: float,
    observation_duration: float,
    buffer_size: int,
) -> tuple[list[float], list[float], list[float], list[float | None]]:
    """Create the values of the simulation.

    Args:
        arrival_rate: number of client arrival per time unit.
        service_rate: average number of clients per time units that are served.
        observation_duration: how long the observation should last.
        buffer_size: size of the buffer. If the number of clients is greater than the
            buffer size + 1 (because of the client that is currently serviced), the
            next clients to arrive will be lost (value of None). If negative value,
            unlimited buffer.

    Returns:
        A tuple (time_between_arrivals, arrival_times, service_times, departure_times).
    """
    time_between_arrivals = generate_inter_arrival_times(
        arrival_rate, observation_duration
    )
    arrival_times = get_arrival_times(time_between_arrivals)
    service_times = generate_service_times(service_rate, len(arrival_times))
    if buffer_size < 0:
        departure_times = get_departure_times(arrival_times, service_times)
    else:
        departure_times = get_departure_times_limited_buffer(
            arrival_times, service_times, buffer_size
        )
    return time_between_arrivals, arrival_times, service_times, departure_times
