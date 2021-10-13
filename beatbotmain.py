# bot.py
import discord
import json
import asyncio
import random
import time
import utilities
import logging
import os
import music

from pathlib import Path
from discord.ext import commands
from discord.ext.commands import Bot

cogs = [music_cog]


cwd = Path(__file__).parents[0]
cwd = str(cwd)
print("{}\n-----".format(cwd))

logging.basicConfig(level=logging.INFO)

tokencode = json.load(open(cwd+'/config/secrets.json'))

TOKEN = tokencode['token']

songs = asyncio.Queue()
play_next_song = asyncio.Event()

# version = '1.01'

client = commands.Bot(command_prefix = '>', case_insensitive=True, intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

@client.event
async def on_ready():
    print('-----------')
    print("logged in as user {} with an ID of {}".format(client.user.name, client.user.id))
    print('-----------')


#kinky dice game command
@client.command(name='kinkydice', help='roll 2x 6-sided kinky dice (action + body part)')
async def kinkydice(ctx):
    diceresult = utilities.k_dice()
    await ctx.send(diceresult)




client.loop.create_task(audio_player_task())

client.run(TOKEN)
