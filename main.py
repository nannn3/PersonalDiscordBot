
import discord
from discord.ext import commands
from dotenv import load_dotenv
import pdb
import os

load_dotenv('.env')
TOKEN = os.environ.get('token')
TestServer= os.environ.get('testingServerID')


intents=discord.Intents.default()
intents.members=True

bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

@bot.event
async def on_member_join(member):
    pass

@bot.event ()
async def on_message(message):
    '''collection of replys to messages with no prefix'''
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
    if message.content.startswith('cutie'):
        embed = discord.Embed(title=None)
        embed.set_image(url='https://c.tenor.com/iESegr2Kb6MAAAAd/narpy-cute.gif')
        await message.channel.send(embed=embed)
    
    if message.content.lower().startswith('$join'):
        pdb.set_trace()
        '''
        Joins voice channel of person who types '$join'
        '''
        if message.author.voice == None:
            await message.reply("You're not in a voice channel, Silly")
        else:
            channel=message.author.voice.channel
            await channel.connect()
    #if message.content.lower().startswith('$leave'):
        
@bot.command()
async def leave(ctx):
    print("leave recieved")
    if(ctx.voice_bot):
        await ctx.guild.voice_bot.disconnect()
        await ctx.send("Bye!")
    else:
        await ctx.send("I already left")
bot.run(TOKEN)