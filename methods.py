from pyrogram import filters
from connection import app
import random

SCROLL_EMOJI = '\U0001F4DC'


# To get json from the message has sent
@app.on_message(filters.command("json", "/", True))
def get_json_from_message(client, message):
    print(message)


# Everyone can say hello to Abobus!
@app.on_message(filters.command("hi", "/", True))
def abobus_hello(client, message):
    app.send_message(chat_id=message["chat"]["id"], text="Abobus welcomes you!")



