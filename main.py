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
intents=nextcord.Intents.default()
intents.members = True
#pdb.set_trace()
client = commands.Bot(command_prefix='!')
testingServerID=serverTest
@client.event

async def on_ready():#When the bot boots up
    print("The bot is now ready for use")
    print(testingServerID)

@client.slash_command(guild_ids=[testingServerID])
async def hello(interaction: Interaction):
    await interaction.response.send_message("Hello Wolrd!")

token=str(token)
client.run(token)
