import discord
from discord.ext import commands
from mytoken import TOKEN
import syllables

bot = commands.Bot(command_prefix="3")
bot.remove_command("help")

@bot.listen('on_message')
async def message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('3hello'):
        channel = bot.get_channel(846889420220792842)
        await message.channel.send('Hello!')

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))


extensions = ['cogs.helpCommands',
              'cogs.haikuCommands',
              'cogs.searchCommands']

if __name__ == '__main__':
    for ext in extensions:
        bot.load_extension(ext)

bot.run(TOKEN)