import os
import time
import unicodedata
import telebot

bot_token = os.environ['BOT_TOKEN']

def normalize_caseless(text):
    return unicodedata.normalize("NFKD", text.casefold())

bot = telebot.TeleBot(os.environ['BOT_TOKEN'])

trigger_words = [
    "Datenkommunikation",
    "Datkom",
    "Datkomm"
]

@bot.message_handler(commands=['loesung', 'hilfe', 'help', 'klausur'])
def send_link(message):
    """
    Sends help!
    """
    bot.reply_to(message, "Eselsbrücke: https://open.spotify.com/track/72FWIzbWGeZ8w0QsiVJTUo")

@bot.message_handler(content_types=["text"])
def send_phrase(message):
    """
    Responds to all messages containing the trigger words above
    """
    text = normalize_caseless(message.text)
    for trigger in trigger_words:
        if normalize_caseless(trigger) in text and normalize_caseless("und Sicherheit") not in text:
            bot.reply_to(message, "und Sicherheit!")

if __name__ == '__main__':
    try:
        bot.polling()
    except Exception:
        exit(1)