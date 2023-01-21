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
	while True:
		u='https://www.coolgenerator.com/credit-card-generator'
		h={'Host': 'www.coolgenerator.com',
'content-length': '23',
'cache-control': 'max-age=0',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform': '"Android"',
'upgrade-insecure-requests': '1',
'origin': 'https://www.coolgenerator.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': 'Mozilla/5.0 (Linux; Android 9; SM-J610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'referer': 'https://www.coolgenerator.com/credit-card-generator',}
		d='cardbrand=0&quantity=1'
		r=requests.post(u,headers=h,data=d).text
		soup = bs4.BeautifulSoup(r, 'html.parser')
		try:
			iii = soup.find_all("p", {"class": "text-center grey"})
			g=str(iii)
			cv= (g.split('CVV:')[1].split('<')[1].split('>')[1])
			c1=cv[0]
			ccv = (cv.split(c1)[1])
			date = (g.split('Expiry:')[1].split('<')[1].split('>')[1])
			gk = (f'{date.split("/")[0]}|{date.split("/")[1]}|{ccv}')
			i8=soup.find_all("p", {"class": "text-center font-18"})
			g = str(i8)
			cc = (g.split('<span>')[1].split('<')[0])
			c1=cc[0]
			cun= (cc.split(c1)[1])
			list=f"{cun}|{gk}"
			apibinlist = json.loads(requests.get("https://lookup.binlist.net/"+cun).text)
			emoji = apibinlist["country"]["emoji"]
			name = apibinlist["country"]["name"]
			binType = apibinlist["type"]
			bank_name = apibinlist["bank"]["name"]
			bank_phone = apibinlist["bank"]["phone"]
			bank_url = apibinlist["bank"]["url"]
			brand = apibinlist["brand"]
			scheme = apibinlist["scheme"]
			respo= f"""
┏━━━━━━━━━━━━━━
┣ 🍂 𝑪𝑪 𝑺𝑺𝑪𝑹𝑨𝑷𝑷𝑬𝑹 🍂 ┗━━━━━━━━━━━━━━
════════════════════                   ╠𝑪𝑪: {list}
┏━━━━━━━━━━━━━━
┣ 🍁 𝑩𝑰𝑵 𝑫𝑨𝑻𝑨 🍁
┗━━━━━━━━━━━━━━
╠𝑩𝒊𝒏 𝑫𝒆𝒕𝒂𝒊𝒍𝒔:{name} -{emoji} -{bank_name}{binType} -{scheme}
╠𝑩𝒂𝒏𝒌: {brand}
┏━━━━━━━━━━━━━━
┣ 🍁 𝑀𝑌 𝐼𝑁𝐹𝑂 🍁
┗━━━━━━━━━━━━━━
🧑🏻‍💻| 𝑫𝐸𝑉:  @Mosalahxyz 
🥷🏻| 𝑪𝑯:@Freeintrnn """
			bot.send_message(message.chat.id,text=respo,parse_mode='html',reply_markup=key)
		except:pass


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
