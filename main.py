import os

import discord
from dotenv import load_dotenv
import random

from discord.ext import commands

from funcs import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

bot = commands.Bot(command_prefix='-')

#Prints a message to say it connected successfully
#NOTE: Sometimes takes a second to trigger and send msg
@bot.event
async def on_ready():
    print("Connected successfully!")

@bot.command(name='slideIntoDMs', help='Messages the user that typed the msg.')
async def slideIntoDMs(ctx):
    msg = "I just slid into your dms"
    await ctx.message.author.send(msg)

@bot.command(name='echo', help='Echos what the user just said')
async def echo(ctx, *args):
    await ctx.send(list_to_str(args))

bot.run(TOKEN)
