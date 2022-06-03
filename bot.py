
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
	context.bot.send_voice(chat_id=-1001692468825,voice=update.message.voice,caption="""\n🔴🔈@music_online_2022💯\nlink -> https://t.me/music_online_2022""")
	return  'bot'
def music(update: Update, context: CallbackContext):
	id = update.effective_user.id
	context.bot.send_audio(chat_id=-1001692468825,audio=update.message.audio,caption="""🔴🔈@music_online_2022💯\n
🔊  ▁ ▂ ▃ ▄ ▅ ▆ ▇ █

  ⇆ㅤㅤ◁ㅤ❚❚ㅤ▷ㅤㅤ↻
\n🔴yuqori sifatda💯🔈\nlink -> https://t.me/music_online_2022""")
	return  'bot'


def video(update: Update, context: CallbackContext):
	context.bot.send_video(chat_id=-1001692468825, video=update.message.video,caption="""
	🔴🔈@music_online_2022 🎥
•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈• 
🖤  𝐁𝐈𝐙 𝐁𝐈𝐋𝐀𝐍 𝐁𝐈𝐑𝐆𝐀 𝐁𝐎𝐋𝐈𝐍🖤
•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈• 
 ☞𝐃𝐎𝐒𝐓𝐋𝐀𝐑𝐆𝐀 𝐔𝐋𝐀𝐒𝐇𝐈𝐍𝐆☜
•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈•
       link->https://t.me/music_online_2022
•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈•""")
	return  'bot'



def other(update: Update, context: CallbackContext):
	context.bot.send_message(chat_id=-1001692468825,text="""
	🔴🔈@music_online_2022 🎥
•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈• 
🖤 
🔊  ▁ ▂ ▃ ▄ ▅ ▆ ▇ █

  ⇆ㅤㅤ◁ㅤ❚❚ㅤ▷ㅤㅤ↻
🖤
•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈• 
 ☞𝐃𝐎𝐒𝐓𝐋𝐀𝐑𝐆𝐀 𝐔𝐋𝐀𝐒𝐇𝐈𝐍𝐆☜
•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈•
       link->https://t.me/music_online_2022
•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈•""")

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