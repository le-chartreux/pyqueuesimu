import math
import statistics


def compute_confidence_interval_95_percents(stats: list[float]) -> tuple[float, float]:
    # 1.96 is OK to get a 95% confidence interval with more than 30 elements
    t_critical = 1.96
    sample_mean = statistics.mean(stats)
    sample_standard_deviation = statistics.stdev(stats)
    standard_error = sample_standard_deviation / math.sqrt(len(stats))
    margin_of_error = t_critical * standard_error
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
    return lower_bound, upper_bound
