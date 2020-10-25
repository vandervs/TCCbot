import telebot
import time
import os

TOKEN = '1369437112:AAGuouyJJd3tTyTCi4dBm43eIWvUcUnfoXM'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Welcome")


@bot.message_handler(commands=['help'])
def Send_help(message):
	bot.reply_to(message, "To use this bot, say something or send a pdf for me to process it")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_all(message):
	# bot.reply_to(message, message.text)
	bot.send_message(message.chat.id, message.text)

def is_extension_pdf(file_extension):
	if file_extension == ".pdf":
		return True
	else:
		return False

def process_file(file):
	
	pass

# Handles all sent documents and audio files
@bot.message_handler(content_types=['document'])
def handle_docs_audio(message):	
	file = bot.get_file(message.document.file_id)
	file_name, file_extension = os.path.splitext(file.file_path)
		
	if is_extension_pdf(file_extension):
		bot.reply_to(message, "Pdf received, thank you")
		process_file(file)
	else:
		bot.reply_to(message, "Sorry, we only handle pdf's for now, try again")
	pass
	
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(e)
		time.sleep(15)