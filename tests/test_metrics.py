import pytest

from sensor_toolkit.metrics import rms, peak_to_peak, moving_average, threshold_crossings


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

# Ensure that threshold crossings function detects when values cross the threshold in both directions
def test_threshold_crossings_detects_both_directions() -> None:
    assert threshold_crossings([1, 4, 6, 3, 7], threshold=5) == pytest.approx([2, 3, 4])

# Ensure that reaching the threshold from either side counts as a crossing, but moving away does not create an additional crossing
def test_threshold_crossings_include_reaching_threshold() -> None:
    assert threshold_crossings([4, 5, 6, 5, 4], threshold=5) == pytest.approx([1, 3])

# Ensure threshold crossings rejects empty inputs
def test_threshold_crossings_rejects_empty_input() -> None:
    with pytest.raises(ValueError, match="samples must not be empty"):
        threshold_crossings([], 5)

# Ensure threshold crossings returns empty when there are no crossings
def test_threshold_crossings_returns_empty_when_no_crossings() -> None:
    assert threshold_crossings([1, 2, 3], 5) == []
    assert threshold_crossings([7], 5) == []