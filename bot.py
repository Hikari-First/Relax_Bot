import discord
from discord.ext import commands
from discord.utils import get
import os

bot = commands.Bot(command_prefix="!")

@bot.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()


@bot.command(pass_context = True)
async def play(ctx):

    voice_client = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)

    if voice_client.is_connected:
        song_there = os.path.isfile('song.mp3')

        await ctx.send("Pls wait, it won't take long.")

        voice = discord.utils.get(bot.voice_clients, guild = ctx.guild)

        voice.play(discord.FFmpegPCMAudio('song.mp3'), after = lambda e: print(f'[LOG]: {name}, music ended.'))

        voice.source = discord.PCMVolumeTransformer(voice.source)

        voice.source.volume = 0.07

        song_name = name.rsplit('-', 2)

        await ctx.send(f'Np: {song_name[0]}')

    else:

        await ctx.send('I`m not connected to ur VC!')


token = os.environ.get('BOT_TOKEN')
bot.run(token)
