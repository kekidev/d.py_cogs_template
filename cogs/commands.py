import discord
from discord.ext import commands
from discord.ext.commands import *

class commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        return await ctx.send("pong")
   

def setup(client):
    client.add_cog(commands(client))