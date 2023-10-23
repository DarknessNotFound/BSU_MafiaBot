# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 13:18:41 2022

@author: easto
"""
import discord
from discord.ext import commands

class Admin(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    # Commands
    @commands.command(name='slideIntoDMs', help='Messages the user that typed the msg.')
    async def slideIntoDMs(self, ctx):
        msg = "I just slid into your dms"
        await ctx.message.author.send(msg)
        
    @commands.command(name='echo', help='Echos what the user just said')
    async def echo(self, ctx, *args):
        await ctx.send(args.join(' '))
        
    @commands.command(name='members', help='Lists all members')
    async def members(self, ctx):
        for member in ctx.guild.members:
            await ctx.send(member.name)


def setup(client):
    client.add_cog(Admin(client))