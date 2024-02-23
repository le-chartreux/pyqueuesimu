def get_server_occupancy_rate(
    cumulated_time_for_each_number_of_clients: list[float],
) -> float:
    """Compute the occupancy rate of the server.

    Args:
        cumulated_time_for_each_number_of_clients: list where cumulated_time_for_each_number_of_clients is the number of time units where i
        clients were in the system.
    """
    observation_duration = sum(cumulated_time_for_each_number_of_clients)
    return (
        observation_duration - cumulated_time_for_each_number_of_clients[0]
    ) / observation_duration


def get_average_number_of_clients(
    cumulated_time_for_each_number_of_clients: list[float],
) -> float:
    """Compute the average number of clients.

    Args:
        cumulated_time_for_each_number_of_clients: list where cumulated_time_for_each_number_of_clients is the number of time units where i
        clients were in the system.
    """
    pondered_times = [
        clients_in_system_time * i
        for i, clients_in_system_time in enumerate(
            cumulated_time_for_each_number_of_clients
        )
    ]
    return sum(pondered_times) / sum(cumulated_time_for_each_number_of_clients)


def get_cumulated_time_for_each_number_of_clients(
    arrival_times: list[float],
    departure_times: list[float],
    observation_duration: float,
) -> list[float]:
    """Compute the cumulated time for each number of clients (A.K.A 'T').

    Args:
        arrival_times: list where arrival_times[i] is the moment where client i arrived.
        departure_times: list where departure_times[i] is the moment where client i left.
        observation_duration: how long the observation lasts.

    Returns:
        A list where result[i] is the number of time units where i clients were in the
        system.
    """
    events = [(time, "ARRIVAL") for time in arrival_times] + [
        (time, "DEPARTURE") for time in departure_times
    ]
    # Add a final arrival with an empty duration to handle the final segment from the
    # last event to the end of the observation period
    events.append((observation_duration, "ARRIVAL"))
    events.sort()

    current_number_of_clients = 0
    last_event_time = 0.0
    T = [0.0]  # Initialize T with one element to handle the system with 0 clients

    # Process each event
    for event_time, event_type in events:
        time_diff = event_time - last_event_time

        # Update the duration for the current number of clients
        if current_number_of_clients < len(T):
            T[current_number_of_clients] += time_diff
        else:
            # Extend T if we have more clients than previously encountered
            T.extend([0.0] * (current_number_of_clients - len(T) + 1))
            T[current_number_of_clients] = time_diff

        if event_type == "ARRIVAL":
            current_number_of_clients += 1
        else:  # departure
            current_number_of_clients -= 1

        last_event_time = event_time

    # Remove all the possible trailing zeros except the zero to say that there is
    # no time with 0 clients
    while len(T) > 1 and T[-1] == 0:
        T.pop()

    return T
