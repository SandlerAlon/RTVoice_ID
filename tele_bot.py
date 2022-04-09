import telebot
from telebot import types

from producer_crypto_rate import CryptoApiRate

telebot_token = '5265934962:AAH88FrYy8pbBjQa9qitN1PgvRQWgAWN4to'
bot = telebot.TeleBot(telebot_token)

# test_chat1 = 1149508890
# test_chat2 = 1652471822
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
		'To get all our suggestion type /listen. \n' +
		'To get suggestion of Influencer type /from InfluencerName  (put his name instead of InfluencerName). ')

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

car = CryptoApiRate()
bot.polling(none_stop=True)




