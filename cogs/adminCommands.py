from discord.ext import commands
from .utils import checks
import discord

class adminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='reload', hidden=True)
    @checks.is_owner()
    async def _reload(self, ctx, module : str):
        """Reloads a module"""
        try:
            self.bot.reload_extension(module)
        except Exception as e:
            await ctx.channel.send('\N{PISTOL}')
            await ctx.channel.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.channel.send('\N{OK HAND SIGN}')

async def setup(bot):
    await bot.add_cog(adminCommands(bot))