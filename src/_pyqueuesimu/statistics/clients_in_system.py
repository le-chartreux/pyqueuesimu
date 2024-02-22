def get_average_number_of_clients_in_system(
    clients_in_system_times: list[float],
) -> float:
    pondered_times = [
        clients_in_system_time * i
        for i, clients_in_system_time in enumerate(clients_in_system_times)
    ]
    return sum(pondered_times) / sum(clients_in_system_times)


def get_clients_in_system_times(
    arrival_times: list[float],
    departure_times: list[float],
    observation_duration: float,
) -> list[float]:
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
