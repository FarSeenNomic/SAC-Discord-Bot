"""
This bot is dedicated to the Santa Ana College Computer Science Server, where members are free to
send updates through github at https://github.com/Imanton1/SAC-Discord-Bot.

When complete, it shoud preform this automatically from github.

https://discord.com/oauth2/authorize?client_id=624446144189300736&scope=bot&permissions=1099511627775
"""
import discord

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    # Stopps the bot from responding to other bots, including itself.
    if message.author.bot:
        return

    if message.content == "Hello!":
        await message.channel.send("Hello!")

@client.event
async def on_ready():
    print(client.user.name, "is ready!")

client.run(open("../Discord/TOKENSelfMod", "r").read().rstrip())
