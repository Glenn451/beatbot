# beatbot
BeatBot - Bot of Vibes - personal discord bot project

Pieced together from multiple sources.

Self-hosted bot that you can run locally or on a VPS (AWS, DigitalOcean, Linode).

Requirements:
  Python 3+
  Discord.py / Discord (use pip)
  Youtube-DL
  FFMPEG
  PyNaCl

Replaced the token in the file config/secrets_template.json with your own bot's token and then rename the file to "secrets.json"

Bot is capable of running on multiple Discord servers at the same time, however you would need to make it so that people can invite it and provision enough resources for that to happen. That will also result in increased costs from hosting (bandwidth mostly), so be careful about letting anyone invite your hosted bot.
