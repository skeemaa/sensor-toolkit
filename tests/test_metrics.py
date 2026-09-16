import pytest

from sensor_toolkit.metrics import rms, peak_to_peak, moving_average


# Calculate the RMS of the constant signal [3.0, 3.0, 3.0] and verify that the result is approximately 3.0
def test_rms_of_constant_signal() -> None:
    assert rms ([3.0, 3.0, 3.0]) == pytest.approx(3.0)

# Calculate the peak-to-peak voltage and verify that the result is approximately 7.0
def test_peak_to_peak() -> None:
    assert peak_to_peak([-2.0, 1.0, 5.0]) == pytest.approx(7.0)

# Ensure RMS function rejects empty inputs
def test_rms_rejects_empty_input() -> None:
    with pytest.raises(ValueError, match="samples must not be empty"):
        rms([])

# Ensure peak-to-peak function rejects empty inputs
def test_peak_to_peak_rejects_empty_input() -> None:
    with pytest.raises(ValueError, match="samples must not be empty"):
        peak_to_peak([])

# Calculate the moving average of signal [1.0, 2.0, 3.0, 4.0] and verify the result is [1.5, 2.5, 3.5]
def test_moving_average_with_window_size_two() -> None:
    assert moving_average([1.0, 2.0, 3.0, 4.0], window_size=2) == pytest.approx([1.5, 2.5, 3.5])

# Ensure moving average function rejects empty inputs
def test_moving_average_rejects_empty_input() -> None:
    with pytest.raises(ValueError, match="samples must not be empty"):
        moving_average([], window_size=2)

# Ensure moving average function rejects zero window size
def test_moving_average_rejects_zero_window_size() -> None:
    with pytest.raises(ValueError, match="window_size must be positive"):
        moving_average([1.0, 2.0, 3.0, 4.0], window_size=0)

# Ensure moving average function rejects window size larger than available signal
def test_moving_average_rejects_oversized_window() -> None:
    with pytest.raises(ValueError, match="window_size must not exceed the number of samples"):
        moving_average([1.0, 2.0], window_size=3)