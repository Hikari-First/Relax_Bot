import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import ffmpeg
import time
import os

bot = commands.Bot(command_prefix="!")

@bot.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command()
async def play(ctx):
    channel = ctx.message.author.voice.channel
    vc = await channel.connect()
    while True:
        vc.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: print('done', e))
        vc.is_playing()
        await asyncio.sleep(203)

token = os.environ.get('BOT_TOKEN')
bot.run(token)
