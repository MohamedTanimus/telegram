import requests,user_agent,json,flask,telebot,random,os,sys
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)
@bot.message_handler(commands=['start'])
def run(message):
	key = types.InlineKeyboardMarkup()
	b2=types.InlineKeyboardButton(text='CHANEEL', url='https://t.me/Freeintrnn')
	key.row_width = 1
	key.add(b2)
	bot.send_message(message.chat.id,text='Hello',parse_mode='html',reply_markup=key)


@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200
if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://appitele.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
