"""
Shared helper for computing energy metrics from a codecarbon EmissionsTracker.

Pulled out into its own module (rather than importing from main.py) so it can
be imported without triggering the training pipeline that main.py runs at
import time.
"""


def energy_stats(energy_consumption_kwh, energy_tracker):
    """Extract and compute energy metrics from codecarbon Energy Tracker.
    IMPORTANT: this function should be called right after stopping the tracker.
    """
    energy_consumption_joules = energy_consumption_kwh * 1000 * 3600  # Joules
    duration = energy_tracker._last_measured_time - energy_tracker._start_time
    return energy_consumption_joules, duration
