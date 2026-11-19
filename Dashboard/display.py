from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# Create terminal display
console = Console()


def display_dashboard(data, alerts):

    # Create dashboard table
    table = Table(title="AETHERHOUND MONITOR")

    table.add_column("Parameter", style="cyan")
    table.add_column("Value", style="white")
    table.add_column("Status", style="green")

    # Display RF information
    table.add_row(
        "RF Frequency",
        str(data["rf_frequency"]),
        data["rf_status"]
    )

    # Display acoustic information
    table.add_row(
        "Acoustic Signal",
        data["acoustic_signal"],
        data["acoustic_status"]
    )

    # Display anomaly information
    table.add_row(
        "Anomaly Score",
        str(data["anomaly_score"]),
        data["detection_status"]
    )

    # Show dashboard table
    console.print(
        Panel(table, border_style="blue")
    )

    # Display alerts
    alert_text = "\n".join(alerts) if alerts else "No alerts detected."

    console.print(
        Panel(alert_text, title="ALERTS", border_style="red")
    )