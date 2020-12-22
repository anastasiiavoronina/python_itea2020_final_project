from shop.bot.sending_news import Sender
from shop.models.shop_models import User
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True)
discount = KeyboardButton(text='We have new button')
kb.add(discount)

s = Sender(User.objects(), text='News', reply_markup=kb)
s.send_message()