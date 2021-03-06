# beatbot
BeatBot - Bot of Vibes - personal Discord music bot project

Pieced together from multiple sources.

Self-hosted bot that you can run locally or on a VPS (AWS, DigitalOcean, Linode).

Requirements:
  * Python 3+
  * Discord.py / Discord (use pip)
  * Youtube-DL
  * FFMPEG
  * PyNaCl

I'm assuming that you can figure out how register a bot on discord and set it up yourself. There are plenty of resources online covering that.
Replace the token in the file config/secrets_template.json with your own bot's token and then rename the file to "secrets.json"

Bot is capable of running on multiple Discord servers at the same time, however you would need to make it so that people can invite it and provision enough resources for that to happen. That will also result in increased costs from hosting (bandwidth mostly), so be careful about letting anyone invite your hosted bot. I'm running it on a $5/month DO droplet and it was able to handle 4 servers simultaneously without issue.

The intention is to update this bot with some additional utilities related to Discord server role management so that you can automate role assignment based on reacting to messages sent by the bot.

Commands use the ">" prefix currently, can be changed manually in beatbotmain.py - will consider future update to allow server specific command prefix and the ability to change it from within discord.


Special thanks to <a href='https://github.com/xavierjenkins99'>xavierjenkins99</a> for code review, editing contributions, and testing.


Licensed under GPL3
