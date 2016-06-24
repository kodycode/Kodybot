import discord
import requests

class Misc:
    def __init__(self, summoner):
        self.summoner = summoner

    async def get_avatar(self):
        self.avatar = 'https://avatar.leagueoflegends.com/NA/' + self.summoner + '.png'
        
    async def display_avatar(self, client, channel):
        await client.send_message(channel, self.avatar)
