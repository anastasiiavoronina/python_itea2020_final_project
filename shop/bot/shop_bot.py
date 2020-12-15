import json

from mongoengine import NotUniqueError
from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, Message

from ..models.shop_models import Category, Product, User
from ..models.extra_models import News
from .config import TOKEN
from . import constants
from .utils import inline_kb_from_iterable

bot = TeleBot(TOKEN)

update_status_for_users = {}

@bot.message_handler(commands=['start'])
def handle_start(message):
    update_status_for_users[message.chat.id] = None
    print(message)
    try:
        User.objects.create(
                            telegram_id=message.chat.id,
                            username=getattr(message.from_user, 'username', None),
                            first_name=getattr(message.from_user, 'first_name', None)
                            )
    except NotUniqueError:
        greetings = 'Nice to see you back in our shop'
    else:
        name = f', {message.from_user.first_name}' if getattr(message.from_user, 'first_name') else ''
        greetings = constants.GREETINGS.format(name)

    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [KeyboardButton(n) for n in constants.START_KB.values()]
    kb.add(*buttons)
    bot.send_message(message.chat.id, greetings, reply_markup=kb)


@bot.message_handler(func=lambda m: constants.START_KB[constants.CATEGORIES] == m.text)
def handle_categories(message):
    update_status_for_users[message.chat.id] = None
    root_categories = Category.get_root_categories()
    kb = inline_kb_from_iterable(constants.CATEGORY_TAG, root_categories)
    bot.send_message(message.chat.id, 'Please choose category', reply_markup=kb)


@bot.message_handler(func=lambda m: constants.START_KB[constants.NEWS] == m.text)
def handle_categories(message: Message):
    update_status_for_users[message.chat.id] = None
    news = News.get_latest()
    for n in news:
        bot.send_message(message.chat.id, f'{n.title}: {n.body}')


@bot.callback_query_handler(lambda c: json.loads(c.data)['tag'] == constants.CATEGORY_TAG)
def handle_category_click(call):
    update_status_for_users[call.message.chat.id] = None
    category = Category.objects.get(id=json.loads(call.data)['id'])
    if category.subcategories:
        kb = inline_kb_from_iterable(constants.CATEGORY_TAG, category.subcategories)
        bot.edit_message_text(category.title, call.message.chat.id, message_id=call.message.id, reply_markup=kb)
        #bot.send_message(call.message.chat.id, category.title, reply_markup=kb)
    else:
        products = category.get_products()
        for p in products:
            if p.image:
                description = p.description if p.description else ''
                bot.send_photo(call.message.chat.id,
                               p.image.read(),
                               #caption=f'{p.title}\n{description}'
                               caption=p.formatted_data()
                              )
            else:
                bot.send_message(call.message.chat.id, p.formatted_data())

    #products = Product.objects(category=category)
    # for p in products:
    #     bot.send_message(call.message.chat.id, f'Title: {p.title}. Description{p.description}. '\
    #                                            f'In stock: {str(p.in_stock)}. '\
    #                                            f'Discount: {str(p.discount)}. Price: {str(p.price)}')


@bot.message_handler(func=lambda m: constants.START_KB[constants.SETTINGS] == m.text)
def handle_settings(message: Message):
    update_status_for_users[message.chat.id] = None
    user = User.objects.get(telegram_id=message.chat.id)
    data = user.formatted_data()

    buttons = []
    for k,v in constants.SETTINGS_UPDATE.items():
        json_data = json.dumps({'id': k,
                                'tag': constants.MODIFY_SETTINGS_TAG
                                })
        buttons.append(InlineKeyboardButton(text=k, callback_data=json_data))

    kb = InlineKeyboardMarkup()
    kb.add(*buttons)

    bot.send_message(user.telegram_id, data, reply_markup=kb)

@bot.callback_query_handler(lambda c: json.loads(c.data)['tag'] == constants.MODIFY_SETTINGS_TAG)
def handle_category_click(call):
    update_status_for_users[call.message.chat.id] = json.loads(call.data)['id']
    bot.send_message(call.message.chat.id, constants.SETTINGS_UPDATE[json.loads(call.data)['id']])

@bot.message_handler(content_types=['text'])
def handle_settings(message: Message):
    if update_status_for_users[message.chat.id] == constants.MODIFY_ADDRESS:
        user = User.objects.get(telegram_id=message.chat.id)
        user.update(address=message.text)
        update_status_for_users[message.chat.id] = None
        bot.send_message(message.chat.id, 'Modification was completed')
    elif update_status_for_users[message.chat.id] == constants.MODIFY_NAME:
        user = User.objects.get(telegram_id=message.chat.id)
        user.update(first_name=message.text)
        update_status_for_users[message.chat.id] = None
        bot.send_message(message.chat.id, 'Modification was completed')
    elif update_status_for_users[message.chat.id] == constants.MODIFY_PHONE:
        user = User.objects.get(telegram_id=message.chat.id)
        user.update(phone_number=message.text)
        update_status_for_users[message.chat.id] = None
        bot.send_message(message.chat.id, 'Modification was completed')
    elif update_status_for_users[message.chat.id] == constants.MODIFY_EMAIL:
        user = User.objects.get(telegram_id=message.chat.id)
        user.update(email=message.text)
        update_status_for_users[message.chat.id] = None
        bot.send_message(message.chat.id, 'Modification was completed')