# bot.py
import os

import discord
from dotenv import load_dotenv
import random

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

bot = commands.Bot(command_prefix='--')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name} (id: {guild.id})'
    )

@bot.command(name='99', help='Sends a random message')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

def scrambleString(string):
    if len(string) == 1:
        return string
    scramble = []
    listed = []
    listed[:0] = string
    while len(listed) != 0:
        ranChar = random.choice(listed)
        scramble.append(ranChar)
        listed.remove(ranChar)
    scrambled = ''.join(scramble)

    if (string == scrambled):
        print("Tis the same!")
        scrambled = scrambleString(scrambled)

    return scrambled


@bot.command(name='scramble', help='Scrambles the message inputed')
async def scramble_input(ctx, *args):
    scrambled = []
    for word in args:
        scrambled.append(scrambleString(word))
    output = ' '.join(scrambled)
    await ctx.send(output)

bot.run(TOKEN)
