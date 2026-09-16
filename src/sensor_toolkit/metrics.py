from collections.abc import Sequence
from math import sqrt


#Calculate the RMS value of a signal
def rms(samples: Sequence[float]) -> float:
    squared_sum = sum(value**2 for value in samples)
    mean_square = squared_sum / len(samples)
    return sqrt(mean_square)