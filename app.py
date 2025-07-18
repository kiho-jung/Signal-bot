
import os
import telegram
from flask import Flask, request

app = Flask(__name__)
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
bot = telegram.Bot(token=TOKEN)

@app.route("/testlong", methods=["GET"])
def testlong():
    bot.send_message(chat_id=CHAT_ID, text="🚀 저점 LONG 신호 발생!")
    return "Long alert sent!"

@app.route("/testshort", methods=["GET"])
def testshort():
    bot.send_message(chat_id=CHAT_ID, text="🔻 고점 SHORT 신호 발생!")
    return "Short alert sent!"

@app.route("/")
def home():
    return "Signal bot is running."
