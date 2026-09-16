import pytest

from sensor_toolkit.metrics import rms


#Calculate the RMS of the constant signal [3.0, 3.0, 3.0] and verify that the result is approximately 3.0.
def test_rms_of_constant_signal() -> None:
    assert rms ([3.0, 3.0, 3.0]) == pytest.approx(3.0)