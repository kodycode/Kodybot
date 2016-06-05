import discord
import requests

class misc:
    def __init__(self, summoner):
        self.summoner = summoner

    async def get_avatar(self):
        self.avatar = 'https://avatar.leagueoflegends.com/NA/' + self.summoner + '.png'
