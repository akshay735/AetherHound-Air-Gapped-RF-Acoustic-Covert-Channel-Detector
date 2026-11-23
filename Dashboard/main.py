
import time
from collections import deque

from rich.live import Live
from rich.console import Console, Group
from rich.panel import Panel

from live_monitor import generate_monitoring_data
from alerts import generate_alerts
from display import create_dashboard


console = Console()


def main():

    frame = 0
    spectrum_history = deque(maxlen=5)

    fps_start = time.perf_counter()
    fps_frames = 0
    current_fps = 0.0

    print("Starting AETHERHOUND...")
    time.sleep(1)

    with Live(
        console=console,
        refresh_per_second=15,
        screen=True,
        transient=False
    ) as live:

        while True:

            loop_start = time.perf_counter()
            frame += 1
            fps_frames += 1

            data = generate_monitoring_data(frame)
            alerts = generate_alerts(data)

            spectrum_history.append(data["spectrum"])

            dashboard, waterfall, alert_panel = create_dashboard(
                data,
                alerts,
                list(spectrum_history)
            )

            elapsed = time.perf_counter() - fps_start

            if elapsed >= 1:
                current_fps = fps_frames / elapsed
                fps_frames = 0
                fps_start = time.perf_counter()

            performance_panel = Panel(
                f"[bold green]{current_fps:.1f} updates/sec[/bold green] "
                f"| Frame: {frame}",
                title="PERFORMANCE MONITOR"
            )

            live.update(
                Group(
                    performance_panel,
                    dashboard,
                    waterfall,
                    alert_panel
                ),
                refresh=True
            )

            processing_time = time.perf_counter() - loop_start
            remaining = (1 / 30) - processing_time

            if remaining > 0:
                time.sleep(remaining)


if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        print("\nAETHERHOUND monitoring stopped.")
