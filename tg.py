# coding: utf8
'''
Telegram bot && imports
'''

import telebot

TG_BOT_TOKEN = '656974486:AAFhijLPV10bnge-n8buRhRxKsfpaDYP43I'

bot = telebot.TeleBot(TG_BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)


bot.polling()
