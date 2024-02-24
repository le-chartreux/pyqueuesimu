def get_loss_rate(departures: list[float | None]) -> float:
    """Get the percentage of None (lost clients) in the departures."""
    # Prevent divide by zero
    return departures.count(None) / len(departures) if departures else 0
