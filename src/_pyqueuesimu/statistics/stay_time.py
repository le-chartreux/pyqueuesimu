import statistics


def get_stay_times(
    arrival_times: list[float], departure_times: list[float]
) -> list[float]:
    return [
        departure_time - arrival_time
        for arrival_time, departure_time in zip(
            arrival_times, departure_times, strict=True
        )
    ]


def get_average_stay_time(stay_times: list[float]) -> float:
    return statistics.mean(stay_times)
