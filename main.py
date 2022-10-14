import discord, asyncio, syllables, os, logging, sys
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
import cogs.funcs
from cogs.database.database import engine
from cogs.database import models

load_dotenv(find_dotenv())

TOKEN = os.environ.get('TOKEN')

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='3', intents=intents, help_command=None)

handler = logging.StreamHandler(sys.stdout)
discord.utils.setup_logging(handler=handler)
models.Base.metadata.create_all(bind=engine)

extensions = ['cogs.helpCommands',
              'cogs.haikuCommands',
              'cogs.searchCommands',
              'cogs.events',
              'cogs.gameCommands',
              'cogs.adminCommands']

async def load_extensions():
    for ext in extensions:
        await bot.load_extension(ext)

async def main():
    await load_extensions()
    await bot.start(TOKEN)

asyncio.run(main())