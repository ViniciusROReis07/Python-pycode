import psutil

battery = psutil.sensors_battery()

percent = float(str(battery.percent))

print(f"No momento voce tem {percent:.0f}% de bateria!")
