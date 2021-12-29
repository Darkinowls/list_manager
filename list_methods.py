import re
from collections import OrderedDict

from methods import app, filters, SCROLL_EMOJI


# TODO: validation if it is our group

@app.on_message(filters.command("head", "/", True) & filters.reply)
def edit_header(client, message):
    if (message["reply_to_message"]["from_user"]["username"] != "abobus_servitor_bot" or
            SCROLL_EMOJI not in message["reply_to_message"]["text"]):
        return

    order_list = message["reply_to_message"]["text"]
    new_header = SCROLL_EMOJI + ' ' + message["text"][6:] + '\n'

    new_order_list = re.sub("^" + SCROLL_EMOJI + "\s?.{0,100}((\n)|($))", new_header, order_list)

    app.edit_message_text(chat_id=message["chat"]["id"],
                          message_id=message["reply_to_message"]["message_id"],
                          text=new_order_list)


@app.on_message(filters.command("head", "/", True) & filters.reply)
def edit_header(client, message):
    if (message["reply_to_message"]["from_user"]["username"] != "abobus_servitor_bot" or
            SCROLL_EMOJI not in message["reply_to_message"]["text"]):
        return

    order_list = message["reply_to_message"]["text"]
    new_header = SCROLL_EMOJI + ' ' + message["text"][6:] + '\n'

    new_order_list = re.sub("^" + SCROLL_EMOJI + "\s?.{0,100}((\n)|($))", new_header, order_list)

    app.edit_message_text(chat_id=message["chat"]["id"],
                          message_id=message["reply_to_message"]["message_id"],
                          text=new_order_list)


@app.on_message(filters.command("list", "/", True))
def make_header(client, message):
    # TODO: validate the command
    header = message["text"]
    header = header.replace('/list', SCROLL_EMOJI + ' ')
    app.send_message(chat_id=message["chat"]["id"], text=header)


@app.on_message(filters.reply)
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
        return app.edit_message_text(chat_id=message["chat"]["id"],
                                     message_id=message["reply_to_message"]["message_id"],
                                     text=message["reply_to_message"]["text"] + '\n' + message["text"])

    dict_list = dict()
    indexes = []
    record_list.append(message["text"])
    for record in record_list[1:]:
        index = int(re.search('^\d{1,3}', record).group())
        if index in indexes :
            return
        indexes.append(index)
        dict_list[indexes[-1]] = record

    indexes = sorted(indexes)

    new_list = record_list[0] + '\n'
    for i in indexes:
        new_list += dict_list[i] + '\n'

    app.edit_message_text(chat_id=message["chat"]["id"],
                          message_id=message["reply_to_message"]["message_id"],
                          text=new_list)
