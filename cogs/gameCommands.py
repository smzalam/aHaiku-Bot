import discord, json, syllables
from discord import channel, guild
from discord.ext import commands
from sqlalchemy import select, and_, insert, update, delete
from sqlalchemy.orm import Session
from cogs.database import models, database
from cogs.database import database_operations as dbops
from pprint import pprint
import cogs.funcs as funcs  # pylint: disable=E0401

class gameCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = dbops.DatabaseOperations()

    @commands.command()
    async def sc(self, ctx, operation, channelid=0, channelname=""):
        
        if operation == "--set" and channelname != "" and channelid != 0:
            await ctx.channel.send(f"{ctx.author.mention} Are you sure you want to set the channel to {channelname}? y/n")
            msg = await self.bot.wait_for('message')
            if msg.content == 'y':
                result = self.db.update_channel(ctx.guild.id, channelid, channelname)
            channel = self.db.select_server(ctx.guild.id, 'channel_name')
            await ctx.channel.send(f"Game channel has been set to {channel}!")
        elif operation == "--current" and channelname == "" and channelid == 0:
            channel = self.db.select_server(ctx.guild.id, 'channel_name')   
            if channel is None:  
                await ctx.channel.send(f"Channel hasn't been set yet. See 3help_3sc to see how to set a channel.")
            elif channel is not None:
                await ctx.channel.send(f"Channel is set to {channel}.")
        elif ((channelname != "" and operation != "-current") and channelid == 0) or (channelname == "" and channelid != 0):
            await ctx.channel.send("Wrong command. For more information, type 3help_3sc")

    @commands.command()
    async def ssy(self, ctx, operation, s1 = 0, s2 = 0, s3 = 0): 
        if operation == "--set" and s1 != 0 and s2 != 0 and s3 != 0:
            self.db.update_syllables(ctx.guild.id, s1, s2, s3)
            channel = self.db.select_syllables(ctx.guild.id)
            await ctx.channel.send(f"Game syllable count has been set to {channel['line_one']}-{channel['line_two']}-{channel['line_three']}")
        elif operation == "--current" and s1 == 0 and s2 == 0 and s3 == 0:
            self.db.select_syllables(ctx.guild.id)
            channel = self.db.select_syllables(ctx.guild.id)
            await ctx.channel.send(f"Game syllable count is {channel['line_one']}-{channel['line_two']}-{channel['line_three']}")
        else:
            await ctx.channel.send("Incorrect command. For more information, type 3help_3ssy.")

    @commands.command()
    async def streak(self, ctx):
        current_streak = self.db.select_server(ctx.guild.id, 'streak')
        server_name = self.db.select_server(ctx.guild.id, 'server_name')
        await ctx.channel.send(f"Current streak for `{server_name}`: `{current_streak}`")

    @commands.Cog.listener('on_message')
    async def message(self, message):
        if message.author == self.bot.user:
            return

        channel_id = self.db.select_server(message.guild.id, 'channel_id')
        x = str(message.channel.id)
        if x != channel_id or message.content.startswith("3"):
             return
        else:            
            haiku = message.content.split("/")
            query = self.db.select_syllables(message.guild.id)
            pattern = [query['line_one'], query['line_two'], query['line_three']]

            for i in range(len(pattern)):
                try:
                    if syllables.estimate(haiku[i]) == pattern[i] and i == 2:
                        self.db.update_streak(message.guild.id, models.ServerStats.streak + 1)
                        await message.add_reaction('✅')  
                    elif syllables.estimate(haiku[i]) == pattern[i]:
                        continue
                    else:
                        await message.add_reaction('❌')    
                        streak = self.db.select_server(message.guild.id, 'streak')
                        self.db.update_streak(message.guild.id, 0)
                        await message.channel.send(f"Streak broken at `{streak}`! Line {i+1} had {syllables.estimate(haiku[i])} syllables instead of {pattern[i]} syllables.")
                        break
                except IndexError:
                    await message.add_reaction('❌')    
                    streak = self.db.select_server(message.guild.id, 'streak')
                    self.db.update_streak(message.guild.id, 0)
                    await message.channel.send(f"Streak broken at `{streak}`! Complete haiku not written.")
                    break

    @commands.command()
    async def syl(self, ctx, *, s="word"):
        await ctx.channel.send("The syllable count for `" + s + "` is " + str(syllables.estimate(s)))

    @commands.command()
    async def rules(self, ctx):
        
        id = ctx.guild.id

        stmt = select(models.Rules)
        result = self.db.execute(stmt)
        

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

        await ctx.channel.send(embed = em)

        
async def setup(bot):
    await bot.add_cog(gameCommands(bot))
