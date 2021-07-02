from discord.ext import commands
import discord

class helpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #master help command
    @commands.command(invoke_wihoutcommand=True)
    async def help(self, ctx):
        em = discord.Embed(
            title = "aHaiku Bot Commands", 
            description = "Use 3help <command> to learn more about each command!",
            color = discord.Color.dark_blue()
        )

        em.add_field(
            name = "Moderation", 
            value = "`3sc`, \n `3ssy`",
        )

        em.add_field(
            name = "Haikus", 
            value = "`3rules`, \n `3arules`, \n `3rrules`", 
            inline = False
        )

        em.add_field(   
            name = "Search", 
            value = "`3example`, \n `3search`", 
            inline = False
        )

        channel = self.bot.get_channel(ctx.channel.id)
        await ctx.channel.send(embed = em)

    #moderation settings set channel command
    @commands.command(invoke_wihoutcommand=True)
    async def help_3sc(self, ctx):
        emc = discord.Embed(
            title = "3sc Info", 
            color = discord.Color.dark_gold()
        )

        emc.add_field(
            name = "Description",
            value = "Set and see the channel where the bot plays the haiku game",
            inline = False
        )

        emc.add_field(
            name = "Syntax",
            value = "`3sc` \n `3sc <channel name>`",
            inline = False
        )

        emc.add_field(
            name = "Example",
            value = "`The current channel is set to #haiku-wars.` \n `3sc #haiku-wars`",
            inline = False
        )
        channel = self.bot.get_channel(846889420220792842)
        await ctx.channel.send(embed=emc)


    #moderation syllables set syllables command
    @commands.command(invoke_wihoutcommand=True)
    async def help_3ssy(self, ctx):
        emc = discord.Embed(
            title = "3ssy Info", 
            color = discord.Color.dark_gold()
        )

        emc.add_field(
            name = "Description",
            value = "Set and see the syllables required per line",
            inline = False
        )

        emc.add_field(
            name = "Syntax",
            value = "`3ssy`, \n `3ssy <line1syllable line2syllable line3syllabe>`",
            inline = False
        )

        emc.add_field(
            name = "Example",
            value = "`5 7 5`, \n `3ssy 5 7 5`",
            inline = False
        )

        channel = self.bot.get_channel(846889420220792842)
        await ctx.channel.send(embed=emc)

    #haiku see rules command
    @commands.command(invoke_wihoutcommand=True)
    async def help_3rules(self, ctx):

        emc = discord.Embed(
            title = "3rules Info", 
            color = discord.Color.dark_magenta()
        )

        emc.add_field(
            name = "Description", 
            value = "Lists all the game rules", 
            inline=False
        )

        emc.add_field(
            name = "Syntax",
            value = "`3rules`",
            inline = False
        )

        emc.add_field(
            name = "Example", 
            value = "`3rules`", 
            inline=False
        )

        channel = self.bot.get_channel(846889420220792842)
        await ctx.channel.send(embed=emc)

    #haiku add rules command
    @commands.command(invoke_wihoutcommand=True)
    async def help_3arules(self, ctx):

        emc = discord.Embed(
            title = "3arules Info", 
            color = discord.Color.dark_magenta()
        )

        emc.add_field(
            name = "Description", 
            value = "Add a game rule", 
            inline=False
        )

        emc.add_field(
            name = "Syntax", 
            value = '`3arules <position of game rule> <" game rule ">`', 
            inline=False
        )

        emc.add_field(
            name = "Example", 
            value = '`3arules 3 "One person cant go twice in a row"`, \n  `3arules 5 "Each succesful written haiku is one point"`', 
            inline=False
        )

        channel = self.bot.get_channel(846889420220792842)
        await ctx.channel.send(embed=emc)

    #haiku see rules command
    @commands.command(invoke_wihoutcommand=True)
    async def help_3rrules(self, ctx):

        emc = discord.Embed(
            title = "3rules Info", 
            color = discord.Color.dark_magenta()
        )

        emc.add_field(
            name = "Description", 
            value = "Remove a game rule", 
            inline=False
        )

        emc.add_field(
            name = "Syntax", 
            value = '`3rules <position of game rule>`', 
            inline=False
        )

        emc.add_field(
            name = "Example", 
            value = '`3rrules 3`, \n  `3rrules 1`', 
            inline=False
        )

        channel = self.bot.get_channel(846889420220792842)
        await ctx.channel.send(embed=emc)

    #search searching haiku examples help command
    @commands.command(invoke_wihoutcommand=True)
    async def help_3example(self, ctx):

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
            value = "`3example`",
            inline = False
        )

        emc.add_field(
            name = "Example", 
            value = "`Example Haiku \n \n The sunset draws close, \n as the weather blooms, the bright \n orange leaves flutter down`", 
            inline=True
        )

        channel = self.bot.get_channel(846889420220792842)
        await ctx.channel.send(embed=emc)

    #search searching haiku with title and author
    @commands.command(invoke_wihoutcommand=True)
    async def help_3search(self, ctx):

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
            value = "`3search <'title of haiku'> ['name of author']`, \n `3search ['title of haiku'] <'name of author'>`, \n `3search <'title of haiku'> <'name of author'>`",
            inline = False
        )

        emc.add_field(
            name = "Example", 
            value = "`3search 'The Spring'`, \n `3search 'Matsuo Kinsaku'`, \n `3search 'This Autumn' 'Matsuo Kinsaku'`", 
            inline=True
        )

        channel = self.bot.get_channel(846889420220792842)
        await ctx.channel.send(embed=emc)

def setup(bot):
    bot.add_cog(helpCommands(bot))