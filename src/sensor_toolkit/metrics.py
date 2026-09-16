from collections.abc import Sequence
from math import sqrt


#Calculate the RMS value of a signal
def rms(samples: Sequence[float]) -> float:
    squared_sum = sum(value**2 for value in samples)
    mean_square = squared_sum / len(samples)
    return sqrt(mean_square)

#Calculate the peak-to-peak value of a signal
def peak_to_peak(samples: Sequence[float]) -> float:
    peak_to_peak_value = max(samples) - min(samples)
    return peak_to_peak_value