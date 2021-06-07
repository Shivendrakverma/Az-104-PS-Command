
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging


def main():

    t_token = 'token'
    updater = Updater(token=t_token, use_context=True)
    dis_p = updater.dispatcher
    #logging.basicConfig(format='%(asctime)s -%(name) -%(levelname)s - %(message)s', level=logging.INFO)
    start_handler = CommandHandler('start', start)
    hi_handler = CommandHandler('hi', hi)
    dis_p.add_handler(start_handler)
    dis_p.add_handler(hi_handler)
    updater.start_polling()
    updater.idle()


def start(update, context):

    chat_id = update.message.chat_id
    user_name = update.message.from_user.username

    welcome_msg = "Hi @{}\nI am your Bot, How may I help you?".format(user_name)
    context.bot.send_message(chat_id=chat_id, text=welcome_msg)


def hi(update, context):
    chat_id = update.message.chat_id
    user_name = update.message.from_user.username
    hi_msg = "Hello @{}\n How may I assist you?".format(user_name)
    context.bot.send_message(chat_id=chat_id, text=hi_msg)


if __name__ == '__main__':
    main()
