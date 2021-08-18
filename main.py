import keyboard
from datetime import datetime, timedelta
import time


def get_dates():
    real_date = datetime.now()
    comfort_date = real_date - timedelta(hours=9)
    readable_date = datetime.now().strftime("%H:%M:%S %d-%m-%Y")
    # current_time = datetime.now().time().strftime('%H:%M')
    return real_date, comfort_date, readable_date


def main(key_event):
    _, comfort_date, readable_date = get_dates()
    if key_event.event_type == 'down':
        with open(comfort_date.strftime('%d-%m-%Y') + '.txt', 'a') as file:
            file.write(str(readable_date) + '\n')


if __name__ == '__main__':
    keyboard.hook(main)
    while True:
        time.sleep(10)
