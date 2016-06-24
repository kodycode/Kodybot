from bs4 import BeautifulSoup
from selenium import webdriver
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

options = []
options.append('--load-images=false')

class LOLFantasy:

    def __init__(self, fantasyID):
        self.driver = webdriver.PhantomJS(executable_path=config.directory, service_args=options)
        self.driver.get('http://fantasy.na.lolesports.com/en-US/league/' + fantasyID)
        self.html_source = self.driver.page_source
        self.team_names = []
        self.summoner_names = []

    async def get_team_names(self):
        soup = BeautifulSoup(self.html_source, 'html.parser')
        
        for head in soup.find_all('div', {'class': 'homepage-middle-right'}):
            for team in head.find_all('div', {'class': 'team-name'}):
                self.team_names.append(team.text)
                
        self.driver.quit()

    async def get_summoner_names(self):
        soup = BeautifulSoup(self.html_source, 'html.parser')

        for head in soup.find_all('div', {'class': 'standings-list'}):
            for summoner in head.find_all('div', {'class': 'summoner-name'}):
                self.summoner_names.append(summoner.text)

        self.driver.quit()

    
