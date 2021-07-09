import sqlite3

import discord
import syllables
from discord import channel, guild
from discord.ext import commands

import cogs.funcs as funcs  # pylint: disable=E0401


class gameCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sc(self, ctx, channelid=0, channelname=""):
        conn = sqlite3.connect(f'{ctx.guild.id}.db')
        cursor = conn.cursor()

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

    @commands.Cog.listener('on_message')
    async def message(self, message):
        if message.author == self.bot.user:
            return

        conn = sqlite3.connect(f'{message.guild.id}.db')
        cursor = conn.cursor()
        cursor.execute("SELECT channelid FROM gamechannel")
        gamechannel = int(str(cursor.fetchone()).strip('(,)'))
        
        if message.channel.id != gamechannel:
            return "Error"
        elif message.channel.id == gamechannel:
            
            # author = message.author

            haiku = message.content.split("/")

            scount = []
            for i in range(len(haiku)):
                scount.append(syllables.estimate(haiku[i]))
            scount = str(scount)[1:-1]

            cursor.execute("SELECT * FROM syllablecount")
            syllable = str(cursor.fetchone()).strip('(,)')

            if scount == syllable:
                print(funcs.counter)
                funcs.counter += 1
                print(funcs.counter)
                print(type(funcs.counter))
                cursor.execute("DELETE FROM haikustreak")
                cursor.execute("INSERT INTO haikustreak(streak) VALUES (?)", (funcs.counter,))
                conn.commit()
                await message.add_reaction("✅")      
            else:
                cursor.execute("SELECT * from haikustreak")
                streak = str(cursor.fetchone()).strip('(,)')
                print(streak)
                cursor.execute("DELETE FROM haikustreak")
                conn.commit()
                await message.channel.send(f"Not correct syllables. Streak lost! The highest streak was {streak}")

def setup(bot):
    bot.add_cog(gameCommands(bot))
