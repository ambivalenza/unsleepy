import telebot
from main import get_dates
import datetime

TOKEN = '1971830852:AAFcBsCGYQC1NIVsER1sjnvLV5AnWN7OHxU'

bot = telebot.TeleBot(TOKEN)
CHAT_ID = '-1001300589546'


def date_to_str(dt):
    minute = int(5 * round(dt.minute / 5))
    hours = dt.hour
    if minute == 60:
        hours += 1
        minute = 0
    if hours == 24:
        hours = 0
    result_time = ":".join([str(hours), ('0' if minute < 10 else '') + str(minute)])
    print(result_time)
    return result_time


def myround(x, base=5):
    print(int(base * round(float(x) / base)))


def get_dates_to_show(data_str):
    prev_date = None
    for date_str in data_str.split("\r\n"):
        if not date_str:
            return
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
        if prev_date and date - prev_date < datetime.timedelta(minutes=5):
            continue

        yield date_to_str(date)
        prev_date = date


def send():
    real_date, comfort_date = get_dates()
    with open(f"{comfort_date.strftime('%d-%m-%Y')}.txt", "rb") as file:
        bot.send_message(chat_id=CHAT_ID,
                         text='<b>'+str(comfort_date.strftime('%d/%m/%Y')) + '</b>\n---------\n' + '\n'.join(
                             get_dates_to_show(file.read().decode())),
                         parse_mode='HTML')


if __name__ == '__main__':
    send()
