import discord
from discord.ext import commands
from mytoken import TOKEN
import syllables

bot = commands.Bot(command_prefix="3")
bot.remove_command("help")

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))

@bot.listen('on_message')
async def message(message):
    if message.author == bot.user:
        return
        
    if message.content.startswith('3hello'):
        await message.channel.send('Hello!')

#master help command
@bot.group(invoke_wihoutcommand=True)
async def help(ctx):
    em = discord.Embed(
        title = "aHaiku Bot Commands", 
        description = "Use 3help <command> to learn more about each command!",
        color = discord.Color.dark_blue()
    )

    em.add_field(
        name = "Moderation", 
        value = "`3help_m`",
    )

    em.add_field(
        name = "Haikus", 
        value = "`3help_h`"
    )

    em.add_field(
        name = "Search", 
        value = "`3help_s`"
    )

    await ctx.channel.send(embed = em)

#moderation help command
@bot.command(invoke_wihoutcommand=True)
async def help_m(ctx):

    emc = discord.Embed(
        title = "Moderation", 
        description = "Admin stuff", 
        color = discord.Color.dark_magenta()
    )

    emc.add_field(
        name = "Settings Commands", 
        value = "`3sc`, `3c`, `3ssy`,`3sy`", 
        inline = False
    )

    await ctx.channel.send(embed=emc)

#moderation settings set channel command
@bot.command(invoke_wihoutcommand=True)
async def help_3sc(ctx):
    emc = discord.Embed(
        title = "3sc Info", 
        color = discord.Color.dark_gold()
    )

    emc.add_field(
        name = "Description",
        value = "Set channel where the bot plays the haiku game",
        inline = False
    )

    emc.add_field(
        name = "Syntax",
        value = "`3sc <channel name>`",
        inline = False
    )

    emc.add_field(
        name = "Example",
        value = "`3sc #haiku-wars`",
        inline = False
    )

    await ctx.channel.send(embed=emc)

#moderation settings see channel command
@bot.command(invoke_wihoutcommand=True)
async def help_3c(ctx):
    emc = discord.Embed(
        title = "3c Info", 
        color = discord.Color.dark_gold()
    )

    emc.add_field(
        name = "Description",
        value = "See channel where the bot plays the haiku game",
        inline = False
    )

    emc.add_field(
        name = "Syntax",
        value = "`3c`",
        inline = False
    )

    emc.add_field(
        name = "Example",
        value = "`3c`",
        inline = False
    )

    await ctx.channel.send(embed=emc)

#moderation syllables set syllables command
@bot.command(invoke_wihoutcommand=True)
async def help_3ssy(ctx):
    emc = discord.Embed(
        title = "3ssy Info", 
        color = discord.Color.dark_gold()
    )

    emc.add_field(
        name = "Description",
        value = "Set syllables required per line",
        inline = False
    )

    emc.add_field(
        name = "Syntax",
        value = "`3ssy <line1syllable line2syllable line3syllabe>`",
        inline = False
    )

    emc.add_field(
        name = "Example",
        value = "`3ssy 5 7 5`",
        inline = False
    )

    await ctx.channel.send(embed=emc)

#moderation syllables see syllables command
@bot.command(invoke_wihoutcommand=True)
async def help_3sy(ctx):
    emc = discord.Embed(
        title = "3sy Info", 
        color = discord.Color.dark_gold()
    )

    emc.add_field(
        name = "Description",
        value = "See the syllables required in the haiku",
        inline = False
    )

    emc.add_field(
        name = "Syntax",
        value = "`3sy`",
        inline = False
    )

    emc.add_field(
        name = "Example",
        value = "`3sy`",
        inline = False
    )

    await ctx.channel.send(embed=emc)

#haiku help command
@bot.command(invoke_wihoutcommand=True)
async def help_h(ctx):

    emc = discord.Embed(
        title = "Haiku Game", 
        description = "Setting rules for the haiku game", 
        color = discord.Color.dark_orange()
    )

    emc.add_field(
        name = "Commands", 
        value = "`3hr`, `3ahr`,`3rhr`", 
        inline=True
    )

    await ctx.channel.send(embed=emc)

#haiku see rules command
@bot.command(invoke_wihoutcommand=True)
async def help_3hr(ctx):

    emc = discord.Embed(
        title = "3hr Info", 
        color = discord.Color.dark_magenta()
    )

    emc.add_field(
        name = "Description", 
        value = "Lists all the game rules", 
        inline=False
    )

    emc.add_field(
        name = "Syntax",
        value = "`3hr`",
        inline = False
    )

    emc.add_field(
        name = "Example", 
        value = "`3hr`", 
        inline=True
    )

    await ctx.channel.send(embed=emc)

#haiku add rules command
@bot.command(invoke_wihoutcommand=True)
async def help_3ahr(ctx):

    emc = discord.Embed(
        title = "3ahr Info", 
        color = discord.Color.dark_magenta()
    )

    emc.add_field(
        name = "Description", 
        value = "Add a game rule", 
        inline=False
    )

    emc.add_field(
        name = "Syntax", 
        value = '`3hr <position of game rule> <" game rule ">`', 
        inline=False
    )

    emc.add_field(
        name = "Example", 
        value = '`3hr 3 "One person cant go twice in a row"` \n  `3hr 5 "Each succesful written haiku is one point"`', 
        inline=False
    )

    await ctx.channel.send(embed=emc)

#haiku see rules command
@bot.command(invoke_wihoutcommand=True)
async def help_3rhr(ctx):

    emc = discord.Embed(
        title = "3rhr Info", 
        color = discord.Color.dark_magenta()
    )

    emc.add_field(
        name = "Description", 
        value = "Remove a game rule", 
        inline=False
    )

    emc.add_field(
        name = "Syntax", 
        value = '`3hr <position of game rule>`', 
        inline=False
    )

    emc.add_field(
        name = "Example", 
        value = '`3hr 3` \n  `3hr 1`', 
        inline=False
    )

    await ctx.channel.send(embed=emc)

#search help command
@bot.command(invoke_wihoutcommand=True)
async def help_s(ctx):

    emc = discord.Embed(
        title = "Search", 
        description = "Search for haikus online", 
        color = discord.Color.dark_magenta()
    )

    emc.add_field(
        name = "Commands", 
        value = "`3hex`, `3sh`", 
        inline=True
    )

    await ctx.channel.send(embed=emc)

#search searching haiku examples help command
@bot.command(invoke_wihoutcommand=True)
async def help_3hex(ctx):

    emc = discord.Embed(
        title = "Haiku Example Info", 
        color = discord.Color.dark_magenta()
    )

    emc.add_field(
        name = "Description", 
        value = "Get a haiku example", 
        inline=False
    )

    emc.add_field(
        name = "Syntax",
        value = "`3hex`",
        inline = False
    )

    emc.add_field(
        name = "Example", 
        value = "`3hex`", 
        inline=True
    )

    await ctx.channel.send(embed=emc)

#search searching haiku with title and author
@bot.command(invoke_wihoutcommand=True)
async def help_3sh(ctx):

    emc = discord.Embed(
        title = "Search Haiku Info", 
        color = discord.Color.dark_magenta()
    )

    emc.add_field(
        name = "Description", 
        value = "Search haiku online by title or author", 
        inline=False
    )

    emc.add_field(
        name = "Syntax",
        value = "`3sh <'title of haiku'> ['name of author']`, \n `3sh ['title of haiku'] <'name of author'>`, \n `3sh <'title of haiku'> <'name of author'>`",
        inline = False
    )

    emc.add_field(
        name = "Example", 
        value = "`3sh 'The Spring'`, \n `3sh 'Matsuo Kinsaku'`, \n `3sh 'This Autumn' 'Matsuo Kinsaku'`", 
        inline=True
    )

    await ctx.channel.send(embed=emc)

@bot.command()
async def syl(ctx, *, s="word"):
    await ctx.channel.send("The syllable count for `" + s + "` is " + str(syllables.estimate(s)))

bot.run(TOKEN)