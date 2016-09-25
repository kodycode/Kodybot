import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import urllib.request

class OWStats:

    def __init__(self, bot):
        self.bot = bot
        self.battle_tag = ''
        self.skill_rating = 0
        self.rank = ''
        self.current_level = 0
        self.wins = 0
        self.total_wins = 0
        self.ranked_wins = 0
        self.losses = 0
        self.ranked_losses = 0
        self.win_percentage = 0
        self.ranked_win_percentage = 0
        self.time_played = 0
        self.ranked_time_played = 0
        self.top_heroes = []
        self.ranked_top_heroes = []
        self.top_hours = []
        self.ranked_top_hours = []
        self.html_source = ''

    @commands.group(pass_context = True)
    async def ow(self, ctx):
        if (ctx.invoked_subcommand is None):
            await self.bot.say('Incorrect random subcommand passed.')

    @ow.group(name='skill', pass_context=True)
    async def display_skill_rating(self, ctx, battle_tag : str):
        self.battle_tag = battle_tag.replace('#','-')
        self.URL = 'https://playoverwatch.com/en-us/career/pc/us/' + self.battle_tag
        self.battle_tag = self.battle_tag.replace('-','#')
        try:
            self.html_source = urllib.request.urlopen(self.URL)
            self.soup = BeautifulSoup(self.html_source, 'html.parser')

            await ctx.invoke(self.get_skill_rating)

            if (self.skill_rating == 0):
                await self.bot.say('No Skill Rating found for this player')
            else:
                await self.bot.say(self.battle_tag + ' has a skill rating of ' + str(self.skill_rating))
        except urllib.error.HTTPError as e:
            await self.bot.say('Error in finding data from battle tag ' + self.battle_tag
                             + '. Did you enter the correct battle tag?')

    @display_skill_rating.command(name='', hidden=True)
    async def get_skill_rating(self):
        try:
            skill = self.soup.find('div', {'class': 'competitive-rank'})
            rating = skill.find('div', {'class': 'u-align-center h6'})
            self.skill_rating = int(rating.text)

        except AttributeError as e:
            self.skill_rating = 'Skill Rating not found'

    @ow.group(name='rank', pass_context=True)
    async def display_rank(self, ctx, battle_tag : str):
        self.battle_tag = battle_tag.replace('#','-')
        self.URL = 'https://playoverwatch.com/en-us/career/pc/us/' + self.battle_tag
        self.battle_tag = self.battle_tag.replace('-','#')
        try:
            self.html_source = urllib.request.urlopen(self.URL)
            self.soup = BeautifulSoup(self.html_source, 'html.parser')

            await ctx.invoke(self.get_skill_rating)

            if (self.skill_rating == 0):
                await self.bot.say('No Rank found for this player')
            else:
                await ctx.invoke(self.get_rank)
                await self.bot.say(self.battle_tag + ' is ' + self.rank + ' rank. ')
        except urllib.error.HTTPError as e:
            await self.bot.say('Error in finding data from battle tag ' + self.battle_tag
                             + '. Did you enter the correct battle tag?')

    @display_rank.command(name='', hidden=True)
    async def get_rank(self):
        #Assumes there is a valid skill rating

        if ((1 <= self.skill_rating) and (self.skill_rating <= 1499)):
            self.rank = 'Bronze'
        elif ((1500 >= self.skill_rating) and (self.skill_rating <= 1999)):
            self.rank = 'Silver'
        elif ((2000 >= self.skill_rating) and (self.skill_rating <= 2499)):
            self.rank = 'Gold'
        elif ((2500 >= self.skill_rating) and (self.skill_rating <= 2999)):
            self.rank = 'Platinum'
        elif ((3000 >= self.skill_rating) and (self.skill_rating <= 3499)):
            self.rank = 'Diamond'
        elif ((3500 >= self.skill_rating) and (self.skill_rating <= 3999)):
            self.rank = 'Master'
        elif ((4000 >= self.skill_rating) and (self.skill_rating <= 5000)):
            self.rank = 'Grandmaster'
        else:
            self.rank = 'Top 500'

    @ow.group(name='wins', pass_context=True)
    async def display_wins(self, ctx, battle_tag : str):
        self.battle_tag = battle_tag.replace('#','-')
        self.URL = 'https://playoverwatch.com/en-us/career/pc/us/' + self.battle_tag
        self.battle_tag = self.battle_tag.replace('-','#')
        try:
            self.html_source = urllib.request.urlopen(self.URL)
            self.soup = BeautifulSoup(self.html_source, 'html.parser')

            await ctx.invoke(self.get_wins)
            await self.bot.say(self.battle_tag + ' has won ' + self.wins + ' games')
        except urllib.error.HTTPError as e:
            await self.bot.say('Error in finding data from battle tag ' + self.battle_tag
                             + '. Did you enter the correct battle tag?')

    @display_wins.command(name='get', hidden = True)
    async def get_wins(self):
        table = self.soup.find_all('table', {'class': 'data-table'})
        td = table[6].find_all('td')

        self.wins = td[1].text.replace(',','')

    @ow.group(name='twins', pass_context=True)
    async def display_total_wins(self, ctx, battle_tag : str):
        self.battle_tag = battle_tag.replace('#', '-')
        self.URL = 'https://playoverwatch.com/en-us/career/pc/us/' + self.battle_tag
        self.battle_tag = self.battle_tag.replace('-','#')
        try:
            self.html_source = urllib.request.urlopen(self.URL)
            self.soup = BeautifulSoup(self.html_source, 'html.parser')

            await ctx.invoke(self.get_total_wins)
            await self.bot.say(self.battle_tag + ' has won a total of ' + self.total_wins + ' games.')
        except urllib.error.HTTPError as e:
            await self.bot.say('Error in finding data from battle tag ' + self.battle_tag
                             + '. Did you enter the correct battle tag?')

    @display_total_wins.command(name='', hidden=True)
    async def get_total_wins(self):
        try:
            head = self.soup.find('p', {'class': 'masthead-detail h4'})
            self.total_wins = str(head.text).split()[0]

        except AttributeError as e:
            self.skill_rating = 'Total wins not found.'

    @ow.group(name='rwins', pass_context=True)
    async def display_ranked_wins(self, ctx, battle_tag : str):
        self.battle_tag = battle_tag.replace('#','-')
        self.URL = 'https://playoverwatch.com/en-us/career/pc/us/' + self.battle_tag
        self.battle_tag = self.battle_tag.replace('-','#')
        try:
            self.html_source = urllib.request.urlopen(self.URL)
            self.soup = BeautifulSoup(self.html_source, 'html.parser')

            await ctx.invoke(self.get_ranked_wins)
            await self.bot.say(self.battle_tag + ' has won ' + self.ranked_wins + ' ranked games')
        except urllib.error.HTTPError as e:
            await self.bot.say('Error in finding data from battle tag ' + self.battle_tag
                             + '. Did you enter the correct battle tag?')

    @display_ranked_wins.command(name='', hidden=True)
    async def get_ranked_wins(self):
        for competitive in self.soup.find('div', {'id': 'competitive-play'}):
            table = competitive.find_all('table', {'class': 'data-table'})

        td = table[6].find_all('td')

        self.ranked_wins = td[3].text.replace(',','')

    @ow.group(name='rlosses', pass_context=True)
    async def display_ranked_losses(self, ctx, battle_tag : str):
        self.battle_tag = battle_tag.replace('#','-')
        self.URL = 'https://playoverwatch.com/en-us/career/pc/us/' + self.battle_tag
        self.battle_tag = self.battle_tag.replace('-','#')
        try:
            self.html_source = urllib.request.urlopen(self.URL)
            self.soup = BeautifulSoup(self.html_source, 'html.parser')

            await ctx.invoke(self.get_ranked_losses)
            await self.bot.say(self.battle_tag + ' has lost ' + self.ranked_losses + ' ranked games')
        except urllib.error.HTTPError as e:
            await self.bot.say('Error in finding data from battle tag ' + self.battle_tag
                             + '. Did you enter the correct battle tag?')

    @display_ranked_losses.command(name='', hidden=True)
    async def get_ranked_losses(self):

        for competitive in self.soup.find('div', {'id': 'competitive-play'}):
            table = competitive.find_all('table', {'class': 'data-table'})

        td = table[6].find_all('td')

        self.ranked_losses = int(td[1].text.replace(',','')) - int(td[3].text.replace(',',''))
        self.ranked_losses = str(self.ranked_losses)

    @ow.group(name='rpercentage', pass_context=True)
    async def display_ranked_win_percentage(self, ctx, battle_tag : str):
        self.battle_tag = battle_tag.replace('#','-')
        self.URL = 'https://playoverwatch.com/en-us/career/pc/us/' + self.battle_tag
        self.battle_tag = self.battle_tag.replace('-','#')
        try:
            self.html_source = urllib.request.urlopen(self.URL)
            self.soup = BeautifulSoup(self.html_source, 'html.parser')

            await ctx.invoke(self.get_ranked_win_percentage)
            await self.bot.say(self.battle_tag + "'s win percentage is %.2f" % self.ranked_win_percentage + '%')
        except urllib.error.HTTPError as e:
            await self.bot.say('Error in finding data from battle tag ' + self.battle_tag
                             + '. Did you enter the correct battle tag?')

    @display_ranked_win_percentage.command(name='', hidden=True)
    async def get_ranked_win_percentage(self):
        for competitive in self.soup.find('div', {'id': 'competitive-play'}):
            table = competitive.find_all('table', {'class': 'data-table'})

        td = table[6].find_all('td')

        wins = int(td[3].text.replace(',',''))
        total_games = int(td[1].text.replace(',',''))

        self.ranked_win_percentage = (wins/total_games) * 100

    @ow.group(name='time', pass_context=True)
    async def display_time_played(self, ctx, battle_tag : str):
        self.battle_tag = battle_tag.replace('#','-')
        self.URL = 'https://playoverwatch.com/en-us/career/pc/us/' + self.battle_tag
        self.battle_tag = self.battle_tag.replace('-','#')
        try:
            self.html_source = urllib.request.urlopen(self.URL)
            self.soup = BeautifulSoup(self.html_source, 'html.parser')

            await ctx.invoke(self.get_time_played)
            await self.bot.say(self.battle_tag + ' has played quick play Overwatch for ' + self.time_played)
        except urllib.error.HTTPError as e:
            await self.bot.say('Error in finding data from battle tag ' + self.battle_tag
                             + '. Did you enter the correct battle tag?')

    @display_time_played.command(name='', hidden=True)
    async def get_time_played(self):
        table = self.soup.find_all('table', {'class': 'data-table'})
        td = table[6].find_all('td')

        #Checks if profile is still using score metrics
        if (len(td) == 12):
            #shouldn't(?) work anymore
            self.time_played = td[11].text
        else:
            self.time_played = td[7].text

    @ow.group(name='rtime', pass_context=True)
    async def display_ranked_time_played(self, ctx, battle_tag : str):
        self.battle_tag = battle_tag.replace('#','-')
        self.URL = 'https://playoverwatch.com/en-us/career/pc/us/' + self.battle_tag
        self.battle_tag = self.battle_tag.replace('-','#')
        try:
            self.html_source = urllib.request.urlopen(self.URL)
            self.soup = BeautifulSoup(self.html_source, 'html.parser')

            await ctx.invoke(self.get_ranked_time_played)
            await self.bot.say(self.battle_tag + ' has played competitive play Overwatch for ' + self.ranked_time_played)
        except urllib.error.HTTPError as e:
            await self.bot.say('Error in finding data from battle tag ' + self.battle_tag
                             + '. Did you enter the correct battle tag?')

    @display_ranked_time_played.command(name='', hidden=True)
    async def get_ranked_time_played(self):

        for competitive in self.soup.find('div', {'id': 'competitive-play'}):
            table = competitive.find_all('table', {'class': 'data-table'})

        td = table[6].find_all('td')

        #Checks if profile is still using score metrics
        if (len(td) == 12):
            self.ranked_time_played = td[11].text
        else:
            self.ranked_time_played = td[9].text

    @ow.group(name='ttime', pass_context=True)
    async def display_total_time_played(self, ctx, battle_tag : str):
        self.battle_tag = battle_tag.replace('#','-')
        self.URL = 'https://playoverwatch.com/en-us/career/pc/us/' + self.battle_tag
        self.battle_tag = self.battle_tag.replace('-','#')
        try:
            self.html_source = urllib.request.urlopen(self.URL)
            self.soup = BeautifulSoup(self.html_source, 'html.parser')

            await ctx.invoke(self.get_total_time_played)
            await self.bot.say(self.battle_tag + ' has played Overwatch for ' + self.total_time_played + ' hours overall')
        except urllib.error.HTTPError as e:
            await self.bot.say('Error in finding data from battle tag ' + self.battle_tag
                             + '. Did you enter the correct battle tag?')


    @display_total_time_played.command(name='', hidden=True)
    async def get_total_time_played(self):

        ### Quick Play Time
        table = self.soup.find_all('table', {'class': 'data-table'})
        td = table[6].find_all('td')

        #Checks if profile is still using score metrics
        if (len(td) == 12):
            #shouldn't(?) work anymore
            time_played1 = td[11].text.replace(' hours', '')
        else:
            time_played1 = td[7].text.replace(' hours', '')

        ### Competitive Play Time
        for competitive in self.soup.find('div', {'id': 'competitive-play'}):
            table = competitive.find_all('table', {'class': 'data-table'})

        td = table[6].find_all('td')

        #Checks if profile is still using score metrics
        if (len(td) == 12):
            time_played2 = td[11].text.replace(' hours', '')
        else:
            time_played2 = td[9].text.replace(' hours', '')

        self.total_time_played = str(int(time_played1) + int(time_played2))

    @ow.group(name='level', pass_context=True)
    async def display_level(self, ctx, battle_tag : str):
        self.battle_tag = battle_tag.replace('#','-')
        self.URL = 'https://playoverwatch.com/en-us/career/pc/us/' + self.battle_tag
        self.battle_tag = self.battle_tag.replace('-','#')
        try:
            self.html_source = urllib.request.urlopen(self.URL)
            self.soup = BeautifulSoup(self.html_source, 'html.parser')

            await ctx.invoke(self.get_level)
            if (self.current_level == 0):
                await self.bot.say('Level not found for ' + self.battle_tag)
            else:
                await self.bot.say(self.battle_tag + ' is level ' + self.current_level)
        except urllib.error.HTTPError as e:
            await self.bot.say('Error in finding data from battle tag ' + self.battle_tag
                             + '. Did you enter the correct battle tag?')

    @display_level.command(name='', hidden=True)
    async def get_level(self):
        current_level = self.soup.find('div', {'class': 'u-vertical-center'})

        self.current_level = str(current_level.text)

    @ow.group(name='topfive', pass_context=True)
    async def display_top_five_heroes(self, ctx, battle_tag : str):
        self.battle_tag = battle_tag.replace('#','-')
        self.URL = 'https://playoverwatch.com/en-us/career/pc/us/' + self.battle_tag
        self.battle_tag = self.battle_tag.replace('-','#')
        try:
            self.html_source = urllib.request.urlopen(self.URL)
            self.soup = BeautifulSoup(self.html_source, 'html.parser')

            await ctx.invoke(self.get_top_five_heroes)
            await ctx.invoke(self.get_top_five_heroes_hours)
            display = []
            display.append('Most played heroes for ' + self.battle_tag + ' are:')

            for h, t in zip(self.top_heroes, self.top_hours):
                display.append(h + ' - ' + t)

            await self.bot.say('\n'.join(map(str,display)))
        except urllib.error.HTTPError as e:
            await self.bot.say('Error in finding data from battle tag ' + self.battle_tag
                             + '. Did you enter the correct battle tag?')

    @display_top_five_heroes.command(name='', hidden=True)
    async def get_top_five_heroes(self):
        top_heroes = []
        count = 0
        for competitive in self.soup.find_all('div', {'id': 'quick-play'}):
            for bar in self.soup.find_all('div', {'class': 'bar-text'}):
                if (count == 5):
                    break

                for hero in bar.find_all('div', {'class': 'title'}):
                    top_heroes.append(hero.text)

                count = count+1

        self.top_heroes = top_heroes

    @display_top_five_heroes.command(name='', hidden=True)
    async def get_top_five_heroes_hours(self):
        top_hours = []
        count = 0
        for bar in self.soup.find_all('div', {'class': 'bar-text'}):
            if (count == 5):
                break

            for hours in bar.find_all('div', {'class': 'description'}):
                top_hours.append(hours.text)

            count = count+1
        self.top_hours = top_hours

    @ow.group(name='rtopfive', pass_context=True)
    async def display_ranked_top_five_heroes(self, ctx, battle_tag : str):
        self.battle_tag = battle_tag.replace('#','-')
        self.URL = 'https://playoverwatch.com/en-us/career/pc/us/' + self.battle_tag
        self.battle_tag = self.battle_tag.replace('-','#')
        try:
            self.html_source = urllib.request.urlopen(self.URL)
            self.soup = BeautifulSoup(self.html_source, 'html.parser')

            await ctx.invoke(self.get_ranked_top_five_heroes)
            await ctx.invoke(self.get_ranked_top_five_heroes_hours)

            display = []
            display.append('Most played heroes for ' + self.battle_tag + ' in competitive are:')
            for h, t in zip(self.ranked_top_heroes, self.ranked_top_hours):
                display.append(h + ' - ' + t)

            await self.bot.say('\n'.join(map(str,display)))
        except urllib.error.HTTPError as e:
            await self.bot.say('Error in finding data from battle tag ' + self.battle_tag
                             + '. Did you enter the correct battle tag?')

    @display_ranked_top_five_heroes.command(name='', hidden=True)
    async def get_ranked_top_five_heroes(self):
        count = 0
        for competitive in self.soup.find_all('div', {'id': 'competitive-play'}):
            for bar in competitive.find_all('div', {'class': 'bar-text'}):
                if (count == 5):
                    break

                for hero in bar.find_all('div', {'class': 'title'}):
                    self.ranked_top_heroes.append(hero.text)

                count = count + 1

    @display_ranked_top_five_heroes.command(name='', hidden=True)
    async def get_ranked_top_five_heroes_hours(self):
        count = 0

        for competitive in self.soup.find_all('div', {'id': 'competitive-play'}):
            for bar in competitive.find_all('div', {'class': 'bar-text'}):
                if (count == 5):
                    break

                for hours in bar.find_all('div', {'class': 'description'}):
                    self.ranked_top_hours.append(hours.text)

                count = count+1

    @ow.command(name='quick', pass_context=True)
    async def display_quick_info(self, ctx, battle_tag : str):
        self.battle_tag = battle_tag.replace('#','-')
        self.URL = 'https://playoverwatch.com/en-us/career/pc/us/' + self.battle_tag
        self.battle_tag = self.battle_tag.replace('-','#')
        try:
            self.html_source = urllib.request.urlopen(self.URL)
            self.soup = BeautifulSoup(self.html_source, 'html.parser')

            await ctx.invoke(self.get_level)
            await ctx.invoke(self.get_wins)
            await ctx.invoke(self.get_total_wins)
            await ctx.invoke(self.get_time_played)
            await ctx.invoke(self.get_total_time_played)

            display = []
            display.append(self.battle_tag)
            display.append('-----------------------')
            display.append('**Current Level:** ' + self.current_level)
            display.append('**Total Wins:** ' + self.total_wins)
            display.append('**Quick Wins:** ' + self.wins)
            display.append('**Total Time Played:** ' + self.total_time_played + ' hours')
            display.append('**Quick Time Played:** ' + self.time_played)
            await self.bot.say('\n'.join(map(str,display)))
        except urllib.error.HTTPError as e:
            await self.bot.say('Error in finding data from battle tag ' + self.battle_tag
                             + '. Did you enter the correct battle tag?')

    @ow.command(name='competitive', pass_context=True)
    async def display_ranked_info(self, ctx, battle_tag : str):
        self.battle_tag = battle_tag.replace('#','-')
        self.URL = 'https://playoverwatch.com/en-us/career/pc/us/' + self.battle_tag
        self.battle_tag = self.battle_tag.replace('-','#')
        try:
            self.html_source = urllib.request.urlopen(self.URL)
            self.soup = BeautifulSoup(self.html_source, 'html.parser')

            await ctx.invoke(self.get_skill_rating)
            await ctx.invoke(self.get_rank)
            await ctx.invoke(self.get_level)
            await ctx.invoke(self.get_ranked_wins)
            await ctx.invoke(self.get_total_wins)
            await ctx.invoke(self.get_ranked_losses)
            await ctx.invoke(self.get_ranked_win_percentage)
            await ctx.invoke(self.get_ranked_time_played)
            await ctx.invoke(self.get_total_time_played)

            display = []
            display.append(self.battle_tag)
            display.append('-----------------------')
            display.append('**Skill Rating:** ' + str(self.skill_rating))
            display.append('**Rank:** ' + self.rank)
            display.append('**Current Level:** ' + self.current_level)
            display.append('**Total Wins:** ' + self.total_wins)
            display.append('**Competitive Wins:** ' + self.ranked_wins)
            display.append('**Competitive: Losses:** ' + self.ranked_losses)
            display.append('**Win Percentage:** %.2f%%' % self.ranked_win_percentage)
            display.append('**Total Time Played:** ' + self.total_time_played + ' hours')
            display.append('**Competitive Time Played:** ' + self.ranked_time_played)
            await self.bot.say('\n'.join(map(str,display)))
        except urllib.error.HTTPError as e:
            await self.bot.say('Error in finding data from battle tag ' + self.battle_tag
                             + '. Did you enter the correct battle tag?')

def setup(bot):
    bot.add_cog(OWStats(bot))
