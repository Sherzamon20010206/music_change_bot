
from telegram import Update

from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler, MessageHandler, Filters
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
import  requests

button=ReplyKeyboardMarkup([["Qayta ishga tushirish"]], resize_keyboard=True)



updater = Updater("5174045449:AAFdlW1pGHVZk-kMWc7TIHbCVp8oqWNPs1k")


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		f"""Assalomu aleykum  {update.effective_user.last_name}\n\n sizning id {update.effective_user.id}"""
		,reply_markup=button
	)
	return 'bot'
def voice(update: Update, context: CallbackContext):
	id = update.effective_user.id
	context.bot.send_voice(chat_id=-1001692468825,voice=update.message.voice,caption="""\nπ΄π@music_online_2022π―\nlink -> https://t.me/music_online_2022""")
	return  'bot'
def music(update: Update, context: CallbackContext):
	id = update.effective_user.id
	context.bot.send_audio(chat_id=-1001692468825,audio=update.message.audio,caption="""π΄π@music_online_2022π―\n
π  β β β β β β β β

  βγ€γ€βγ€ββγ€β·γ€γ€β»
\nπ΄yuqori sifatdaπ―π\nlink -> https://t.me/music_online_2022""")
	return  'bot'


def video(update: Update, context: CallbackContext):
	context.bot.send_video(chat_id=-1001692468825, video=update.message.video,caption="""
	π΄π@music_online_2022 π₯
β’ββββ’β’ β¦ππ πβ¦β’β’ββββ’ 
π€  πππ πππππ πππππ ππππππ€
β’ββββ’β’ β¦ππ πβ¦β’β’ββββ’ 
 βπππππππππ ππππππππβ
β’ββββ’β’ β¦ππ πβ¦β’β’ββββ’
       link->https://t.me/music_online_2022
β’ββββ’β’ β¦ππ πβ¦β’β’ββββ’""")
	return  'bot'



def other(update: Update, context: CallbackContext):
	context.bot.send_message(chat_id=-1001692468825,text="""
	π΄π@music_online_2022 π₯
β’ββββ’β’ β¦ππ πβ¦β’β’ββββ’ 
π€ 
π  β β β β β β β β

  βγ€γ€βγ€ββγ€β·γ€γ€β»
π€
β’ββββ’β’ β¦ππ πβ¦β’β’ββββ’ 
 βπππππππππ ππππππππβ
β’ββββ’β’ β¦ππ πβ¦β’β’ββββ’
       link->https://t.me/music_online_2022
β’ββββ’β’ β¦ππ πβ¦β’β’ββββ’""")

	return 'bot'
conv_handler = ConversationHandler(
	entry_points=[
		CommandHandler('start', start),
		# CommandHandler('bot', login),
		MessageHandler(Filters.regex('^(' + 'Qayta ishga tushirish' + ')$'), start),
		CommandHandler('chiqish' , start)],
	states={
		'bot': [
			MessageHandler(Filters.regex('^(' + 'Qayta ishga tushirish' + ')$'), start),
			MessageHandler(Filters.regex('^(' + 'start' + ')$'), start),

			# MessageHandler(Filters.regex('^(' + '/start' + ')$'), start),
			# MessageHandler(Filters.regex('^(' + 'chiqish' + ')$'), start),

			MessageHandler(Filters.audio,music),
			MessageHandler(Filters.voice,voice),
			MessageHandler(Filters.video,video),


		],

	    },


	fallbacks=[
		MessageHandler(Filters.text,other),
		CommandHandler('start' , start),
		# CommandHandler('chiqish' , start),

	]
)
updater.dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()