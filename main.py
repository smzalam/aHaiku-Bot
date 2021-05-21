import discord
from discord.ext import commands
from mytoken import TOKEN
import syllables
import help

bot = commands.Bot(command_prefix="3")
bot.remove_command("help")

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))

@bot.listen('on_message')
async def message(message):
    if message.author == bot.user:
        return
        
    if message.content.startswith('3hello'):
        await message.channel.send('Hello!')

@bot.command()
async def syl(ctx, *, s="word"):
    await ctx.channel.send("The syllable count for '" + s + "' is " + str(syllables.estimate(s)))

bot.run(TOKEN)