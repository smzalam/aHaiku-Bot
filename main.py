import discord
from discord.ext import commands
import os

bot = commands.BOT(command_prefix="3")

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))

@bot.listen('on_message')
async def message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('3hello'):
        await message.channel.send('Hello!')

bot.run(os.getenv('TOKEN'))
