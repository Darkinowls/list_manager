import re

from bot_methods.general import list_bot, filters
from telegram_bot import SCROLL_EMOJI


# TODO: validation if it is our group

def define_header_methods():

    @list_bot.on_message(filters.command("head", "/", True) & filters.reply)
    def edit_header(client, message):
        if (message["reply_to_message"]["from_user"]["username"] != "abobus_servitor_bot" or
                SCROLL_EMOJI not in message["reply_to_message"]["text"]):
            return

        order_list = message["reply_to_message"]["text"]
        new_header = SCROLL_EMOJI + ' ' + message["text"][6:] + '\n'

        new_order_list = re.sub("^" + SCROLL_EMOJI + "\s?.{0,100}((\n)|($))", new_header, order_list)

        list_bot.edit_message_text(chat_id=message["chat"]["id"],
                                   message_id=message["reply_to_message"]["message_id"],
                                   text=new_order_list)

    @list_bot.on_message(filters.command("head", "/", True) & filters.reply)
    def edit_header(client, message):
        if (message["reply_to_message"]["from_user"]["username"] != "abobus_servitor_bot" or
                SCROLL_EMOJI not in message["reply_to_message"]["text"]):
            return

        order_list = message["reply_to_message"]["text"]
        new_header = SCROLL_EMOJI + ' ' + message["text"][6:] + '\n'

        new_order_list = re.sub("^" + SCROLL_EMOJI + "\s?.{0,100}((\n)|($))", new_header, order_list)

        list_bot.edit_message_text(chat_id=message["chat"]["id"],
                                   message_id=message["reply_to_message"]["message_id"],
                                   text=new_order_list)

    @list_bot.on_message(filters.command("list", "/", True))
    def make_header(client, message):
        # TODO: validate the command
        header = message["text"]
        header = header.replace('/list', SCROLL_EMOJI + ' ')
        list_bot.send_message(chat_id=message["chat"]["id"], text=header)

 
