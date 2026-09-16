from collections.abc import Sequence
from math import sqrt


def rms(samples: Sequence[float]) -> float:
    """Calculate the RMS value of a signal"""

    if not samples:
        raise ValueError("samples must not be empty")

    squared_sum = sum(value**2 for value in samples)
    mean_square = squared_sum / len(samples)
    return sqrt(mean_square)

def peak_to_peak(samples: Sequence[float]) -> float:
    """Calculate the peak-to-peak value of a signal"""

    if not samples:
        raise ValueError("samples must not be empty")

    peak_to_peak_value = max(samples) - min(samples)
    return peak_to_peak_value

def moving_average(samples: Sequence[float], window_size: int) -> list[float]:
    """Calculate moving averages over a signal using overlapping windows."""

    if not samples:
        raise ValueError("samples must not be empty")

    if window_size <= 0:
        raise ValueError("window_size must be positive")

    if window_size > len(samples):
        raise ValueError("window_size must not exceed the number of samples")

    results: list[float] = []
    number_of_windows = len(samples) - window_size + 1

    for start in range(number_of_windows):
        window = samples[start : start + window_size]
        average = sum(window) / len(window)
        results.append(average)

    return results