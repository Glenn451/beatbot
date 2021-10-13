import asyncio
import config
import discord
import youtube_dl

from discord.ext import commands

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

class music_cog(commands.Cog):
    def __init__(self, client):
        self.client = client

    ytdl_format_options = {
        'format': 'bestaudio/best',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0'  # bind to ipv4 since ipv6 addresses cause issues sometimes
    }

    ffmpeg_options = {
        'options': '-vn',
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'
    }

    ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
    songs = asyncio.Queue()
    play_next_song = asyncio.Event()

    # check server and channel
    @commands.command()
    async def checkconnect(self, ctx):
        guild = ctx.message.guild
        channel = ctx.message.channel
        response = ("I'm in Server: {0} \n Channel: {1}".format(guild,channel))

    # Joins a voice channel
    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("You're not in a voice channel!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)


    # disconnects bot from voice channel
    @commands.command()
    async def stop(self, ctx):
        await ctx.voice_client.disconnect()

    # alternate disconnect command from voice channel
    @commands.command()
    async def fuckoff(self, ctx):
        await ctx.voice_client.disconnect()

    #  queue music setup
    @commands.command()
    async def audio_player_task():
        while True:
            play_next_song.clear()
            current = await songs.get()
            current.start()
            await play_next_song.wait()

    @commands.command(pass_context=True)
    async def play(ctx, url):
        if not client.is_voice_connected(ctx.message.server):
            voice = await client.join_voice_channel(ctx.message.author.voice_channel)
        else:
            voice = client.voice_client_in(ctx.message.server)

            player = await voice.create_ytdl_player(url, after=toggle_next)
        await songs.put(player)

    # skip track by stopping the current track and letting the next one in the queue get grabbed
    @commands.command()
    async def skip():
        await ctx.voice_client.stop()
        await ctx.send("Skipping current song")

    #  pause music
    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("Paused current playback")

    #  resume music
    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send("Resuming current playback")

    # stopping playback and clearing queue
    @commands.command()
    async def skip():
        await ctx.voice_client.stop()
        await ctx.send("Stopping playback entirely")


#### plays music in voice channel
#    @commands.command()
#    async def play(ctx, url):
#        ctx.voice_client.stop()
#        vc = ctx.voice_client
#        with ytdl as ydl:
#            info = ydl.extra_info(url, download=False)
#            url2 = info['formats'][0]['url']
#            source = await discord.FFmpegOpusAudio.from_probe(url2, **ffmpeg_options)
#            vc.play(source)
####

def setup(client):
    client.add_cog(music(client))
    print('Music is loaded')