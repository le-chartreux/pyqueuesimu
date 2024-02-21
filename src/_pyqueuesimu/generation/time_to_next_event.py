import math
import random


def generate_time_to_next_event(event_rate: float) -> float:
    """Generate the time to the next event following an exponential law."""
    # random is fine because we aren't doing some cryptography -> disable security lint
    return -(math.log(random.random()) / event_rate)  # noqa: S311
