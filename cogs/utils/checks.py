from discord.ext import commands
import discord.utils

def is_owner_check(message):
    x = message.author.id
    return str(message.author.id) == '636612845341245442'

def is_owner():
    return commands.check(lambda ctx: is_owner_check(ctx.message))