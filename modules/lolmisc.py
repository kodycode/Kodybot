import discord
from discord.ext import commands

class Misc:

    def __init__(self, bot):
        self.bot = bot
        self.avatar = ''

    @commands.group(pass_context=True, description='Displays miscellaneous commands.')
    async def misc(self, ctx):
        if (ctx.invoked_subcommand is None):
            await self.bot.say('Incorrect subcommand passed.')

    @misc.command(name='icon', description='Obtains image of summoner icon.')
    async def display_icon(self, summoner: str):
        self.avatar = 'https://avatar.leagueoflegends.com/NA/' + summoner + '.png'
        await self.bot.say(self.avatar)

def setup(bot):
    bot.add_cog(Misc(bot))
