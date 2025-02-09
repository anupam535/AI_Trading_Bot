from telegram import Bot, Update
from telegram.ext import CommandHandler, Updater
import pandas as pd

TOKEN = "6198191947:AAHnUnTQU3BDWoG6Qr5vTerqMXhQdvbvQyM"

def start(update, context):
    update.message.reply_text("Welcome! Type /signal to get the latest trade signal.")

def send_signal(update, context):
    df = pd.read_csv("data/nifty_predictions.csv", index_col=0, parse_dates=True)
    last_signal = df.iloc[-1]["Prediction"]
    signal_text = "BUY" if last_signal == 1 else "SELL"
    update.message.reply_text(f"Latest Signal: {signal_text}")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("signal", send_signal))

if __name__ == "__main__":
    updater.start_polling()
    updater.idle()
