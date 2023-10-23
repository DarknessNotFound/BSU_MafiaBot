# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 14:47:48 2022

@author: easto
"""

import discord
from discord.ext import commands
from funcs import list_to_str, accessible_channel
from Game_Module import Game, game

class Game_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    # Commands
    @commands.command(name='new', help='Creates a new game')
    async def new(self, ctx):
        if accessible_channel(ctx):
            game.new()
            await ctx.send("New game begun")
        else:
            await ctx.send("This isn't the time to use that!")
        
    @commands.command(name='start', help='Fills remaing roles as Villager and starts game')
    async def start(self, ctx):
        if accessible_channel(ctx):
            await ctx.send(game.fill())
            if game.good_to_go():
                game.assign_random_roles()
                
                # Informs current players of their roles by DMs
                for member in ctx.guild.members:
                    if game.find_player(member.name):
                        await member.send(game.player_role(member.name))
                
                await ctx.send("Random roles assigned")
                await ctx.send("Game started!!!")
            else:
                await ctx.send("Start aborted (like you should have been). More roles than players, or only mimics are in the game. Review and try again.")
        else:
            await ctx.send("This isn't the time to use that!")
    

def setup(client):
    client.add_cog(Game_Commands(client))