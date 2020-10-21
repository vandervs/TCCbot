import telebot
import time

TOKEN = '1369437112:AAGuouyJJd3tTyTCi4dBm43eIWvUcUnfoXM'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Welcome")


@bot.message_handler(commands=['help'])
def Send_help(message):
	bot.reply_to(message, "To use this bot, say something")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	# bot.reply_to(message, message.text)
	bot.send_message(message.chat.id, message.text)
	
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(e)
		time.sleep(15)