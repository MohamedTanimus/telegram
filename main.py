import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=["start"])
def start(message):
	name_name = message.chat.first_name
	las_name = message.chat.last_name
	bot.send_message(message.chat.id, text=f"<strong>Hello [ {name_name} {las_name} ]\nBot Creat Account Picsart\nPlease Enter /Creat </strong>",parse_mode="html")
@bot.message_handler(commands=["Creat"])
def Creat(message):
	ps = "@QwEr#YuIo@PaSdFgHjMlZxCvBnMkL#zX@CvBn#MNBvCx@XdZsXa1Sd5Gh3Hj1Jk0Lp9Iu7Yt6Re4Ew3W2q91928802129ejnsks9w9Knawisiw"
	ema = "1234567890qwertyuiopassdghhkjlmnbvccxz"
	dom = ["yahoo.com","gmail.com","hotmail.com","outlook.com","aol.com"]
	pwd = ''.join(random.choice(ps) for i in range(16))
	email0 = ''.join(random.choice(ema) for i in range(8))
	domain = ''.join(random.choice(dom) for i in range(1))
	email = email0+"@"+domain
	password = pwd
	url = "https://picsart.com/sign-up"
	data={
    "email": email,
    "password": password,
    "isLocal": "false"
}
	r = requests.post(url,data=data)
	try:
		name = r.json()["username"]
		key = r.json()["key"]
		iq = r.json()["response"]
		id = iq["id"]
		created = iq["created"]
		photo = iq["photo"]
		bot.send_photo(message.chat.id,f"{photo}",caption=f"<strong>•email: {email}\n•×××××××××××××××××\n•user: {name}\n•×××××××××××××××××\n•pas: {password}\n•×××××××××××××××××\n•id: {id}\n•×××××××××××××××××\n•key: {key}</strong>",parse_mode="html")
	except:
		bot.send_message(message.chat.id, text=f"<strong>Error [ {name_name} {las_name} ]\nPlease Try Agin /Creat </strong>",parse_mode="html")
		

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
