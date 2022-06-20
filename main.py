from asyncio.constants import SSL_HANDSHAKE_TIMEOUT
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import os
from os.path import join, dirname
from dotenv import load_dotenv
import pdb
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

token = os.environ.get("token")
serverTest = os.environ.get("testingServerID")
serverTest=int(serverTest)
intents = nextcord.Intents(messages=True,message_content = True, guilds=True)


bot = commands.Bot(command_prefix='$')

@bot.command()
async def ping(ctx):
    await ctx.reply('Pong!')
@bot.event
async def on_ready():#When the bot boots up
    print("The bot is now ready for use")

@bot.slash_command(guild_ids=[serverTest]) #Basic test of slash commands
async def hello(interaction: Interaction):
    await interaction.response.send_message("Hello Wolrd!")
"""
it looks like discord doesn't let this happen. Fair enough.
@bot.event
async def on_message(message):
    print("Message Recieved")
    if message.author == bot.user:
        return
    print(message.content)
    pdb.set_trace()
"""

#set up COG reading folder
Initial_extensions=[]

for fileName in os.listdir('./cogs'):
    if fileName.endswith('.py'):
        Initial_extensions.append("cogs."+fileName[:-3])
if __name__=='__main__':
    for extension in Initial_extensions:
        bot.load_extension(extension)

token=str(token)
bot.run(token)
