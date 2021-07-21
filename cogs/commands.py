import discord
from discord.ext import commands
from discord.ext.commands import *

class commands(commands.Cog): # commands.Cog 상속
    def __init__(self, client):
        self.client = client # main.py에서 보내주는 client를 self.client에다가 넣기

    @commands.command() # 이건 명령어다 라고 선언해주는 데코레이터
    async def ping(self, ctx): # self, ctx은 그냥 뭐든간에 다 있어야합니다
        return await ctx.send("pong")
   
# 셋업 함수
def setup(client):
    client.add_cog(commands(client))
