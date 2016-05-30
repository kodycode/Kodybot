#Responsible for running the bot.

import requests
import discord
import logger
client = discord.Client()

async def get_Summoner_ID(region, summoner_name, API_key):
    URL = 'https://' + region + '.api.pvp.net/api/lol/' + region + '/v1.4/summoner/by-name/' + summoner_name + '?api_key=' + API_key
    response = requests.get(URL)
    print(URL)
    return response.json()

async def request_Ranked_Data(region, ID, API_key):

    URL = 'https://' + region + '.api.pvp.net/api/lol/' + region + '/v2.5/league/by-summoner/' + ID + '/entry?api_key=' + API_key
    response = requests.get(URL)
    print(URL)
    return response.json()

async def print_ranked_data(message, summoner_name):
    summoner = summoner_name.replace(' ', '')
    summoner = summoner.lower()
    
    region = 'na'       #Change to any other region if so desired
    
    API_key = 'Enter LoL API Key Here';
    #If you don't have one you can get one at https://developer.riotgames.com

    responseJSON = await get_Summoner_ID(region, summoner, API_key)

    ID = responseJSON[summoner]['id']
    ID = str(ID)          
    responseJSON2 = await request_Ranked_Data(region, ID, API_key)

    tier = responseJSON2[ID][0]['tier']
    division = responseJSON2[ID][0]['entries'][0]['division']
    lp = str(responseJSON2[ID][0]['entries'][0]['leaguePoints'])
    wins = str(responseJSON2[ID][0]['entries'][0]['wins'])
    losses = str(responseJSON2[ID][0]['entries'][0]['losses'])
                       
    await client.send_message(message.channel, summoner_name + '\n-------------\nTier: ' + tier + '\nDivison: '
                                + division + '\nLP: ' + lp + '\nWins: ' + wins + '\nLosses: ' + losses + '\n\n')

@client.async_event
async def on_message(message):
    #author = message.author
    if message.content.startswith('$exit'):
        client.logout()
        print('Bot has logged out')
    if message.content.startswith('$rank'):
        summoner_name = message.content[6:]
        
        try:
            await print_ranked_data(message, summoner_name)
        except KeyError:
            await client.send_message(message.channel, 'ERROR! No ranked stats found for this player')
            
client.run('Enter discord token/account information here')
client.connect()
