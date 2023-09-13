import time

def pomodoro_timer(work_minutes, break_minutes):
    print("Work session started.")
    time.sleep(work_minutes * 60)
    print("Time's up! Take a break.")

    print("Break started.")
    time.sleep(break_minutes * 60)
    print("Break's over. Back to work!")

work_time = int(input("Enter work time in minutes: "))
break_time = int(input("Enter break time in minutes: "))

while True:
    pomodoro_timer(work_time, break_time)
    restart = input("Start another Pomodoro session? (yes/no): ")
    if restart.lower() != "yes":
        break
