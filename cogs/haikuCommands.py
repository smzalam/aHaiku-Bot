import discord
from discord.ext import commands
import syllables
import sqlite3
from cogs.funcs import getting_pos, getting_rules, writing_rules # pylint: disable=E0401

class haikuCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def syl(self, ctx, *, s="word"):
        # channel = self.bot.get_channel(ctx.channel.id)
        await ctx.channel.send("The syllable count for `" + s + "` is " + str(syllables.estimate(s)))

    @commands.command()
    async def rules(self, ctx):
        
        id = ctx.guild.id
        conn = sqlite3.connect(f'{id}.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM rules")
        result = cursor.fetchall()  

        pos = getting_pos(result)
        rules = getting_rules(result)
        val = writing_rules(pos, rules)

        em = discord.Embed(
            title = f'{ctx.guild.name} aHaiku Game Rules',
            color = discord.Color.purple()
        )

        em.add_field(
            name = "Rules",
            value = val
        )

        # channel = self.bot.get_channel(ctx.channel.id)
        await ctx.channel.send(embed = em)

    @commands.command()
    async def arules(self, ctx, pos, *, rule):

        id = ctx.guild.id
        conn = sqlite3.connect(f'{id}.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO rules(position, rules) VALUES(?, ?)", (pos, rule))

        cursor.execute("SELECT * FROM rules")
        result = cursor.fetchall()  

        pos = getting_pos(result)
        rules = getting_rules(result)
        val = writing_rules(pos, rules)

        em = discord.Embed(
            title = f'{ctx.guild.name} aHaiku Game Rules',
            color = discord.Color.purple()
        )
        
        em.add_field(
            name = "Rule Added",
            value = f"`{pos[-1]}. {rules[-1]}`",
            inline = False
        )

        em.add_field(
            name = "Rules",
            value = val
        )
        conn.commit()
        conn.close()
        await ctx.channel.send(embed = em)

    @commands.command()
    async def rrules(self, ctx, pos):

        id = ctx.guild.id
        conn = sqlite3.connect(f'{id}.db')
        cursor = conn.cursor()
        cursor.execute("SELECT position, rules FROM rules WHERE position = ?", (pos))
        deleted = cursor.fetchone()
        cursor.execute("DELETE FROM rules WHERE position = ?", (pos))

        cursor.execute("SELECT * FROM rules")
        result = cursor.fetchall()  

        pos = getting_pos(result)
        rules = getting_rules(result)
        val = writing_rules(pos, rules)

        em = discord.Embed(
            title = f'{ctx.guild.name} aHaiku Game Rules',
            color = discord.Color.purple()
        )
        
        em.add_field(
            name = "Deleted rule",
            value = f"`{deleted[0]}. {deleted[1]}`",
            inline = False
        )

        em.add_field(
            name = "Rules",
            value = val
        )
        conn.commit()
        conn.close()
        await ctx.channel.send(embed = em)

def setup(bot):
    bot.add_cog(haikuCommands(bot))