import telebot
from main import get_dates

TOKEN = '1971830852:AAFcBsCGYQC1NIVsER1sjnvLV5AnWN7OHxU'

bot = telebot.TeleBot(TOKEN)
CHAT_ID = '556470836'


def send():
    real_date, comfort_date = get_dates()
    print(comfort_date.strftime('%d-%m-%Y'))
    with open(f"{comfort_date.strftime('%d-%m-%Y')}.txt", "rb") as file:
        text = file.read()
        bot.send_message(CHAT_ID, f.decode())


if __name__ == '__main__':
    send()
