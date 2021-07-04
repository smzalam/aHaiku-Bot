import random

import discord
import requests
from discord.embeds import Embed
from discord.ext import commands

from cogs.funcs import haiku  # pylint: disable=E0401


class searchCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def example(self, ctx):
        author = random.randint(1,3)
        authorname = ""
        if author == 1:
            poemnum = random.randint(0, 42)
            authorname = "Kobayashi Issa"
        elif author == 2:
            poemnum = random.randint(0, 52)
            authorname = "Matsuo Bashō"
        elif author == 3:
            poemnum = random.randint(0, 21)
            authorname = "Yosa Buson"

        example = haiku(author, poemnum)
        print(example)

        em = discord.Embed(
            title = "Haiku Example"
            )

        em.add_field(
            name = "Author",
            value = f"{authorname}",
            inline = False
        )

        em.add_field(
            name = "Haiku",
            value = example
        )

        await ctx.channel.send(embed = em)

def setup(bot):
    bot.add_cog(searchCommands(bot))
