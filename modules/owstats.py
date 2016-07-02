from bs4 import BeautifulSoup
import urllib.request

class OWStats:

    def __init__(self, battle_tag):
        self.battle_tag = battle_tag.replace('-','#')
        self.level = 0
        self.wins = 0
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
        self.URL = 'https://playoverwatch.com/en-us/career/pc/us/' + battle_tag
        self.html_source = urllib.request.urlopen(self.URL)
        self.soup = BeautifulSoup(self.html_source, 'html.parser')
        
    async def get_wins(self):     
        table = self.soup.find_all('table', {'class': 'data-table'})
        td = table[6].find_all('td')
        
        self.wins = td[1].text.replace(',','')

    async def display_wins(self, client, channel):
        await client.send_message(channel, self.battle_tag + ' has won ' + self.wins + ' games')

    async def get_ranked_wins(self):
         table = self.soup.find_all('table', {'class': 'data-table'})
         td = table[191].find_all('td')

         self.ranked_wins = td[1].text.replace(',','')

    async def display_ranked_wins(self, client, channel):
        await client.send_message(channel, self.battle_tag + ' has won ' + self.ranked_wins + ' ranked games')

    async def get_losses(self):
        table = self.soup.find_all('table', {'class': 'data-table'})
        td = table[6].find_all('td')
        
        self.losses = int(td[3].text.replace(',','')) - int(td[1].text.replace(',',''))
        self.losses = str(self.losses)

    async def display_losses(self, client, channel):
        await client.send_message(channel, self.battle_tag + ' has lost ' + self.losses + ' games')

    async def get_ranked_losses(self):
        table = self.soup.find_all('table', {'class': 'data-table'})
        td = table[191].find_all('td')

        self.ranked_losses = int(td[3].text.replace(',','')) - int(td[1].text.replace(',',''))
        self.ranked_losses = str(self.ranked_losses)
        print(self.ranked_losses)

    async def display_ranked_losses(self, client, channel):
        await client.send_message(channel, self.battle_tag + ' has lost ' + self.ranked_losses + ' ranked games')

    async def get_win_percentage(self):
        table = self.soup.find_all('table', {'class': 'data-table'})
        td = table[6].find_all('td')
        
        wins = int(td[1].text.replace(',',''))
        total_games = int(td[3].text.replace(',',''))
        
        self.win_percentage = (wins/total_games) * 100

    async def display_win_percentage(self, client, channel):
        await client.send_message(channel, self.battle_tag + "'s win percentage is %.2f" % self.win_percentage + '%')

    async def get_ranked_win_percentage(self):
        table = self.soup.find_all('table', {'class': 'data-table'})
        td = table[191].find_all('td')
        
        wins = int(td[1].text.replace(',',''))
        total_games = int(td[3].text.replace(',',''))
        
        self.ranked_win_percentage = (wins/total_games) * 100

    async def display_ranked_win_percentage(self, client, channel):
        await client.send_message(channel, self.battle_tag + "'s win percentage is %.2f" % self.ranked_win_percentage + '%')

    async def get_time_played(self):
        table = self.soup.find_all('table', {'class': 'data-table'})
        td = table[6].find_all('td')
        
        #Checks if profile is still using score metrics
        if (len(td) == 12):
            self.time_played = td[11].text
        else:
            self.time_played = td[9].text

    async def display_time_played(self, client, channel):
        await client.send_message(channel, self.battle_tag + ' has played quick play Overwatch for ' + self.time_played)

    async def get_ranked_time_played(self):
        table = self.soup.find_all('table', {'class': 'data-table'})
        td = table[191].find_all('td')
        
        #Checks if profile is still using score metrics
        if (len(td) == 12):
            self.ranked_time_played = td[11].text
        else:
            self.ranked_time_played = td[9].text

    async def display_ranked_time_played(self, client, channel):
        await client.send_message(channel, self.battle_tag + ' has played competitive play Overwatch for ' + self.ranked_time_played)

    #async def display_total_time_played(self, client, channel):
        #await client.send_message(channel, self.battle_tag + ' has played Overwatch for ' + self.ranked_time_played

    async def get_level(self):
        level = self.soup.find('div', {'class': 'u-vertical-center'})
        
        prestige1 = self.soup.find('div', {'style': 'background-image:url(https://' +
                                     'blzgdapipro-a.akamaihd.net/game/playerlevelrewards/0x025000000000092B_Rank.png)'})
        prestige2 = self.soup.find('div', {'style': 'background-image:url(https://' +
                                      'blzgdapipro-a.akamaihd.net/game/playerlevelrewards/0x0250000000000951_Rank.png)'})
        prestige3 = self.soup.find('div', {'style': 'background-image:url(https://' +
                                      'blzgdapipro-a.akamaihd.net/game/playerlevelrewards/0x0250000000000952_Rank.png)'})
        prestige4 = self.soup.find('div', {'style': 'background-image:url(https://' +
                                      'blzgdapipro-a.akamaihd.net/game/playerlevelrewards/0x0250000000000953_Rank.png)'})
        prestige5 = self.soup.find('div', {'style': 'background-image:url(https://' +
                                      'blzgdapipro-a.akamaihd.net/game/playerlevelrewards/0x0250000000000954_Rank.png)'})

        if (prestige1):
            self.level = str(int(level.text) + int(100))
        elif (prestige2):
            self.level = str(int(level.text) + int(200))
        elif (prestige3):
            self.level = str(int(level.text) + int(300))
        elif (prestige4):
            self.level = str(int(level.text) + int(400))
        elif (prestige5):
            self.level = str(int(level.text) + int(500))
        else:
            self.level = str(level.text)

    async def display_level(self, client, channel):
        if (self.level == 0):
            await client.send_message(channel, 'Level not found for ' + self.battle_tag)
        else:
            await client.send_message(channel, self.battle_tag + ' is level ' + self.level)

    async def get_top_five_heroes(self):
        count = 0
        for competitive in self.soup.find_all('div', {'id': 'quick-play'}):
            for bar in self.soup.find_all('div', {'class': 'bar-text'}):
                if (count == 5):
                    break
            
                for hero in bar.find_all('div', {'class': 'title'}):
                    self.top_heroes.append(hero.text)
                
                count = count+1

    async def get_ranked_top_five_heroes(self):
        count = 0
        
        for competitive in self.soup.find_all('div', {'id': 'competitive-play'}):
            for bar in competitive.find_all('div', {'class': 'bar-text'}):
                if (count == 5):
                    break
                
                for hero in bar.find_all('div', {'class': 'title'}):
                    self.ranked_top_heroes.append(hero.text)

                count = count + 1
        

    async def get_top_five_heroes_hours(self):
        count = 0
        
        for bar in self.soup.find_all('div', {'class': 'bar-text'}):
            if (count == 5):
                break
            
            for hours in bar.find_all('div', {'class': 'description'}):
                self.top_hours.append(hours.text)
                
            count = count+1

    async def get_ranked_top_five_heroes_hours(self):
        count = 0

        for competitive in self.soup.find_all('div', {'id': 'competitive-play'}):
            for bar in competitive.find_all('div', {'class': 'bar-text'}):
                if (count == 5):
                    break
            
                for hours in bar.find_all('div', {'class': 'description'}):
                    self.ranked_top_hours.append(hours.text)
                
                count = count+1

    async def display_top_five_heroes(self, client, channel):
        display = []
        display.append('Most played heroes for ' + self.battle_tag + ' are:')

        for h, t in zip(self.top_heroes, self.top_hours):
            display.append(h + ' - ' + t)
        
        await client.send_message(channel, '\n'.join(map(str,display)))

    async def display_ranked_top_five_heroes(self, client, channel):
        display = []
        display.append('Most played heroes for ' + self.battle_tag + ' in competitive are:')

        for h, t in zip(self.ranked_top_heroes, self.ranked_top_hours):
            display.append(h + ' - ' + t)
        
        await client.send_message(channel, '\n'.join(map(str,display)))
            
    async def display_quick_info(self, client, channel):
        display = []
        display.append(self.battle_tag)
        display.append('-----------------------')
        display.append('Level: ' + self.level)
        display.append('Wins: ' + self.wins)
        display.append('Losses: ' + self.losses)
        display.append('Win Percentage: %.2f%%' % self.win_percentage)
        display.append('Time Played: ' + self.time_played)
        await client.send_message(channel, '\n'.join(map(str,display)))

    async def display_ranked_info(self, client, channel):
        display = []
        display.append(self.battle_tag)
        display.append('-----------------------')
        display.append('Level: ' + self.level)
        display.append('Wins: ' + self.ranked_wins)
        display.append('Losses: ' + self.ranked_losses)
        display.append('Win Percentage: %.2f%%' % self.ranked_win_percentage)
        display.append('Time Played: ' + self.ranked_time_played)
        await client.send_message(channel, '\n'.join(map(str,display)))

