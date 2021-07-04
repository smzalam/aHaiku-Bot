import discord
from discord.ext import commands

class gameCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sc(self, ctx, channel):
        pass

    async def ssy(self, ctx, syllables):
        pass

def setup(bot):
    bot.add_cog(gameCommands(bot))