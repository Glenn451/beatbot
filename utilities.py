import discord
import json
import asyncio
import random
import time
import utilities
import logging
import os

from pathlib import Path
from discord.ext import commands
from discord.ext.commands import bot


#kinky dice
def k_dice():
    kdie1 = ['touch', 'lick', 'suck on', 'look at', 'grab', 'breathe on']
    kdie2 = ['neck', 'ear', 'breast', 'thigh', 'hand',' lips']
    k_result = ("Rolling kinky dice - here's what you do: " + random.choice(kdie1) + ' ' + random.choice(kdie2))
    return k_result


#ping test
@commands.command()
    async def ping(self, ctx):
        ping = int(self.client.latency * 100)
        await ctx.send(':ping_pong: Pong! (In {}ms)'.format(str(ping)))