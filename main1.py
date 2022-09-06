# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 14:55:33 2022

@author: Tristen
"""
from stack import Stack
import discord
from discord.ext import commands

from dotenv import load_dotenv
import os
import time


load_dotenv('.env')
TOKEN = os.environ.get('token')
TestServer = os.environ.get('testingServerID')

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


class Storage:
    def __init__(self):
        self.thds = {}


storage = Storage()


@bot.event
async def on_ready():  # When the bot first connects to discord
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()  # the bot looks for messages with the command_prefix and the following as commands:
async def leave(ctx):
    # Makes bot leave voice channel
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
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You're not in a voice channel, silly.")


@bot.command()
async def test(ctx):
    await ctx.reply('0')

    @bot.event
    async def on_message(message):
        if message.author == bot.user and message.content.isnumeric() and int(message.content) < 10:
            await message.reply(str(int(message.content)+1))
            await bot.process_commands(message)


@bot.command()
async def thread(ctx):
    # takes a reply chain and makes it into a thread.
    start = time.time()

    try:
        s = Stack()

        message = ctx.message
        name = message.content.removeprefix("!thread")
        while message.reference:
            # follows the reply chain to the end. Creates a thread on the first message in the chain
            # and adds the messages in the reply chain to the thread
            if '!thread' not in message.content:
                s.push(str(message.author.name)+":\n"+str(message.content))
            message = await ctx.channel.fetch_message(message.reference.message_id)

        thd = await message.create_thread(name=name)

        while not s.isEmpty():
            await thd.send(s.pop())

        storage.thds[message.id] = thd.jump_url
        end = time.time()
        print("Time taken :", end-start)
    except discord.errors.HTTPException or KeyError:
        link = [message.jump_url if message.id not in storage.thds else storage.thds[message.id]]
        await ctx.send("That message is already a thread: " + str(link))
        end = time.time()
        print("Time taken :", end-start)


@bot.command()
async def git(ctx):
    # Shameless self promotion!
    await ctx.send("Come help work on me!\nhttps://github.com/nannn3/PersonalDiscordBot")


@bot.event
async def on_message(message):

    '''collection of replys to messages with no prefix'''
    if message.author == bot.user:  # Responding to itself would be silly
        return

    if "@y'all" in message.content.lower():
        await message.reply("@everyone")

    if 'cutie' in message.content.lower():
        '''This one's almost exclusivly for my girlfriend'''
        embed = discord.Embed()
        embed.set_image(url='https://c.tenor.com/iESegr2Kb6MAAAAd/narpy-cute.gif')
        await message.channel.send(embed=embed)

    # clears out the input buffer, similar to fflush in c. lets it process other messages
    await bot.process_commands(message)

'''
code for importing cogs. Currently have none set up.
for filename in os.listdir('./cogs'):
    # Load all Cogs
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

    else:
        print(f'Unable to load {filename[:-3]}')
'''
bot.run(TOKEN)
