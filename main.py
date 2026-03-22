import psutil
from datetime import datetime

def check_system():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n[{timestamp}]")
    print(f"CPU: {cpu}%")
    print(f"Memory: {memory}%")
    print(f"Disk: {disk}%")

if __name__ == "__main__":
    check_system()
