from urllib3 import HTTPSConnectionPool

from sending import bot, comfort_date, get_dates_to_show, CHAT_ID


@bot.message_handler(commands='call')
def call(message):
    text = ''
    with open(f"{comfort_date.strftime('%d-%m-%Y')}.txt", "rb") as file:
        text += '<b>' + str(comfort_date.strftime('%d/%m/%Y')) + '</b>\n---------\n' + '\n'.join(
            get_dates_to_show(file.read().decode()))
        bot.send_message(text=text, parse_mode='HTML', chat_id=CHAT_ID)


bot.polling()
# {comfort_date.strftime('%d-%m-%Y')}
# try:
# bot.polling()
# except HTTPSConnectionPool:
# bot.polling()
