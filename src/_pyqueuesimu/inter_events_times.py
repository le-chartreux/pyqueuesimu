import math
import random


def generate_inter_events_times_exponential(
    constant_rate: float, observation_duration: float
) -> list[float]:
    """Create a list of durations between events that follows an exponential law.

    Args:
        constant_rate: rate that the exponential law follows.
        observation_duration: how long should the observation be.

    Returns:
        An ordinated list where result[i] is the number of time units between the event
        i-1 and event i. result[0] is the number of time units before the first event.
    """
    times_between_events: list[float] = []
    while sum(times_between_events) < observation_duration:
        times_between_events.append(_generate_time_to_next_event(constant_rate))
    if sum(times_between_events) != observation_duration:
        # not the last one because it goes after the observation duration
        times_between_events.pop()
    return times_between_events


def _generate_time_to_next_event(constant_arrival_rate: float) -> float:
    """Generate the time to the next event following an exponential law."""
    # random is fine because we aren't doing some cryptography -> disable security lint
    return -(math.log(random.random()) / constant_arrival_rate)  # noqa: S311
