import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv('.env')
TOKEN = os.environ.get('token')
TestServer= os.environ.get('testingServerID')


intents=discord.Intents.default()
intents.members=True

client=commands.Bot(command_prefix="!",intents=intents)
@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

@client.event
async def on_member_join(member):
    pass

@client.event
async def on_message(message):
    '''collection of replys to messages with no prefix'''
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
    if message.content.startswith('cutie'):
        embed = discord.Embed(title=None)
        embed.set_image(url='https://c.tenor.com/iESegr2Kb6MAAAAd/narpy-cute.gif')
        await message.channel.send(embed=embed)
@client.command(pass_context=True)
async def join(ctx):
        print("Join recieved")
        if(ctx.author.voice):
            channel=ctx.message.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("You're not in a voice channel, silly.")
            
@client.command(pass_context=True)
async def leave(ctx):
    print("leave recieved")
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Bye!")
    else:
        await ctx.send("I already left")
client.run(TOKEN)