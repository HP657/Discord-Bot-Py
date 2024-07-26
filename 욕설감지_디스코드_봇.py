import requests
import discord
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
API_KEY = os.getenv('API_KEY')
CHANNEL_ID = int(os.getenv('CHANNEL_ID')) 

intents = discord.Intents.default()
intents.message_content = True  

url = "https://api.matgim.ai/54edkvw2hn/api-keyword-slang"
headers = {
    "Content-Type": "application/json",
    "x-auth-token": API_KEY
}

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} 에 로그인하였습니다.')

@bot.event
async def on_message(message):
    if not message.author.bot:
        payload = {
            "document": message.content
        }
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        print(data)
        if data['success']:
            if data['result']['data']:
                await message.channel.send(f"{data['result']['data'][0]['text']}는 욕설이야 새끼야 ^^")
            else:
                await message.channel.send('욕설 없음')
        else:
            print('요청 오류')

bot.run(TOKEN)
