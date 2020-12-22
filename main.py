from shop.bot.shop_bot import bot, app
import time
from shop.bot.config import *


#bot.polling()


bot.remove_webhook()
time.sleep(0.5)
bot.set_webhook(WEBHOOKURL, certificate=open('webhook_cert.pem'))

app.run()