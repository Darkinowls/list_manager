import re

from pyrogram import filters

from telegram_bot import list_bot, SCROLL_EMOJI


def define_list_methods():
    @list_bot.on_message(filters.reply)
    def add_to_list(client, message):
        if (message["reply_to_message"]["from_user"]["username"] != "abobus_servitor_bot" or
                SCROLL_EMOJI not in message["reply_to_message"]["text"]):
            return

        match = re.search('^((\d{1,3}\.)|(\d{1,3}))(\s?[a-zA-z]{3,50}\s?\w{0,50}$)', message["text"])

        if not match:
            return

        if match.group(3):
            message["text"] = match.group(3) + '.' + match.group(4)

        record_list = message["reply_to_message"]["text"].split('\n')

        if len(record_list) == 1:
            return list_bot.edit_message_text(chat_id=message["chat"]["id"],
                                              message_id=message["reply_to_message"]["message_id"],
                                              text=message["reply_to_message"]["text"] + '\n' + message["text"])

        dict_list = dict()
        indexes = []
        record_list.append(message["text"])
        for record in record_list[1:]:
            index = int(re.search('^\d{1,3}', record).group())
            if index in indexes:
                return
            indexes.append(index)
            dict_list[indexes[-1]] = record

        indexes = sorted(indexes)

        new_list = record_list[0] + '\n'
        for i in indexes:
            new_list += dict_list[i] + '\n'

        list_bot.edit_message_text(chat_id=message["chat"]["id"],
                                   message_id=message["reply_to_message"]["message_id"],
                                   text=new_list)
