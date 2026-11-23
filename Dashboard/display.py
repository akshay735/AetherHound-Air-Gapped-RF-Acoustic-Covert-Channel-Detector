
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.columns import Columns

console = Console()


def get_status_style(status):
    status = status.lower()

    if status in ("suspicious", "anomaly"):
        return "bold red"
    elif status == "warning":
        return "bold yellow"

    return "bold green"


def create_spectrum(spectrum, width=64):
    bars = Text()

    for value in spectrum[:width]:
        height = max(0, min(8, int(value * 8)))

        if value >= 0.8:
            style = "red"
        elif value >= 0.5:
            style = "yellow"
        else:
            style = "green"

        bars.append("█" * height + " ", style=style)

    return bars


def create_monitoring_table(data):
    table = Table(
        title="SIGNAL MONITORING",
        expand=True
    )

    table.add_column("Parameter", style="cyan")
    table.add_column("Value")
    table.add_column("Status")

    table.add_row(
        "RF Frequency",
        f"{data['rf_frequency']} MHz",
        Text(data["rf_status"], style=get_status_style(data["rf_status"]))
    )

    table.add_row(
        "RF Amplitude",
        str(data["rf_amplitude"]),
        Text(data["rf_status"], style=get_status_style(data["rf_status"]))
    )

    table.add_row(
        "Acoustic Signal",
        data["acoustic_signal"],
        Text(
            data["acoustic_status"],
            style=get_status_style(data["acoustic_status"])
        )
    )

    table.add_row(
        "Acoustic Amplitude",
        str(data["acoustic_amplitude"]),
        Text(
            data["acoustic_status"],
            style=get_status_style(data["acoustic_status"])
        )
    )

    table.add_row(
        "Anomaly Score",
        str(data["anomaly_score"]),
        Text(
            data["detection_status"],
            style=get_status_style(data["detection_status"])
        )
    )

    return table


def create_dashboard(data, alerts, spectrum_history):
    monitoring_table = create_monitoring_table(data)

    spectrum_panel = Panel(
        create_spectrum(data["spectrum"]),
        title="LIVE RF SPECTRUM",
        border_style="blue"
    )

    waterfall_lines = []

    for spectrum in spectrum_history[-8:]:
        waterfall_lines.append(create_spectrum(spectrum))

    waterfall_text = Text("\n").join(waterfall_lines)

    waterfall_panel = Panel(
        waterfall_text,
        title="SPECTRUM WATERFALL",
        border_style="magenta"
    )

    alert_table = Table(
        title="SECURITY ALERTS",
        expand=True
    )

    alert_table.add_column("Alert", style="white")

    if alerts:
        for alert in alerts:
            if "CRITICAL" in alert:
                style = "bold red"
            elif "WARNING" in alert:
                style = "bold yellow"
            else:
                style = "white"

            alert_table.add_row(Text(alert, style=style))
    else:
        alert_table.add_row(
            Text("No alerts detected.", style="bold green")
        )

    return Panel(
        Columns(
            [
                monitoring_table,
                spectrum_panel
            ],
            expand=True
        ),
        title="AETHERHOUND | RF & ACOUSTIC MONITOR",
        subtitle=f"Last updated: {data['timestamp']}",
        border_style="bright_blue"
    ), waterfall_panel, alert_table


def display_dashboard(data, alerts, spectrum_history):
    dashboard, waterfall, alert_panel = create_dashboard(
        data,
        alerts,
        spectrum_history
    )

    console.clear()
    console.print(dashboard)
    console.print(waterfall)
    console.print(alert_panel)
