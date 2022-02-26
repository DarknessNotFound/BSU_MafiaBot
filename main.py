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
    
@bot.command(name='join', help='User joins game queue if nothing else is specified. If another name is stated,attempts to add that player. Searches by "begins with"')
async def join(ctx, *args):
    if args == ():
        await ctx.send(game.add_player(ctx.author.name))
    else:
        found = await ctx.guild.query_members(list_to_str(args))
        if len(found) == 0:
            await ctx.send("Player not found")
        for i in found:
            await ctx.send(game.add_player(i.name))
    
@bot.command(name='remove', help='User (or specified if -join is followed by anything) leaves game queue.')
async def remove(ctx, *args):
    if args == ():
        await ctx.send(game.remove_player(ctx.author.name))
    else:
        await ctx.send(game.remove_player(list_to_str(args)))
        
@bot.command(name='members', help='Lists all members')
async def members(ctx):
    for member in ctx.guild.members:
        await ctx.send(member.name)
        
@bot.command(name='queue', help='Lists all players in game')
async def queue(ctx):
    await ctx.send(game.list_queue())
    
@bot.command(name='select', help='Adds new role to the game role selection')
async def select(ctx, *args):
    await ctx.send(game.add_role(list_to_str(args)))
    
@bot.command(name='selection', help='Adds new role to the game role selection')
async def selection(ctx):
    await ctx.send(game.list_roles())

@bot.command(name='deselect', help='Adds new role to the game role selection')
async def deselect(ctx, *args):
    await ctx.send(game.remove_role(list_to_str(args)))
    
@bot.command(name='preset', help='Allows for quick selection of roles. If nothing else is specified, lists all presets. Otherwise, deletes the current selection and adds the preset roles')
async def preset(ctx, *args):
    if args == ():
        await ctx.send(game.all_presets())
    else:
        await ctx.send(game.assign_preset(list_to_str(args)))
        
@bot.command(name='all_join', help='All server members except the bot join')
async def all_join(ctx):
    for member in ctx.guild.members:
        if member.name != "MafiaBot":
            await ctx.send(game.add_player(member.name))
    
@bot.command(name='start', help='Fills remaing roles as Villager and starts game')
async def start(ctx):
    await ctx.send(game.fill())
    if game.good_to_go():
        await ctx.send("Game started!!!")
    else:
        await ctx.send("Start aborted (like you should have been). More roles than players. Review and try again.")
bot.run(TOKEN)
