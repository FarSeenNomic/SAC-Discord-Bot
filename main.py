"""
This bot is dedicated to the Santa Ana College Computer Science Server, where members are free to send updates.

When complete, it shoud preform this automatically from github.
"""
import discord

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.content == "Hello!":
        await message.channel.send("Hello!")

@client.event
async def on_ready():
    print("ready!")

client.run(open("../Discord/TOKENSelfMod", "r").read().rstrip())
