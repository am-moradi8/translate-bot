import telebot
import os
from googletrans import Translator

API_TOKEN = os.environ.get('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)
translate = Translator()

@bot.message_handler(commands=['start'])
def start_Bot(message):
    bot.reply_to(message , 'سلام\nبه ربات مترجم خوش آمدید\nبرای استفاده و آگاهی از کلید های زیر استفاده کنید\n/help \n/help_translate')

@bot.message_handler(commands=['help'])
def help_Bot(message):
    bot.reply_to(message , 'برای استفاده از ربات و ترجمه های متن خود اول متن را بارگزاری میکنید و جلوی آن پسوند ترجمه مورد نظر را قرار میدهید ,مانند\nامروز هوا خوب است en')
    bot.reply_to(message , 'برای آگاهی زبان های  قابل استفاده کلید /help_translate را بزنید')
@bot.message_handler(commands=['help_translate'])
def help2_bot(message):
    bot.reply_to(message, '<img src=https://media.geeksforgeeks.org/wp-content/uploads/20200430163105/google-trans-python.png')
    bot.reply_to(message , 'ربات برای شما آماده کار است\nلطفا عبارت مد نظر خود را ارسال کنید تا در کمترین زمان برای شما ترجمه شود:')
@bot.message_handler(func=lambda message:True)
def translate_command(message):
    text = message.text
    language = text.split()[-1]
    translate = Translator()
    translated_text= translate.translate(text , dest=language).text
    bot.reply_to(message, translated_text)

bot.infinity_polling()