# Sensor Toolkit

Small Python package that calculates basic signal metrics such as RMS, peak-to-peak amplitude, moving average, and threshold crossings.

## Features
- Root mean square (RMS) calculation
- Peak-to-peak amplitude calculation
- Moving average calculation
- Upward and downward threshold-crossing detection

## Installation
Prerequisites: Python 3.12 or newer and Git

1. Clone the repository and enter its directory.

    ```bash
    git clone https://github.com/skeemaa/sensor-toolkit.git
    cd sensor-toolkit
    ```

2. Create a virtual environment.

    ```bash
    python -m venv .venv
    ```

3. Activate it using Windows Git Bash.

    ```bash
    source .venv/Scripts/activate
    ```

4. Install the package and development dependencies.

    ```bash
    python -m pip install -e ".[dev]"
    ```
    - Note: `-e` creates an editable installation, so source-code changes are immediately available in the active virtual environment.

## Usage

```python
from sensor_toolkit.metrics import (
    moving_average,
    peak_to_peak,
    rms,
    threshold_crossings,
)

samples = [1.0, 2.0, 3.0, 2.0, 4.0]

signal_rms = rms(samples)
amplitude_range = peak_to_peak(samples)
smoothed_samples = moving_average(samples, window_size=3)
crossing_indices = threshold_crossings(samples, threshold=2.5) # [2, 3, 4]
```

## Running Tests

- Verify the virtual environment is active.

- Run
    ```bash
    python -m pytest
    ```

- Verify all tests pass.