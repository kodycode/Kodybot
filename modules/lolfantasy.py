from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

options = []
options.append('--load-images=false')

class LOLFantasy:

    def __init__(self, fantasyID):
        self.fantasyID = fantasyID
        self.driver = webdriver.PhantomJS(executable_path=config.directory, service_args=options)
        self.driver.get('http://fantasy.na.lolesports.com/en-US/league/' + fantasyID)
        self.html_source = self.driver.page_source
        self.team_names = []
        self.summoner_names = []
        self.total_points = []
        self.wins = []
        self.ties = []
        self.losses = []

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_all_elements_located)
        self.driver.quit()

    async def get_team_names(self):
        soup = BeautifulSoup(self.html_source, 'html.parser')
        
        for head in soup.find_all('div', {'class': 'homepage-middle-right'}):
            for team in head.find_all('div', {'class': 'team-name'}):
                self.team_names.append(team.text)

    async def display_team_names(self, client, channel):
        if not self.team_names:
            await client.send_message(channel, 'No teams found for Fantasy ID: ' + self.fantasyID)
        else:
            await client.send_message(channel, 'For Fantasy ID: ' + self.fantasyID + '\n' + '\n'.join(map(str,self.team_names)))

    async def get_summoner_names(self):
        soup = BeautifulSoup(self.html_source, 'html.parser')

        for head in soup.find_all('div', {'class': 'standings-list'}):
            for summoner in head.find_all('div', {'class': 'summoner-name'}):
                self.summoner_names.append(summoner.text)

    async def display_summoner_names(self, client, channel):
        if not self.summoner_names:
            await client.send_message(channel, 'No players found for Fantasy ID: ' + self.fantasyID)
        else:
            await client.send_message(channel, 'For Fantasy ID: ' + self.fantasyID + '\n' + '\n'.join(map(str,self.summoner_names)))

    async def get_wins(self):
        soup = BeautifulSoup(self.html_source, 'html.parser')

        for head in soup.find_all('div', {'class': 'wins'}):
            for wins in head.find('div', {'class': 'value'}):
                self.wins.append(wins)

    async def get_ties(self):
        soup = BeautifulSoup(self.html_source, 'html.parser')

        for head in soup.find_all('div', {'class': 'ties'}):
            for ties in head.find('div', {'class': 'value'}):
                self.ties.append(ties)

    async def get_losses(self):
        soup = BeautifulSoup(self.html_source, 'html.parser')

        for head in soup.find_all('div', {'class': 'losses'}):
            for losses in head.find('div', {'class': 'value'}):
                self.losses.append(losses)

    async def get_total_points(self):
        soup = BeautifulSoup(self.html_source, 'html.parser')
        whole_numbers = []
        fraction_numbers = []
        for head in soup.find_all('div', {'class': 'total-points'}):
            num = ''
            for whole in head.find('span', {'class': 'whole-part'}):
                whole_numbers.append(whole)
            
            for fraction in head.find('span', {'class': 'fraction-part'}):
                fraction_numbers.append(fraction)
        for w, f in zip(whole_numbers, fraction_numbers):
            self.total_points.append(w+f)

    async def display_league(self, client, channel):
        if not (self.team_names):
            await client.send_message(channel, 'No teams found for Fantasy ID: ' + self.fantasyID)
        elif not (self.summoner_names):
            await client.send_message(channel, 'No summoners found for Fantasy ID: ' + self.fantasyID)
        elif not (self.wins):
            await client.send_message(channel, 'No wins found for Fantasy ID: ' + self.fantasyID)
        elif not (self.ties):
            await client.send_message(channel, 'No ties found for Fantasy ID: ' + self.fantasyID)
        elif not (self.losses):
            await client.send_message(channel, 'No losses found for Fantasy ID: ' + self.fantasyID)
        else:
            display = []
            rank = 1
            display.append('Rankings\t\t\t Summoners')
            display.append('-----'*20)
            for (s, n, w, t, l, p) in zip(self.summoner_names, self.team_names, self.wins, self.ties, self.losses, self.total_points):
                display.append(str(rank) + '\t\t\t\t\t\t\t' + s) #+ '\t\t\t\t\t\t\t' + s.ljust(20,'-') + t + '----' +
                               #str(p) + '\n')
                display.append('  \t\t\t\t\t\t\t' + n)
                display.append('  \t\t\t\t\t\t\t' + w + 'W-' + t + 'T-' + l + 'L')
                display.append('  \t\t\t\t\t\t\t' + str(p) + '\n')
                rank += 1

            await client.send_message(channel, '\n'.join(map(str,display)))        
