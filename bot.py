import discord
from discord.ext import commands
from discord.utils import get
import ffmpeg
import os

bot = commands.Bot(command_prefix="!")

@bot.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

token = os.environ.get('BOT_TOKEN')
bot.run(token)
