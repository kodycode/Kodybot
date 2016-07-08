import discord
from discord.ext import commands

class Misc:
    
    def __init__(self, bot):
        self.bot = bot
        self.avatar = ''

    @commands.group(name='icon')
    async def display_icon(self, summoner: str):
        self.avatar = 'https://avatar.leagueoflegends.com/NA/' + summoner + '.png'
        await self.bot.say(self.avatar)

def setup(bot):
    bot.add_cog(Misc(bot))
