import discord
from discord.ext import commands
import os
import sqlite3
from dotenv import dotenv_values

config = dotenv_values(".env")

intents = discord.Intents.all()

client = commands.Bot(command_prefix=config.get("PREFIX"), intents=intents)
client.remove_command("help")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")  

client.run(config.get("DISCORD_BOT_TOKEN")) 