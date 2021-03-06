from discord.ext import commands
from tabulate import tabulate

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='about',
                      aliases=['info'],
                      description="Posts info about the bot",
                      brief="Posts info about the bot",
                      help="Posts info about the bot")
    async def about(self, ctx):
        await ctx.send("```" + "Developed by: Josh#1373\nDiscord:      discord.gg/wDu5CAA\nPlease DM or @ Josh if you have any feedback/suggestions!" + "```")

    @commands.command(name='invite',
                      help='Posts the invite link for Lisabot',
                      brief='Posts the invite link for Lisabot',
                      description='Posts the invite link for Lisabot')
    async def invite(self, ctx):
        await ctx.send('LisaBot: https://lisabot.bandori.app')
    @commands.command(name='support',
                      brief='Posts kofi link')
    async def kofi(self, ctx):
        await ctx.send("If you'd like to support the hosting costs for Lisabot, you can do so by visiting https://ko-fi.com/lisabot")

    @commands.command(name='github',
                      brief='Posts github repo')
    async def github(self, ctx):
        await ctx.send("If you'd like to contribue to Lisabot or just learn more about the code, please visit https://github.com/Amexy/lisa-bot")

    @commands.command(name='suggest',
                      brief='Make a suggestion for Lisabot',
                      help='Sends a suggestion for Lisabot to Josh#1373')
    async def suggest(self, ctx, *suggestion):
        if suggestion:
            suggestionString = suggestion[0]
            for x in suggestion:
                if x == suggestionString:
                    continue
                suggestionString += " %s" % x
            channel = self.bot.get_channel(624799117213958144)
            await channel.send(str(ctx.message.author.name) + "#" + str(ctx.message.author.discriminator) + " | " + str(ctx.message.guild.name) + ": " + suggestionString)
            await ctx.send("Thanks for the suggestion {0.author.mention}!".format(ctx.message))
        else:
            await ctx.send('Please enter your suggestion')

def setup(bot):
    bot.add_cog(Misc(bot))