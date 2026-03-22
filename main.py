import psutil
import time

while True:  # This loop runs forever
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")
    print("-" * 20)  # separator

    time.sleep(60)  # wait 60 seconds before checking again
