import math
import statistics


def get_confidence_interval_95_percents(stats: list[float]) -> tuple[float, float]:
    """Compute a confidence interval at 95% for the given statistics.

    A static t-critical of 1.96 is used because it's OK for intervals on more than
    30 elements.

    Args:
        stats: elements to compute a 95% interval on them. Must be longer than 30.
    """
    t_critical = 1.96
    sample_mean = statistics.mean(stats)
    sample_standard_deviation = statistics.stdev(stats)
    standard_error = sample_standard_deviation / math.sqrt(len(stats))
    margin_of_error = t_critical * standard_error
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
    return lower_bound, upper_bound
