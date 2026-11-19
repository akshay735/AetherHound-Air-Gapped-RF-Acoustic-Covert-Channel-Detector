def generate_alerts(data):

    alerts = []

    if data["rf_status"].lower() == "suspicious":
        alerts.append("[WARNING] Suspicious RF activity detected!")

    if data["acoustic_status"].lower() == "suspicious":
        alerts.append("[WARNING] Unusual acoustic activity detected!")

    if data["detection_status"].lower() in ["anomaly", "suspicious"]:
        alerts.append("[WARNING] Machine learning anomaly detected!")

    return alerts