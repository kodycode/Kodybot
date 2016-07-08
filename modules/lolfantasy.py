from discord.ext import commands
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

options = []
options.append('--load-images=false')

class LOLFantasy:
    
    def __init__(self, bot):
        self.bot = bot
        self.html_source = ''
        self.header = ''
        self.team_names = []
        self.summoner_names = []
        self.total_points = []
        self.wins = []
        self.ties = []
        self.losses = []
        self.fantasy_ID = ''

    @commands.group(pass_context=True)
    async def fantasy(self, ctx):
        if (ctx.invoked_subcommand is None):
            await self.bot.say('Incorrect subcommand passed.')

    @fantasy.group(name='teams', pass_context=True)
    async def display_team_names(self, ctx, ID : str):
        self.fantasy_ID = ID
        self.driver = webdriver.PhantomJS(executable_path=config.directory, service_args=options)
        self.driver.get('http://fantasy.na.lolesports.com/en-US/league/' + self.fantasy_ID)
        self.driver.implicitly_wait(5)
        self.html_source = self.driver.page_source
        self.soup = BeautifulSoup(self.html_source, 'html.parser')
        self.driver.quit()
            
        await ctx.invoke(self.get_team_names)
        if not self.team_names:
            await self.bot.say('No teams found for Fantasy ID: ' + self.fantasy_ID)
        else:
            await self.bot.say('For Fantasy ID: ' + self.fantasy_ID + '\n' + '\n'.join(map(str,self.team_names)))
        
    @display_team_names.command(name='', hidden=True)
    async def get_team_names(self):
        team_names = []
        for head in self.soup.find_all('div', {'class': 'homepage-middle-right'}):
            for team in head.find_all('div', {'class': 'team-name'}):
                team_names.append(team.text)

        self.team_names = team_names
                
    @fantasy.group(name='summoners', pass_context=True)
    async def display_summoner_names(self, ctx, ID : str):
        self.fantasy_ID = ID
        self.driver = webdriver.PhantomJS(executable_path=config.directory, service_args=options)
        self.driver.get('http://fantasy.na.lolesports.com/en-US/league/' + self.fantasy_ID)
        self.driver.implicitly_wait(5)
        self.html_source = self.driver.page_source
        self.soup = BeautifulSoup(self.html_source, 'html.parser')
        self.driver.quit()
            
        await ctx.invoke(self.get_summoner_names)
        if not self.summoner_names:
            await self.bot.say('No players found for Fantasy ID: ' + self.fantasy_ID)
        else:
            await self.bot.say('For Fantasy ID: ' + self.fantasy_ID + '\n' + '\n'.join(map(str,self.summoner_names)))

    @display_summoner_names.command(name='', hidden=True)
    async def get_summoner_names(self):
        summoner_names = []
            
        for head in self.soup.find_all('div', {'class': 'standings-list'}):
            for summoner in head.find_all('div', {'class': 'summoner-name'}):
                 summoner_names.append(summoner.text)
                 
        self.summoner_names = summoner_names

    @fantasy.command(name='', hidden=True)
    async def get_wins(self):
        team_wins = []
        for head in self.soup.find_all('div', {'class': 'wins'}):
            for wins in head.find('div', {'class': 'value'}):
                team_wins.append(wins)

        self.wins = team_wins

    @fantasy.command(name='', hidden=True)
    async def get_ties(self):
        team_ties = []
        for head in self.soup.find_all('div', {'class': 'ties'}):
            for ties in head.find('div', {'class': 'value'}):
                team_ties.append(ties)

        self.ties = team_ties

    @fantasy.command(name='', hidden=True)
    async def get_losses(self):
        team_losses = []
        for head in self.soup.find_all('div', {'class': 'losses'}):
            for losses in head.find('div', {'class': 'value'}):
                team_losses.append(losses)

        self.losses = team_losses

    @fantasy.command(name='', hidden=True)
    async def get_total_points(self):
        whole_numbers = []
        fraction_numbers = []
        total_points = []
        for head in self.soup.find_all('div', {'class': 'total-points'}):
            num = ''
            for whole in head.find('span', {'class': 'whole-part'}):
                whole_numbers.append(whole)
            
            for fraction in head.find('span', {'class': 'fraction-part'}):
                fraction_numbers.append(fraction)
        for w, f in zip(whole_numbers, fraction_numbers):
            total_points.append(w+f)
            
        self.total_points = total_points

    @fantasy.command(name='', hidden=True)
    async def get_header(self):
        self.header = self.soup.title.string

    @fantasy.command(name='league', pass_context=True)
    async def display_league(self, ctx, ID : str):
        self.fantasy_ID = ID
        self.driver = webdriver.PhantomJS(executable_path=config.directory, service_args=options)
        self.driver.get('http://fantasy.na.lolesports.com/en-US/league/' + self.fantasy_ID)
        self.driver.implicitly_wait(10)
        self.html_source = self.driver.page_source
        self.soup = BeautifulSoup(self.html_source, 'html.parser')
        self.driver.quit()

        await ctx.invoke(self.get_header)            
        await ctx.invoke(self.get_team_names)
        await ctx.invoke(self.get_summoner_names)
        await ctx.invoke(self.get_wins)
        await ctx.invoke(self.get_ties)
        await ctx.invoke(self.get_losses)
        await ctx.invoke(self.get_total_points)

        if not (self.header):
            await self.bot.say('Could not find the league name for Fantasy ID: ' + self.fantasy_ID)
        elif not (self.team_names):
            await self.bot.say('No teams found for Fantasy ID: ' + self.fantasy_ID)
        elif not (self.summoner_names):
            await self.bot.say('No summoners found for Fantasy ID: ' + self.fantasy_ID)
        elif not (self.wins):
            await self.bot.say('No wins found for Fantasy ID: ' + self.fantasy_ID)
        elif not (self.ties):
            await self.bot.say('No ties found for Fantasy ID: ' + self.fantasy_ID)
        elif not (self.losses):
            await self.bot.say('No losses found for Fantasy ID: ' + self.fantasy_ID)
        else:
            display = []
            rank = 1
            display.append(self.header)
            display.append('-----'*15)
            display.append('Rankings\t\t\t Summoners')
            display.append('-----'*15)
            for (s, n, w, t, l, p) in zip(self.summoner_names, self.team_names, self.wins, self.ties, self.losses, self.total_points):
                display.append(str(rank) + '\t\t\t\t\t\t\t' + s)
                display.append('  \t\t\t\t\t\t\t' + n)
                display.append('  \t\t\t\t\t\t\t' + w + 'W-' + t + 'T-' + l + 'L')
                display.append('  \t\t\t\t\t\t\t' + str(p) + '\n')
                rank += 1

            await self.bot.say('\n'.join(map(str,display)))    

def setup(bot):
    bot.add_cog(LOLFantasy(bot))

