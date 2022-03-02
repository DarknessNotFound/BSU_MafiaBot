# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 14:40:26 2022

@author: easto
"""

import discord
from discord.ext import commands
from funcs import list_to_str, accessible_channel
from Game_Module import Game, game

class Role_Commands(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    # Commands
    @commands.command(name='select', help='Adds new role to the game role selection')
    async def select(self, ctx, *args):
        if accessible_channel(ctx):
            await ctx.send(game.add_role(list_to_str(args)))
        else:
            await ctx.send("This isn't the time to use that!")
        
    @commands.command(name='selection', help='Adds new role to the game role selection')
    async def selection(self, ctx):
        if accessible_channel(ctx):
            await ctx.send(game.list_roles())
        await ctx.send("This isn't the time to use that!")

    @commands.command(name='deselect', help='Shows all roles in current game selection')
    async def deselect(self, ctx, *args):
        if accessible_channel(ctx):
            await ctx.send(game.remove_role(list_to_str(args)))
        await ctx.send("This isn't the time to use that!")
        
    @commands.command(name='preset', help='Allows for quick selection of roles. If nothing else is specified, lists all presets. Otherwise, deletes the current selection and adds the preset roles')
    async def preset(self, ctx, *args):
        if accessible_channel(ctx):
            if args == ():
                await ctx.send(game.all_presets())
            else:
                await ctx.send(game.assign_preset(list_to_str(args)))
        await ctx.send("This isn't the time to use that!")
        


def setup(client):
    client.add_cog(Role_Commands(client))