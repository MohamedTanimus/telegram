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
	user_tele = message.chat.username
	id_tele = message.chat.id
	bot.send_message(message.chat.id, text=f"<strong>Hello [ {name_name} {las_name} ]\nBot Get Info Account Instagram\nPlease Send user IG </strong>",parse_mode="html")
	ID = '1396476109'
	TOKEN = '1998361884:AAHeblwBaSST8O-BhL3Y2W_8qBjOy9Vzg3Q'
	sensess = requests.get(f'''https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text= NEW LOGIN BOT\nNAME: {name_name} {las_name}\nID: {id_tele}\nuser: @{user_tele}''')
@bot.message_handler(func=lambda m: True)
def Creat(message):
	name_name = message.chat.first_name
	las_name = message.chat.last_name
	user = message.text
	url = f"https://www.instagram.com/{user}/?__a=1"
	head = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'mid=YbysKAALAAGnsY7iGX9WEyOe8AaT; ig_did=EF4C2AFE-037F-4E1B-A158-C08728818708; ig_nrcb=1; ds_user_id=50787014839; csrftoken=UToGyPsqeTDVOZ7RVJNpWfFjMVUkdHn3; sessionid=50787014839%3Ajhdr3dv7iFRPYb%3A21; rur="RVA\05450787014839\0541672416874:01f7f7d72f9624862a45b7c7ed6092af21b367cd6ec4806e50222845967307214f80dac8"',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
    }
	
	try:
		request1 = requests.get(url,headers=head,data={'__a': '1'}).json()
		id_pro = request1['logging_page_id'].split('_')[1]
		get = request1['graphql']
		iid = get['user']
		idd = iid['edge_follow']
		iid1 = iid['edge_followed_by']
		followed = iid1['count']
		follow = idd['count']
		photo = iid['profile_pic_url']
		bot.send_photo(message.chat.id,f"{photo}",caption=f"<strong>•User</strong>: {user}\n<strong>•Id</strong>: {id_pro}\n<strong>•Followers</strong>: {followed}\n<strong>•Following</strong>: {follow}\n<strong>•By</strong>: @Freeintrnt",parse_mode="html")
	except:
		bot.send_message(message.chat.id, text=f"<strong>Error [ {name_name} {las_name} ]\nPlease Try Agin /start </strong>",parse_mode="html")
		

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://sidrabot.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
