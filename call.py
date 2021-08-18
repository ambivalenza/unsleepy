import time
from datetime import timedelta

from urllib3 import HTTPSConnectionPool

from sending import bot, comfort_date, get_dates_to_show, CHAT_ID, date_to_str


# tconv = lambda x: time.strftime("%H:%M:%S.%f %d.%m.%Y", time.localtime(x))  # Конвертация даты в читабельный вид

ACTIVITIES = [timedelta(hours=3, minutes=30), timedelta(hours=3, minutes=50), timedelta(hours=4, minutes=0)]
SLEEP = [timedelta(hours=1, minutes=30), timedelta(hours=1, minutes=10)]


def tconv(x):
    return time.strftime("%H:%M:%S %d-%m-%Y", time.localtime(x))


@bot.message_handler(commands='get')
def get(message):
    with open(f"{comfort_date.strftime('%d-%m-%Y')}.txt", "rb") as file:
        dates = list(get_dates_to_show(file.read().decode()))
    dates_str = [date_to_str(dt) for dt in dates]
    schedule = ''
    start_dt = dates[-1]
    for i, t in enumerate(ACTIVITIES):
        end_dt = start_dt + t
        schedule += f'\n{start_dt.strftime("%H:%M")} - {end_dt.strftime("%H:%M")}\n'
        if i < len(SLEEP):
            start_dt = end_dt + SLEEP[i]
    text = '<b>' + str(comfort_date.strftime('%d/%m/%Y')) + '</b>\n---------\n' + '\n'.join(dates_str) + schedule
    print(text)
    bot.send_message(text=text, parse_mode='HTML', chat_id=CHAT_ID)


@bot.message_handler(commands=['issue'])
def get_text_messages(message):
    with open(comfort_date.strftime('%d-%m-%Y') + '.txt', 'a') as file:
        file.write(str(tconv(message.date)) + '\n')
    bot.send_message(text='сохранено!', chat_id=CHAT_ID)
    print(tconv(message.date))


bot.polling()
# {comfort_date.strftime('%d-%m-%Y')}
# try:
# bot.polling()
# except HTTPSConnectionPool:
# bot.polling()
