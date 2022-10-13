import random
import discord
import requests
from discord.embeds import Embed
from discord.ext import commands

from cogs.funcs import haiku, poemsearch, authors, titles, lcounts  # pylint: disable=E0401


class searchCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def example(self, ctx):
        author = random.randint(1,3)

        authorname = ""
        if author == 1:
            poemnum = random.randint(0, 41)
            authorname = "Kobayashi Issa"
        elif author == 2:
            poemnum = random.randint(0, 51)
            authorname = "Matsuo Bashō"
        elif author == 3:
            poemnum = random.randint(0, 20)
            authorname = "Yosa Buson"

        example = haiku(author, poemnum)

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

    @commands.command()
    async def search(self, ctx, author=None, *, title=None):
        response = poemsearch(author, title)

        if len(response) > 2000:
            n = 2000
            result = [response[i:i+n] for i in range(0, len(response), n)]
            for i in range(len(result)):
                await ctx.channel.send(result[i])
        else:
            await ctx.channel.send(response)

async def setup(bot):
    await bot.add_cog(searchCommands(bot))
