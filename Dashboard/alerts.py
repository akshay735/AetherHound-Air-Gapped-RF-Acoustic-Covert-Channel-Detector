
from datetime import datetime


def generate_alerts(data):

    alerts = []

    timestamp = data.get(
        "timestamp",
        datetime.now().strftime("%H:%M:%S")
    )

    # RF alerts
    if data["rf_status"].lower() == "suspicious":
        alerts.append(
            f"[{timestamp}] [CRITICAL] Suspicious RF activity detected!"
        )

    elif data["rf_status"].lower() == "warning":
        alerts.append(
            f"[{timestamp}] [WARNING] Unusual RF activity detected."
        )

    # Acoustic alerts
    if data["acoustic_status"].lower() == "suspicious":
        alerts.append(
            f"[{timestamp}] [CRITICAL] Unusual acoustic activity detected!"
        )

    elif data["acoustic_status"].lower() == "warning":
        alerts.append(
            f"[{timestamp}] [WARNING] Elevated acoustic activity detected."
        )

    # Machine learning alerts
    if data["detection_status"].lower() in ["anomaly", "suspicious"]:
        alerts.append(
            f"[{timestamp}] [CRITICAL] Machine learning anomaly detected!"
        )

    return alerts
