import telebot
from telebot import types

from crypto_api_rate import CryptoApiRate

telebot_token = '5265934962:AAH88FrYy8pbBjQa9qitN1PgvRQWgAWN4to'
bot = telebot.TeleBot(telebot_token)


# echo
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)

@bot.message_handler(commands=['rate'])
def crypto_rate(message):
	crypto = message.text[6:]
	rate = car.retrieve_crypto_rate(crypto)
	bot.reply_to(message, str(rate))


car = CryptoApiRate()
bot.polling(none_stop=True)
