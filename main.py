import discord
from discord.ext import commands
from mytoken import TOKEN
import syllables

bot = commands.Bot(command_prefix="3")
bot.remove_command("help")

extensions = ['cogs.helpCommands',
              'cogs.haikuCommands',
              'cogs.searchCommands',
              'cogs.events']

if __name__ == '__main__':
    for ext in extensions:
        bot.load_extension(ext)

bot.run(TOKEN)