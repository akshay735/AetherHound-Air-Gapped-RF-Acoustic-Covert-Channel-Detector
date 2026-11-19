from display import display_dashboard
from alerts import generate_alerts
from datetime import datetime


def main():

    # Temporary sample data for testing
    data = {
        "rf_frequency": "2400 MHz",
        "rf_status": "Normal",
        "acoustic_signal": "Unusual sound detected",
        "acoustic_status": "Suspicious",
        "anomaly_score": 0.89,
        "detection_status": "Anomaly",
        "timestamp": str(datetime.now())
    }

    alerts = generate_alerts(data)

    display_dashboard(data, alerts)


if __name__ == "__main__":
    main()