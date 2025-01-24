import psutil
import platform
import time
from datetime import datetime

def get_system_health():
    health_data = {
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "OS": platform.system(),
        "OS Version": platform.version(),
        "CPU Usage (%)": psutil.cpu_percent(interval=1),
        "Memory Usage (%)": psutil.virtual_memory().percent,
        "Disk Usage (%)": psutil.disk_usage('/').percent,
        "Network Sent (MB)": psutil.net_io_counters().bytes_sent / (1024 * 1024),
        "Network Received (MB)": psutil.net_io_counters().bytes_recv / (1024 * 1024),
        "Uptime (seconds)": time.time() - psutil.boot_time()
    }
    return health_data

def print_health_status():
    health = get_system_health()
    print("\n--- System Health Status ---")
    for key, value in health.items():
        print(f"{key}: {value}")
    print("-----------------------------\n")

if __name__ == "__main__":
    while True:
        print_health_status()
        time.sleep(10)  # Monitor every 10 seconds


