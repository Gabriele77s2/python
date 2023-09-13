import time
import winsound

alarm_time = input("Enter alarm time (HH:MM): ")
current_time = time.strftime("%H:%M")

while current_time != alarm_time:
    current_time = time.strftime("%H:%M")
    time.sleep(1)

print("Time's up!")
frequency = 2500
duration = 1000
winsound.Beep(frequency, duration)