import discord
from discord.ext import commands
import syllables
import sqlite3
from funcs import *


class haikuCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def syl(self, ctx, *, s="word"):
        channel = self.bot.get_channel(ctx.channel.id)
        await ctx.channel.send("The syllable count for `" + s + "` is " + str(syllables.estimate(s)))

    @commands.command()
    async def rules(self, ctx):
        
        id = ctx.guild.id
        conn = sqlite3.connect(f'{id}.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM rules")
        result = cursor.fetchall()  

        val = ''
        pos = []
        rules = []

        for i in result:
            pos.append(i[0])
            rules.append(i[1])

        for i in range(len(rules)):
            val += str(pos[i]) + '.' + str(rules[i]) + '\n'

        em = discord.Embed(
            title = f'{ctx.guild.name} aHaiku Game Rules',
            color = discord.Color.purple()
        )

        em.add_field(
            name="Rules",
            value=val
        )

        channel = self.bot.get_channel(ctx.channel.id)
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