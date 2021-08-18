import time

from sending import bot

tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x))  # Конвертация даты в читабельный вид


@bot.message_handler(commands=['issue'])
def get_text_messages(message):
    print(tconv(message.date))  # Вывод даты типо 20:58:30 05.07.2020\


bot.polling()
