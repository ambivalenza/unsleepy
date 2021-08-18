import time

from urllib3 import HTTPSConnectionPool

from sending import bot, comfort_date, get_dates_to_show, CHAT_ID


# tconv = lambda x: time.strftime("%H:%M:%S.%f %d.%m.%Y", time.localtime(x))  # Конвертация даты в читабельный вид

def tconv(x):
    return time.strftime("%H:%M:%S %d-%m-%Y", time.localtime(x))


@bot.message_handler(commands='call')
def call(message):
    text = ''
    with open(f"{comfort_date.strftime('%d-%m-%Y')}.txt", "rb") as file:
        text += '<b>' + str(comfort_date.strftime('%d/%m/%Y')) + '</b>\n---------\n' + '\n'.join(
            get_dates_to_show(file.read().decode()))
        bot.send_message(text=text, parse_mode='HTML', chat_id=CHAT_ID)


@bot.message_handler(commands=['issue'])
def get_text_messages(message):
    with open(comfort_date.strftime('%d-%m-%Y') + '.txt', 'a') as file:
        file.write(str(tconv(message.date)) + '\n')
    bot.send_message(text='сохранено!', chat_id=CHAT_ID)
    print(tconv(message.date))  # Вывод даты типо 20:58:30 05.07.2020\


bot.polling()
# {comfort_date.strftime('%d-%m-%Y')}
# try:
# bot.polling()
# except HTTPSConnectionPool:
# bot.polling()
