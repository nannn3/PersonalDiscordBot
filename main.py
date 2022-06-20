import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN=os.environ.get("token")
testingServerID=os.environ.get("testingServerID")

intents=nextcord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!',intents=intents)

@client.event
async def on_ready():
    print("The bot is now ready for use")

@nextcord.slash_command(name="hello",description="Hello World")
async def hellocommand(interaction: Interaction)
    await interaction.response.send_message("Hello Wolrd")

client.run('TOKEN')
