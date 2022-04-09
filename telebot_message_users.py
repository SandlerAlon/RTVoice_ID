import requests


class TelebotSender:
    def __init__(self):
        self.telebot_token = '5265934962:AAH88FrYy8pbBjQa9qitN1PgvRQWgAWN4to'

    def telegram_bot_sendtext(self, bot_message):
        bot_chat_id = '1652471822'  # liya             # '1149508890' # test id Lev
        send_text = 'https://api.telegram.org/bot' + self.telebot_token \
                    + '/sendMessage?chat_id=' + bot_chat_id \
                    + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        # TODO send telebot message to several chat ids
        # TODO handle telebot send message status
        return response.json()
