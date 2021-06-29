import discord
from discord.ext import commands
from discord.ext.commands import *

from dotenv import dotenv_values

config = dotenv_values(".env")

class events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Running")
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            return await ctx.send(f"{ctx.message.author.mention}, You don't have permission to execute this command")

 
def setup(client):
    client.add_cog(events(client))