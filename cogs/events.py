import discord
from discord.ext import commands
from discord.ext.commands import *

from dotenv import dotenv_values

config = dotenv_values(".env")

class events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener() # 이건 이벤트라고 선언해주는 데코레이터
    async def on_ready(self): # self는 모든 함수에 들어가야합니다
        print("Running")
    
    # 에러 핸들링 다음 강의에서 볼 것
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            return await ctx.send(f"{ctx.message.author.mention}, You don't have permission to execute this command")

 
def setup(client):
    client.add_cog(events(client))
