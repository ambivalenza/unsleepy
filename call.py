import time
from datetime import timedelta

from urllib3 import HTTPSConnectionPool

from sending import bot, comfort_date, get_dates_to_show, CHAT_ID, date_to_str, hm_show

ACTIVITIES = [timedelta(hours=3, minutes=40), timedelta(hours=4), timedelta(hours=4)]
SLEEP = [timedelta(hours=1, minutes=20), timedelta(hours=1)]


def tconv(x):
    return time.strftime("%H:%M:%S %d-%m-%Y", time.localtime(x))


@bot.message_handler(commands='get')
def get(message):
    with open(f"{comfort_date.strftime('%d-%m-%Y')}.txt", "rb") as file:
        dates = list(get_dates_to_show(file.read().decode()))

    schedule = ''
    start_dt = dates[-1]
    header_len = 0
    for i, t in enumerate(ACTIVITIES):
        end_dt = start_dt + t
        schedule += f'{date_to_str(start_dt)} - {date_to_str(end_dt)} ({hm_show(t.seconds // 3600, (t.seconds // 60) % 60)})\n'
        if i == 0:
            header_len = len(schedule)
        if i < len(SLEEP):
            start_dt = end_dt + SLEEP[i]

    dates_str = "\n".join(date_to_str(dt) for dt in dates)
    text = f'<pre><b>{comfort_date.strftime("%d/%m/%Y")}</b>\n{"-" * header_len}\n{dates_str}\n\n{schedule}</pre>'
    bot.send_message(text=text, parse_mode='HTML', chat_id=CHAT_ID)


@bot.message_handler(commands=['issue'])
def get_text_messages(message):
    with open(comfort_date.strftime('%d-%m-%Y') + '.txt', 'a') as file:
        file.write(str(tconv(message.date)) + '\n')
    bot.send_message(text='сохранено!', chat_id=CHAT_ID)


bot.polling()
