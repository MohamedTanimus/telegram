import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request
from bs4 import BeautifulSoup

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def start(message):
	name = message.chat.first_name
	las_name = message.chat.last_name
	bot.send_message(message.chat.id, text=f"<strong>Hello [ {name} {las_name} ]\nBot Download +18 Video\nPlease Send Link Downlaoder </strong>",parse_mode="html")
@bot.message_handler(func=lambda m: True)
def get_text(message):
	msg_text = message.text

	r = requests.get(msg_text)
	soup = BeautifulSoup(r.content, "html.parser")
	siup = soup.find("div",{'style':'font-weight: bold; padding: 3px; border: 1px #000 solid; background: #CCC;'})
	ssd = siup.find("a")["href"]
	bot.send_video(message.chat.id,f"{ssd}",caption="<strong>Done Downlaod Video....</strong>",parse_mode="html")
		

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://telebotwane.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
