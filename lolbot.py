#Responsible for running the bot.

import requests
import discord
import logger
import config
from modules.lolrank import LOLRank
from modules.lolmisc import misc
from modules.lolfantasy import LOLFantasy
client = discord.Client()

@client.async_event
async def on_ready():
    print('Logging in..')
    print('Successfully logged in!')

@client.async_event
async def on_message(message):

    if message.content.startswith('$avatar'):
        summoner_name = message.content[8:].replace(' ', '%20')

        avatar = misc(summoner_name)
        await avatar.get_avatar()
        await client.send_message(message.channel, avatar.avatar)
        
    if message.content.startswith('$rank'):
        summoner_name = message.content[6:]
        
        try:
            rank = LOLRank(summoner_name)
            await rank.get_ranked_data()

            rank.summoner = summoner_name
            await client.send_message(message.channel, rank.summoner + '\n-------------\nTier: ' + rank.tier + '\nDivison: '
                                    + rank.division + '\nLP: ' + rank.lp + '\nWins: ' + rank.wins + '\nLosses: ' + rank.losses + '\n\n')
        except KeyError:
            await client.send_message(message.channel, 'ERROR! No ranked stats found for this player')
            
    if message.content.startswith('$fantasy teams'):
        fantasyID = message.content[15:]
        
        team = LOLFantasy(fantasyID)
        await team.get_team_names()
        
        if not team.team_names:
            await client.send_message(message.channel, 'No teams found for Fantasy ID: ' + fantasyID)
        else:
            await client.send_message(message.channel, 'For Fantasy ID: ' + fantasyID + '\n' + '\n'.join(map(str,team.team_names)))

    if message.content.startswith('$fantasy summoners'):
        fantasyID = message.content[19:]

        summoner = LOLFantasy(fantasyID)
        await summoner.get_summoner_names()
        
        if not summoner.summoner_names:
            await client.send_message(message.channel, 'No players found for Fantasy ID: ' + fantasyID)
        else:
            await client.send_message(message.channel, 'For Fantasy ID: ' + fantasyID + '\n' + '\n'.join(map(str,summoner.summoner_names)))
            
#if you want to use email and password, enable below and disable client.run(config.token)
#client.run(config.email, config.password)
client.run(config.token)
