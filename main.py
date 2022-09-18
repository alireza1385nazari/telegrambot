from turtle import update
import api as C
import responses as R
from telegram.ext import *

print("bot started...")
def main():
    updater = Updater(C.BOT_API,use_context=1)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("seting",seting))
    dp.add_handler(CommandHandler("help",Help))
    dp.add_handler(MessageHandler(Filters.text,handle_response))
    updater.start_polling()
    updater.idle()
def start(Update, context):
    Update.message.reply_text("ربات اجرا شد")
def Help(Update, context):
    Update.message.reply_text("با ربات حرف بزنید")
def seting(Update, context):
    Update.message.reply_text("این قسمت به زودی فعال میشود")
def handle_response(Update, context):
    text = Update.message.text
    Update.message.reply_text(R.responses(str(text)))
main()