from pyrogram import filters

from telegram_bot import list_bot, BOT_NAME, SLASH, JSON, HI


def define_general_methods():

    # To get json from the message has sent
    @list_bot.on_message(filters.command(JSON, SLASH, True))
    def get_json_from_message(client, message):
        print(message)

    # Everyone can say hello to bot!
    @list_bot.on_message(filters.command(HI, SLASH, True))
    def say_hello(client, message):
        list_bot.send_message(chat_id=message["chat"]["id"], text=f"{BOT_NAME} welcomes you!")
