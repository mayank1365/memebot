import discord
from dotenv import load_dotenv
import os

api_key = os.getenv('API_KEY')
debug = os.getenv('DEBUG')

load_dotenv()

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(api_key) 