# bot.py
import discord
import json
import asyncio
import logging
import os
import music

from pathlib import Path
from discord.ext import commands
from discord.ext.commands import Bot

cogs = [music]

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print("{}\n-----".format(cwd))

logging.basicConfig(level=logging.INFO)

tokencode = json.load(open(cwd+'/config/secrets.json'))

TOKEN = tokencode['token']

version = 'Running BeatBot v.1.01'

Bot = commands.Bot(command_prefix = '>', case_insensitive=True)

for i in range(len(cogs)):
    cogs[i].setup(Bot)


@Bot.event
async def on_ready():
    print('-----------')
    print("logged in as user {} with an ID of {}".format(Bot.user.name, Bot.user.id))
    print('-----------')
    print(version)
    print('-----------')

Bot.run(TOKEN)
