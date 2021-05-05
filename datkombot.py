import telebot
import time
import unicodedata

bot_token = '1090151263:AAF1MqT7ai0gn1uwL9DRYiFKYIL1_uZicDA'
bot = telebot.TeleBot(token=bot_token)
cid = 0

def normalize_caseless(text):
    return unicodedata.normalize("NFKD", text.casefold())

@bot.message_handler(content_types=["text"])
def handle(message):
    mid = message.message_id
    cid = message.chat.id
    text = normalize_caseless(message.text)
    if int(text.find(normalize_caseless("Datenkommunikation"))) >= 0 or int(text.find(normalize_caseless("DatKom"))) >= 0 or int(text.find(normalize_caseless("DatKomm"))) >= 0:
        if int(text.find(normalize_caseless("und Sicherheit"))) < 0:
            bot.send_message(cid, "und Sicherheit!", reply_to_message_id=mid)
        else: pass
    else: pass

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
