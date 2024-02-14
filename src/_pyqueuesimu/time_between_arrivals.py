import math
import random


def generate_times_between_arrivals(
    constant_arrival_rate: float, observation_duration: float
) -> list[float]:
    """Create a list of inter-arrival times from an exponential law.

    Returns:
        An ordinated list where result[i] is the number of time units between the
        arrival of client i-1 and client i. result[0] is the number of time units before
        the arrival of the first client.
    """
    times_between_arrivals = []
    while sum(times_between_arrivals) < observation_duration:
        times_between_arrivals.append(
            _generate_time_to_next_arrival(constant_arrival_rate)
        )
    if sum(times_between_arrivals) != observation_duration:
        # not the last one because it goes after the observation duration
        times_between_arrivals.pop()
    return times_between_arrivals


def _generate_time_to_next_arrival(constant_arrival_rate: float) -> float:
    """Generate the time to the next arrival following an exponential law."""
    return -(math.log(random.random()) / constant_arrival_rate)
