import discord
from discord import channel
from discord.ext import commands
import sqlite3
import re

class gameCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sc(self, ctx, channelid=0, channelname=""):
        conn = sqlite3.connect(f'{ctx.guild.id}.db')
        cursor = conn.cursor()
        cursor.execute("SELECT channelid FROM gamechannel")
        gamechannel = str(cursor.fetchone()).strip('(,)')

        if ctx.channel.id != int(gamechannel):
            return
        elif ctx.channel.id == int(gamechannel):
            if channelname != "" and channelid != 0:
                cursor.execute("DELETE FROM gamechannel")
                cursor.execute("INSERT INTO gamechannel VALUES(?, ?, ?)", (ctx.guild.id, channelid, channelname))
                cursor.execute("SELECT channelname FROM gamechannel")
                conn.commit()
                channel = str(cursor.fetchone()).strip('(,)')
                await ctx.channel.send(f"Game channel has been set to {channel}")    
            elif channelname == "" and channelid == 0:
                cursor.execute("SELECT channelname FROM gamechannel")
                result = str(cursor.fetchone()).strip('(,)')
                if result is None:
                    await ctx.channel.send(f"Channel hasn't been set yet. See 3help_3sc to see how to set a channel.")
                elif result is not None:
                    await ctx.channel.send(f"Channel is set to {result}")
            elif (channelid != "" and channelname == 0) or (channelid == "" and channelname != 0):
                await ctx.channel.send("Missing a parameter. Make sure to include both the channel id and the channel name. For more information, type 3help_3sc")

    @commands.command()
    async def ssy(self, ctx, s1 = 0, s2 = 0, s3 = 0):
        conn = sqlite3.connect(f'{ctx.guild.id}.db')
        cursor = conn.cursor()
        cursor.execute("SELECT channelid FROM gamechannel")
        gamechannel = str(cursor.fetchone()).strip('(,)')
        
        if ctx.channel.id != int(gamechannel):
            return
        elif ctx.channel.id == int(gamechannel):
            if s1 != 0 and s2 != 0 and s3 != 0:
                cursor.execute("DELETE FROM syllablecount")
                cursor.execute("INSERT INTO syllablecount VALUES(?, ?, ?)", (s1, s2, s3))
                cursor.execute("SELECT * FROM syllablecount")
                conn.commit()
                syllables = str(cursor.fetchone()).strip('(,)')
                await ctx.channel.send(f"Game syllable count has been set to {syllables}")    
            elif s1 == 0 and s2 == 0 and s3 == 0:
                cursor.execute("SELECT * FROM syllablecount")
                syllables = str(cursor.fetchone()).strip('(,)')
                await ctx.channel.send(f"Game syllable count is set to {syllables}")

def setup(bot):
    bot.add_cog(gameCommands(bot))
