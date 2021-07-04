import discord
from discord.ext import commands
import sqlite3

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("We have logged in as {0.user}".format(self.bot))

    @commands.Cog.listener('on_message')
    async def message(self, message):
        if message.author == self.bot.user:
            return

        if message.content.startswith('3hello'):
            channel = self.bot.get_channel(846889420220792842)
            await message.channel.send('Hello!')

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
            conn = sqlite3.connect('ahaiku.db')
            cursor = conn.cursor()

            id = guild.id
            name = guild.name

            cursor.execute(f"SELECT serverid, servername FROM servers WHERE serverid = {guild.id}")
            result = cursor.fetchone()
            if result is None:
                cursor.execute("INSERT INTO servers VALUES(?, ?)", (id, name))
                newconn = sqlite3.connect(f"{id}.db")
                newcursor = newconn.cursor()
                newcursor.execute("""CREATE TABLE syllablecount (
                    lineone integer,
                    linetwo integer,
                    linethree integer
                )""")
                print("done")
            elif result is not None:
                print(result)

            conn.commit()
            conn.close()

def setup(bot):
    bot.add_cog(Events(bot))