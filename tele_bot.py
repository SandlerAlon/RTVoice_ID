import telebot
from telebot import types

from crypto_api_rate import CryptoApiRate

telebot_token = '5265934962:AAH88FrYy8pbBjQa9qitN1PgvRQWgAWN4to'
bot = telebot.TeleBot(telebot_token)


@bot.message_handler(commands=['start'])
def start_command(message):
	bot.send_message(
		message.chat.id,
		'Greetings to NayaCryptoTweets.\n' +
		'To get help press /help.')


@bot.message_handler(commands=['help'])
def start_command(message):
	bot.send_message(
		message.chat.id,
		'To get Exchange Rate of crypto type /rate .\n' +
		'To get all our suggestion type /listen. \n' +
		'To get suggestion of Influencer type /from @Influencer  (put his name instead of @Influencer). ')


@bot.message_handler(commands=['rate'])
def crypto_rate(message):
	crypto = message.text[6:]
	rate = car.retrieve_crypto_rate(crypto)
	bot.reply_to(message, str(rate))

@bot.message_handler(commands=['listen'])
def reg_to_suggestions(message):
	chat_id = message.chat.id
	# TODO register to suggestions with @chat_id
	bot.send_message(message.chat.id, 'Registered')


@bot.message_handler(commands=['from'])
def reg_to_influencer(message):
	influencer = message.text[6:]
	chat_id = message.chat.id
	#TODO register to @influencer with @chat_id
	bot.send_message(message.chat.id, 'Registered')

#TODO send to chat.id messages

car = CryptoApiRate()
bot.polling(none_stop=True)


