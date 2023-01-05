
import discord
import os
import random
from dotenv import load_dotenv

load_dotenv('file.env')
client = discord.Client()
TOKEN = os.getenv('TOKEN')

@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
  
    print(f'Message {user_message} by {username} on {channel}')

    #so bot doesn't respond to itself
    if message.author == client.user:
        return

    if channel == "bot-test":
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send("sup")
        elif user_message.lower() == "bye":
            await message.channel.send("cya")

client.run(TOKEN)
