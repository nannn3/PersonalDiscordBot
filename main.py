import nextcord
from nextcord import Interaction
from nextcord.ext import commands


intents=nextcord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!',intents=intents)

@client.event
async def on_ready():
    print("The bot is now ready for use")

testingServerID = 988481933841416273

@nextcord.slash_command(name="hello",description="Hello World")
async def hellocommand(interaction: Interaction)
    await interaction.response.send_message("Hello Wolrd")

client.run('OTg4NDc3NTAyOTI4MzM0OTU4.Go32uL.cW-SzPkctlD1_n7iKzsI3KQ3kLLPcAdlqH7gmk')

