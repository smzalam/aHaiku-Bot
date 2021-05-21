import discord
from main import bot
from discord.ext import commands

@bot.group(invoke_wihoutcommand=True)
async def help(ctx):
    em = discord.Embed(
        title = "aHaiku Bot Commands", 
        description = "Use 3help <command> to learn more about each command!",
        color = discord.Color.dark_theme()
    )

    em.add_field(
        name = "Moderation", 
        value = "3help_m",
    )

    em.add_field(
        name = "Haikus", 
        value = "3help_h"
    )

    em.add_field(
        name = "Search", 
        value = "3help_s"
    )

    await ctx.channel.send(embed = em)


@bot.command(invoke_wihoutcommand=True)
async def help_m(ctx):

    emc = discord.Embed(
        title = "Moderation", 
        description = "admin stuff", 
        color = discord.Color.dark_magenta()
    )

    emc.add_field(
        name = "Setings", 
        value = "setting channel settings", 
        inline=False
    )

    emc.add_field(
        name = "Syllables", 
        value = "Change Haiku Syllables", 
        inline=False
    )

    await ctx.channel.send(embed=emc)

bot.command(invoke_wihoutcommand=True)
async def help_h(ctx):

    emc = discord.Embed(
        title = "Haiku Game", 
        description = "Setting rules for the haiku game", 
        color = discord.Color.dark_orange()
    )

    emc.add_field(
        name = "Rules", 
        value = "see game rules" + "\n" + "3help_hr", 
        inline=False
    )

    emc.add_field(
        name = "Add Rule", 
        value = "add a rule" + "\n" + "3help_har", 
        inline=True
    )

    emc.add_field(
        name = "Remove Rule",
        value = "remove a role" + "\n" + "3help_hrr",
        inline = False
    )

    await ctx.channel.send(embed=emc)

bot.command(invoke_wihoutcommand=True)
async def help_s(ctx):

    emc = discord.Embed(
        title = "Search", 
        description = "search for haikus online", 
        color = discord.Color.dark_magenta()
    )

    emc.add_field(
        name = "Haiku Examples", 
        value = "get haiku examples from web " + "\n" + "3help_she", 
        inline=False
    )

    emc.add_field(
        name = "Author", 
        value = "get haiku by author name" + "\n" + "3help_shauthor", 
        inline=False
    )

    await ctx.channel.send(embed=emc)

@bot.command(invoke_wihoutcommand=True)
async def help_ch(ctx):

    emc = discord.Embed(
        title = "Channel Commands", 
        description = "Set channel, see set channel", 
        color = discord.Color.dark_magenta()
    )

    emc.add_field(
        name = "Set Channel", 
        value = "3!sch", 
        inline=True
    )

    emc.add_field(
        name = "See Set Channel", 
        value = "3sch", 
        inline=True
    )

    await ctx.channel.send(embed=emc)