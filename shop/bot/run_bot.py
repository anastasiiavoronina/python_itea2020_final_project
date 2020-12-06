from bot.config import TOKEN
from telebot import TeleBot
from bot.texts import GREETINGS
import random


def run():
    bot = TeleBot(TOKEN)

    @bot.message_handler(commands=['start'])
    def handle_start(message):
        bot.send_message(message.chat.id, random.choice(GREETINGS))

    bot.polling()

if __name__ == '__main__':
    run()