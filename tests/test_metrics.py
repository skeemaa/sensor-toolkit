import pytest

from sensor_toolkit.metrics import rms
from sensor_toolkit.metrics import peak_to_peak


#Calculate the RMS of the constant signal [3.0, 3.0, 3.0] and verify that the result is approximately 3.0
def test_rms_of_constant_signal() -> None:
    assert rms ([3.0, 3.0, 3.0]) == pytest.approx(3.0)

#Calculate the peak-to-peak voltage and verify that the result is approximately 7.0
def test_peak_to_peak() -> None:
    assert peak_to_peak([-2.0, 1.0, 5.0]) == pytest.approx(7.0)

def test_rms_rejects_empty_input() -> None:
    with pytest.raises(ValueError, match="Samples must not be empty"):
        rms([])

def test_peak_to_peak_rejects_empty_input() -> None:
    with pytest.raises(ValueError, match="Samples must not be empty"):
        peak_to_peak([])