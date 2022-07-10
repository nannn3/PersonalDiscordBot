# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 14:55:33 2022

@author: Tristen
"""

# This example requires the 'members' privileged intents

import discord
from discord.ext import commands

from dotenv import load_dotenv
import os

load_dotenv('.env')
TOKEN = os.environ.get('token')
TestServer= os.environ.get('testingServerID')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)



        
@bot.event
async def on_ready(): #When the bot first connects to discord
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command() #the bot looks for messages with the command_prefix and the following as commands:
async def leave(ctx):
    '''Makes bot leave voice channel
    '''
    if(ctx.voice_bot):
        await ctx.guild.voice_bot.disconnect()
        await ctx.send("Bye!")
    else:
        await ctx.send("I already left")
        

    

@bot.command()
async def join(ctx):
    '''
    Makes bot join voice channel
    It will join the voice channel of the person who used the command
    '''
    if(ctx.author.voice):
            channel=ctx.message.author.voice.channel
            await channel.connect()
    else:
            await ctx.send("You're not in a voice channel, silly.")
    
@bot.command()
async def git(ctx):
    #Shameless self promotion!
    await ctx.send("Come help work on me!\nhttps://github.com/nannn3/PersonalDiscordBot")
    
@bot.event 
async def on_message(message):
        
    '''collection of replys to messages with no prefix'''
    if message.author == bot.user: #Responding to itself would be silly
        return
    
    if 'cutie' in message.content:
        '''This one's almost exclusivly for my girlfriend'''
        embed = discord.Embed()
        embed.set_image(url='https://c.tenor.com/iESegr2Kb6MAAAAd/narpy-cute.gif')
        await message.channel.send(embed=embed) 
        
    await bot.process_commands(message) #clears out the input buffer, similar to fflush in c. lets it process other messages
    
for filename in os.listdir('./cogs'):
    #Load all Cogs
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')
    
  else:
    print(f'Unable to load {filename[:-3]}')
bot.run(TOKEN)