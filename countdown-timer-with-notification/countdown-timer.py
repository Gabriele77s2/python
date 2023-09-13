import time
from plyer import notification

seconds = int(input("Enter the number of seconds: "))

while seconds > 0:
    print(f"Time remaining: {seconds} seconds")
    time.sleep(1)
    seconds -= 1

notification_title = "Timer Alert"
notification_text = "Time's up!"
notification.notify(title=notification_title, message=notification_text, app_name="Timer App")
