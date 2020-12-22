from .shop_bot import bot
#from ..models.shop_models import User
from shop.models.shop_models import User
from telebot.apihelper import ApiException
import time
from threading import Thread

class Sender:

    def __init__(self, users, **message_data):
        self._message_data = message_data
        self._users = users

    def send_message(self):
        blocked_ids = []
        users = self._users.filter(is_blocked=False)
        for u in users:
            try:
                bot.send_message(
                    u.telegram_id,
                    **self._message_data
                )
            except ApiException as e:
                print(e)
                if e.error_code == 403:
                    blocked_ids.append(u.telegram_id)
                else:
                    raise e

            time.sleep(0.1)

        User.objects(telegram_id__in=blocked_ids).update(is_blocked=True)


def cron_unlock_users():
    while True:
        User.objects(is_blocked=True).update(is_blocked=False)
        minute = 60
        hour = 60*minute
        day = 24*hour
        time.sleep(2*day)


Thread(target=cron_unlock_users).start()