import os
import asyncio
import discord
# Needed for lists of members
intents = discord.Intents.default()
intents.members = True

from dotenv import load_dotenv
import random

from discord.ext import commands

from funcs import *

from Game_Module import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='-', intents=intents)


# Prints a message to say it connected successfully
# NOTE: Sometimes takes a second to trigger and send msg
@bot.event
async def on_ready():
    print("Connected successfully!")
    
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
   
@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

        
bot.run(TOKEN)
