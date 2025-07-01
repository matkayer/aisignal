import os
import telebot
from flask import Flask, request

TOKEN = os.getenv("7727955265:AAEYqJtMj-J_6lcdDwGe1HrCQ0Rl_ewSHcY")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot is running!'

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if name == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=os.getenv("WEBHOOK_URL") + "/" + TOKEN)
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
