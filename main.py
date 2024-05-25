import discord
import os

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$?'):
    await message.channel.send(
        '> **Du brauchst Hilfe?** \n> https://forms.gle/8uvH9AkFRgK96RjF9, oder DM einem Mod \n> Befehle: \n> $?: Diese Liste auflisten \n> mehr bald...\n> \n> Developed by tamino1230'
    )

  if message.content.startswith('$df?'):
    await message.channel.send(
        '> **Befehle für DF:** \n> $df: Diese Liste auflisten \n> $?: Hilfe für Normale User auflisten \n> \n> Developed by tamino1230'
    )

client.run(os.getenv('token'))
