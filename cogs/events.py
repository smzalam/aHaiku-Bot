import discord, json
from discord.ext import commands
from sqlalchemy import select, and_, insert, delete
from sqlalchemy.orm import Session
from cogs.database import models, database
from cogs.database import database_operations as dbops
from pprint import pprint
from cogs.funcs import db_clean

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = dbops.DatabaseOperations()

    @commands.Cog.listener()
    async def on_ready(self):
        print("We have logged in as {0.user}".format(self.bot))

    @commands.Cog.listener('on_message')
    async def message(self, message):
        if message.author == self.bot.user:
            return

        if message.content.startswith('3hello'):
            await message.channel.send('It works!')

    @commands.Cog.listener()
    async def on_guild_join(self, guild):

        # stmt = select(models.ServerStats).where(models.ServerStats.server_id == id)
        # result = self.db.execute(stmt)
        result = self.db.select_server(guild.id, 'all')
        if result == None:
            server = NewServer(guild.id, guild.name)
            server.create_server()

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):

        server = NewServer(guild.id, guild.name)
        server.remove_server()

class NewServer:
    def __init__(self, id, name):
        self.db = dbops.DatabaseOperations()
        self.id = id
        self.name = name

    def create_server(self):
        self.add_server_stats()
        self.add_syllables()

    # def add_to_db(self, data):
    #     self.db.add(data)
    #     self.db.commit()
    #     self.db.refresh(data)

    def add_server_stats(self):
        # new_server = {'server_id': self.id, 'sever_name': self.name}
        # server_new = models.ServerStats(**new_server)
        # self.add_to_db(server_new)
        self.db.insert_server(self.id, self.name)

    def add_syllables(self):
        # new_server = {'server_id': self.id, 'line_one': 0, 'line_two': 0, 'line_three': 0}
        # syllables_new = models.Syllables(**new_server)
        # self.add_to_db(syllables_new)
        self.db.insert_syllables(self.id, 0, 0, 0)

    def remove_server(self):
        self.db.delete_server(self.id)

async def setup(bot):
    await bot.add_cog(Events(bot))