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
            if self.db.select_server(ctx.guild.id, 'channel_name') is None:
            # self.db.execute(select(models.ServerStats.channel_name).where(models.ServerStats.server_id == ctx.guild.id)).scalar() is None:
                self.db.insert_server(ctx.guild.id, ctx.guild.name, channelid, channelname)
                # self.db.execute(insert(models.ServerStats).values(server_id = ctx.guild.id, server_name = ctx.guild.name, channel_id = channelid, channel_name=channelname, streak = 0))
            else:
                result = self.db.update_channel(ctx.guild.id, channeid, channelname)
                # self.db.execute(update(models.ServerStats).where(models.ServerStats.server_id == ctx.guild.id).values(channel_id = channelid, channel_name=channelname))
            # stmt_select = select(models.ServerStats.channel_name).where(models.ServerStats.server_id == ctx.guild.id)
            # channel = self.db.execute(stmt_select).scalar()
            channel = self.db.select_server(ctx.guild.id, 'channel_name')
            await ctx.channel.send(f"Game channel has been set to {channel}!")
        elif operation == "--current" and channelname == "" and channelid == 0:
            # stmt_select = select(models.ServerStats.channel_name).where(models.ServerStats.server_id == ctx.guild.id)
            # channel = self.db.execute(stmt_select).scalar() 
            channel = self.db.select_server(ctx.guild.id, 'channel_name')   
            if channel is None:  
                await ctx.channel.send(f"Channel hasn't been set yet. See 3help_3sc to see how to set a channel.")
            elif channel is not None:
                await ctx.channel.send(f"Channel is set to {channel}.")
        elif ((channelname != "" and operation != "-current") and channelid == 0) or (channelname == "" and channelid != 0):
            await ctx.channel.send("Wrong command. For more information, type 3help_3sc")

    @commands.command()
    async def ssy(self, ctx, operation, s1 = 0, s2 = 0, s3 = 0): 
        if operation == "-set" and s1 != 0 and s2 != 0 and s3 != 0:
            stmt_update = update(models.Syllables).where(models.Syllables.server_id == ctx.guild.id).values(line_one = s1, line_two = s2, line_three = s3)
            result = self.db.execute(stmt_update)
            stmt_select = select(models.Syllables).where(models.Syllables.server_id == ctx.guild.id)
            channel = self.db.execute(stmt_select).scalars().fetchall()    
            await ctx.channel.send(f"Game syllable count has been set to {channel}")
        elif operation == "-current" and s1 == 0 and s2 == 0 and s3 == 0:
            stmt_select = select(models.Syllables).where(models.Syllables.server_id == ctx.guild.id)
            channel = self.db.execute(stmt_select).scalars().fetchall()    
            await ctx.channel.send(f"Game syllable count has been set to {channel}")
        else:
            await ctx.channel.send("Incorrect command. For more information, type 3help_3ssy.")

    @commands.Cog.listener('on_message')
    async def message(self, message):
        if message.author == self.bot.user:
            return

        stmt = select(models.ServerStats.channel_id).where(models.ServerStats.server_id == message.guild.id)
        channel_id = self.db.execute(stmt).scalar() 
        if message.channel.id != channel_id and message.content[0] != "3":
             await message.channel.send("Wrong channel. Go to the set haiku channel to play the game.")
        else:            
            # author = message.author

            haiku = message.content.split("/")
            stmt_select = select(and_(models.Syllables.line_one, models.Syllables.line_two, models.Syllables.line_three)).where(models.Syllables.server_id == message.guild.id)
            channel = self.db.execute(stmt_select).scalars().fetchall() 

            for i in range(len(haiku)):
                if syllables.estimate(haiku[i]) == channel[i]:
                    continue
                else:
                    self.db.execute(update(models.ServerStats).where(models.ServerStats.server_id == message.guild.id).values(streak = 0))
                    await message.channel.send(f"Streak broken! Line {i} had {syllables.estimate(haiku[i])} syllables instead of {channel[i]} syllables.")

            self.db.execute(update(models.ServerStats).where(models.ServerStats.server_id == message.guild.id).values(streak = models.ServerStats.streak + 1))
            await message.add_reaction("✅")      


async def setup(bot):
    await bot.add_cog(gameCommands(bot))
