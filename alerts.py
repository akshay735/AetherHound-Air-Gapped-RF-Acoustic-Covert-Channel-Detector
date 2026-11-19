def generate_alerts(data):

    # Create an empty list to store warnings
    alerts = []

    # Check RF signal status
    if data["rf_status"].lower() == "suspicious":
        alerts.append("WARNING: Suspicious RF activity detected!")

    # Check acoustic signal status
    if data["acoustic_status"].lower() == "suspicious":
        alerts.append("WARNING: Unusual acoustic activity detected!")

    # Check machine learning detection result
    if data["detection_status"].lower() in ["anomaly", "suspicious"]:
        alerts.append("WARNING: Machine learning anomaly detected!")

    # Return all generated warnings
    return alerts