# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 13:56:00 2022

@author: easto
"""

import discord
from discord.ext import commands
from funcs import list_to_str
from Game_Module import Game, game

class Player_Commands(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    # Commands
    @commands.command(name='join', help='User joins game queue if nothing else is specified. If another name is stated,attempts to add that player. Searches by "begins with"')
    async def join(self, ctx, *args):
        if args == ():
            await ctx.send(game.add_player(ctx.author.name))
        else:
            found = await ctx.guild.query_members(list_to_str(args))
            if len(found) == 0:
                await ctx.send("Player not found")
            for i in found:
                await ctx.send(game.add_player(i.name))
        
    @commands.command(name='remove', help='User (or specified if -join is followed by anything) leaves game queue.')
    async def remove(self, ctx, *args):
        if args == ():
            await ctx.send(game.remove_player(ctx.author.name))
        else:
            await ctx.send(game.remove_player(list_to_str(args)))
            
    @commands.command(name='all_join', help='All server members except the bot join')
    async def all_join(self, ctx):
        for member in ctx.guild.members:
            if member.name != "MafiaBot":
                await ctx.send(game.add_player(member.name))
            
    @commands.command(name='queue', help='Lists all players in game')
    async def queue(self, ctx):
        await ctx.send(game.list_queue())


def setup(client):
    client.add_cog(Player_Commands(client))