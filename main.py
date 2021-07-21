import discord
from discord.ext import commands
import os
from dotenv import dotenv_values

# .env 파일 불러오기
config = dotenv_values(".env")

intents = discord.Intents.all()

client = commands.Bot(command_prefix=config.get("PREFIX"), intents=intents)
client.remove_command("help") # help 명령어 지우기

# cogs 안에 있는 모든 파이썬 파일 불러오기
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")  

client.run(config.get("DISCORD_BOT_TOKEN")) 
