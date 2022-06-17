from pyrogram import Client
from pyrogram import filters
from pyrogram import types
import sqlite3
import time
import random
import asyncio
app = Client('my_accounts')

my_id = 2116984782

@app.on_message()
async def payments (client,message):
    try:
        if message.chat.id == message.from_user.id or int(message.from_user.id == my_id):
            if message.text[0:5] == 'vip @':
                await app.send_message(chat_id= message.chat.id, text = f"""<b>Фильмы 2022 скрыты от посторонних глаз. И доступны на приватном канале по ссылке ниже. Заходи и следуй инструкции
            
<a href = 'https://t.me/PremTokBot?start={message.text[5:]}'>🍿НАЧАТЬ СМОТРЕТЬ🍿</a></b>""",disable_web_page_preview=True,parse_mode='html')
            if message.text[0:5] == 'pro @':
                await app.send_message(chat_id= message.chat.id, text=f"""<b>Фильмы 2022 скрыты от посторонних глаз. И доступны на приватном канале по ссылке ниже. Заходи и следуй инструкции

<a href = 'https://t.me/MoviePro2022Bot?start={message.text[5:]}'>🍿НАЧАТЬ СМОТРЕТЬ🍿</a></b>""",disable_web_page_preview=True,parse_mode = 'html')


    except:
        pass

app.run()