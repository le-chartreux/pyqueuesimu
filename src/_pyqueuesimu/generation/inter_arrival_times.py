from _pyqueuesimu.generation.time_to_next_event import generate_time_to_next_event


def generate_inter_arrival_times(
    arrival_rate: float, observation_duration: float
) -> list[float]:
    """Create a list of durations between arrivals that follows an exponential law.

    Args:
        arrival_rate: number of client arrival per time unit.
        observation_duration: how long should the observation be.

    Returns:
        An ordinated list where result[i] is the number of time units between the
        arrival of client i-1 and the arrival of client i. result[0] is the number of
        time units before the first arrival.
        The sum of the elements is inferior to the observation duration.
    """
    times_between_arrivals: list[float] = []
    while sum(times_between_arrivals) <= observation_duration:
        times_between_arrivals.append(generate_time_to_next_event(arrival_rate))
    # not the last one because it goes after the observation duration
    times_between_arrivals.pop()
    return times_between_arrivals
