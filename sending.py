import telebot
from main import get_dates
import datetime
import os

TOKEN = '1971830852:AAFcBsCGYQC1NIVsER1sjnvLV5AnWN7OHxU'

bot = telebot.TeleBot(TOKEN)


CHAT_ID = os.environ.get("CHAT_ID", '-1001300589546')
real_date, comfort_date, readable_date = get_dates()

def hm_show(hours, minutes):
    return ":".join([('0' if hours < 10 else '') + str(hours), ('0' if minutes < 10 else '') + str(minutes)])


def date_to_str(dt):
    minute = int(5 * round(dt.minute / 5))
    hours = dt.hour
    if minute == 60:
        hours += 1
        minute = 0
    if hours == 24:
        hours = 0
    return hm_show(hours, minute)


def myround(x, base=5):
    print(int(base * round(float(x) / base)))


def get_dates_to_show(data_str):
    prev_date = None
    for date_str in data_str.split("\r\n"):
        if not date_str:
            return
        date = datetime.datetime.strptime(date_str, "%H:%M:%S %d-%m-%Y")
        if prev_date and date - prev_date < datetime.timedelta(minutes=5):
            continue

        yield date
        prev_date = date


def send():
    with open(f"{comfort_date.strftime('%d-%m-%Y')}.txt", "rb") as file:
        dates_str = [date_to_str(dt) for dt in get_dates_to_show(file.read().decode())]
        bot.send_message(chat_id=CHAT_ID,
                         text='<b>' + str(comfort_date.strftime('%d/%m/%Y')) + '</b>\n---------\n' + '\n'.join(dates_str),
                         parse_mode='HTML')


if __name__ == '__main__':
    send()
