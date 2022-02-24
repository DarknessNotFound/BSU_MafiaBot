import os

import discord
# Needed for lists of members
intents = discord.Intents.default()
intents.members = True

from dotenv import load_dotenv
import random

from discord.ext import commands

from funcs import *

from Classes import *
game = Game()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='-', intents=intents)

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
    
@bot.command(name='new', help='Creates a new game')
async def new(ctx):
    game.new()
    await ctx.send("New game begun")
    
@bot.command(name='join', help='User joins game queue if nothing else is specified. If another name is stated,attempts to add that player')
async def join(ctx, *args):
    if args == ():
        game.add_player(ctx.author.name)
        await ctx.send(ctx.author.name + " has joined the game.")
    else:
        found = await ctx.guild.query_members(list_to_str(args))
        if len(found) == 0:
            await ctx.send("Player not found")
        for i in found:
            game.add_player(i.name)
            await ctx.send(i.name + " has joined the game.")
    
@bot.command(name='remove', help='User (or specified if -join is followed by anything) leaves game queue.')
async def remove(ctx, *args):
    if args == ():
        if game.remove_player(ctx.author.name):
            await ctx.send(ctx.author.name + " has left the game.")
    else:
        if game.remove_player(list_to_str(args)):
            await ctx.send(list_to_str(args) + " has left the game.")
        else:
            await ctx.send("Player not found")
        
@bot.command(name='members', help='Lists all members')
async def members(ctx):
    for member in ctx.guild.members:
        await ctx.send(member.name)
        
@bot.command(name='queue', help='Lists all players in game')
async def queue(ctx):
    await ctx.send(game.list_all())

bot.run(TOKEN)
