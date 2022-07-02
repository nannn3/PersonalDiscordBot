# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 14:55:33 2022

@author: Tristen
"""

# This example requires the 'members' privileged intents

import discord
from discord.ext import commands
import random

from dotenv import load_dotenv
import pdb
import os

load_dotenv('.env')
TOKEN = os.environ.get('token')
TestServer= os.environ.get('testingServerID')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def leave(ctx):
    if(ctx.voice_bot):
        await ctx.guild.voice_bot.disconnect()
        await ctx.send("Bye!")
    else:
        await ctx.send("I already left")

@bot.command()
async def join(ctx):
        if(ctx.author.voice):
            channel=ctx.message.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("You're not in a voice channel, silly.")
    

@bot.event 
async def on_message(message):
        
    '''collection of replys to messages with no prefix'''
    if message.author == bot.user:
        return
    
    if 'cutie' in message.content:
        '''This one's almost exclusivly for my girlfriend'''
        embed = discord.Embed()
        embed.set_image(url='https://c.tenor.com/iESegr2Kb6MAAAAd/narpy-cute.gif')
        await message.channel.send(embed=embed) 
        
    await bot.process_commands(message) #clears out the input buffer, similar to fflush in c. lets it process other messages
bot.run(TOKEN)