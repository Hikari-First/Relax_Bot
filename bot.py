import discord
from discord.ext import commands
from discord.utils import get
import ffmpeg
import os

bot = commands.Bot(command_prefix="")

@bot.event
async def on_ready():
    print("Бот активен")


@bot.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command()
async def play(ctx):
    channel = ctx.message.author.voice.channel
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: print('done', e))
    vc.is_playing()

token = os.environ.get('BOT_TOKEN')
bot.run(token)
