import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from nextcord import FFmpegAudio
from nextcord import Member
from nextcord.ext.commands import has_permissions, MissingPermissions
import requests
import json
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__),'..','.env')
load_dotenv(dotenv_path)

intents=nextcord.Intents.default()
intents.members=True

class Audio(commands.Cog):
    def __init__(self,bot):
            self.bot = bot
    serverTest = os.environ.get("testingServerID")  
    serverTest=int(serverTest)
    @nextcord.slash_command(guild_ids=[serverTest])
    async def test(self, interaction: Interaction):
        await interaction.response.send_message("Test!")

def setup(bot):
    bot.add_cog(Audio(bot))

