
import math
import random
from datetime import datetime


def generate_monitoring_data(frame):
    """
    Generate simulated RF and acoustic monitoring data.
    This is a software-only simulation.
    """

    # Simulate occasional abnormal activity
    abnormal_event = (frame % 150) < 20

    # RF monitoring
    rf_frequency = random.uniform(2390, 2420)
    rf_amplitude = random.uniform(0.2, 0.6)

    if abnormal_event:
        rf_amplitude = random.uniform(0.8, 1.0)
        rf_status = "Suspicious"
    elif rf_amplitude > 0.5:
        rf_status = "Warning"
    else:
        rf_status = "Normal"

    # Acoustic monitoring
    acoustic_amplitude = random.uniform(0.1, 0.5)

    if abnormal_event:
        acoustic_amplitude = random.uniform(0.8, 1.0)
        acoustic_status = "Suspicious"
        acoustic_signal = "Unusual periodic sound"
    elif acoustic_amplitude > 0.4:
        acoustic_status = "Warning"
        acoustic_signal = "Elevated sound activity"
    else:
        acoustic_status = "Normal"
        acoustic_signal = "Normal background noise"

    # Simulated anomaly detection
    anomaly_score = random.uniform(0.75, 0.98) if abnormal_event else random.uniform(0.01, 0.35)

    detection_status = (
        "Anomaly" if anomaly_score >= 0.70 else "Normal"
    )

    # Generate simulated spectrum bins
    spectrum = []

    for i in range(64):
        base_signal = (
            0.15
            + 0.25 * abs(math.sin(i * 0.25 + frame * 0.08))
        )

        noise = random.uniform(0, 0.08)
        amplitude = base_signal + noise

        # Add abnormal frequency spikes
        if abnormal_event and i in (15, 16, 42, 43):
            amplitude = random.uniform(0.85, 1.0)

        spectrum.append(min(amplitude, 1.0))

    return {
        "rf_frequency": round(rf_frequency, 2),
        "rf_amplitude": round(rf_amplitude, 3),
        "rf_status": rf_status,

        "acoustic_signal": acoustic_signal,
        "acoustic_amplitude": round(acoustic_amplitude, 3),
        "acoustic_status": acoustic_status,

        "anomaly_score": round(anomaly_score, 3),
        "detection_status": detection_status,

        "spectrum": spectrum,
        "timestamp": datetime.now().strftime("%H:%M:%S.%f")[:-3]
    }
