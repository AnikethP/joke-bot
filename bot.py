import discord
import random
import requests
import json
import time

TOKEN = 'OTM4NTg3OTU3NzkzODAwMzAz.YfseJw.ZyXyC7XkGpiJBshvdPktrgqN7eo'

client = discord.Client()
channel = None

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    global channel
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = message.channel

    if message.author == client.user:
        return
    
    if user_message == "#funny":
        await getJoke()
        

async def getJoke():
    with open('stupidstuff.json') as json_file:
        data = json.load(json_file)
    
        # Print the type of data variable
        num =  random.randrange(0, len(data))
        #for server logging purposes
        print(f"Sent message: {data[num]['body']}")
        await send_message(data[num]['body'])

   
    
    # for word in s:
    #     await send_message(word)
    #     time.sleep(1)

async def send_message(message):
    await channel.send(message)

client.run(TOKEN)
