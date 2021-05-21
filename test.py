import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='_')

channel = str(bot.get_channel(844963672802459648))

print(channel)