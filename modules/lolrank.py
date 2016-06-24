import requests
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

class LOLRank:
    def __init__(self, summoner_name):
        self.summoner = summoner_name.replace(' ', '')
        self.summoner = self.summoner.lower()
        self.tier = 'Bronze'
        self.divison = 'V'
        self.lp = '0'
        self.wins = 0
        self.losses = 0
    
    async def get_summoner_ID(self, region, summoner_name, lol_api_key):
        URL = 'https://' + region + '.api.pvp.net/api/lol/' + region + '/v1.4/summoner/by-name/' + summoner_name + '?api_key=' + lol_api_key
        response = requests.get(URL)
        
        return response.json()

    async def request_ranked_Data(self, region, ID, lol_api_key):

        URL = 'https://' + region + '.api.pvp.net/api/lol/' + region + '/v2.5/league/by-summoner/' + ID + '/entry?api_key=' + lol_api_key
        response = requests.get(URL)
        
        return response.json()

    async def get_ranked_data(self):

        responseJSON = await self.get_summoner_ID(config.region, self.summoner, config.lol_api_key)

        ID = responseJSON[self.summoner]['id']
        ID = str(ID)          
        responseJSON2 = await self.request_ranked_Data(config.region, ID, config.lol_api_key)

        self.tier = responseJSON2[ID][0]['tier']
        self.division = responseJSON2[ID][0]['entries'][0]['division']
        self.lp = str(responseJSON2[ID][0]['entries'][0]['leaguePoints'])
        self.wins = str(responseJSON2[ID][0]['entries'][0]['wins'])
        self.losses = str(responseJSON2[ID][0]['entries'][0]['losses'])                           
       
