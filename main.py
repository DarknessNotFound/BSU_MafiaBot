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

bot = commands.Bot(command_prefix='--')

@bot.command(name='echo', help='Echos what the user just said')
async def echo(ctx, *args):
    await ctx.send(list_to_str(args))

bot.run(TOKEN)
