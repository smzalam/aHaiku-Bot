import discord
from discord.ext import commands
import syllables


class haikuCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def syl(self, ctx, *, s="word"):
        channel = self.bot.get_channel(846889420220792842)
        await ctx.channel.send("The syllable count for `" + s + "` is " + str(syllables.estimate(s)))

    @commands.command()
    async def rules(self, ctx):
        em = discord.Embed(
            title = f'{ctx.message.guild.name} aHaiku Game Rules',
            color = discord.Color.purple()
        )

        em.add_field(
            name="1. The same person can't go twice in a row."
        )

        em.add_field(
            name="2. The haiku verses should be written on new lines. Check an example to see the format of writing a haiku."
        )

        channel = self.bot.get_channel(846889420220792842)
        await ctx.channel.send(embed = em)

    @commands.command()
    async def arules(self, ctx, pos, rule):
        em = discord.Embed(
            title = f'{ctx.message.guild.name} aHaiku Game Rules',
            color = discord.Color.purple()
        )

        em.add_field(
            name="Rule Added",
            value = f'{pos}.{rule}',
            inline = False
        )

        em.add_field(
            name = "Rules",
            value = "right here. :3",
            inline = False
        )
def setup(bot):
    bot.add_cog(haikuCommands(bot))