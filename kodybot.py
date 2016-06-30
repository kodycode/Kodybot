#Responsible for running the bot.

import requests
import discord
import logger
import config
from modules.lolrank import LOLRank
from modules.lolfantasy import LOLFantasy
from modules.lolmisc import Misc
from modules.owstats import OWStats
client = discord.Client()

@client.async_event
async def on_ready():
    print('Logging in..')
    print('Successfully logged in!')

@client.async_event
async def on_message(message):

    if message.content.startswith('$help'):
        await client.send_message(message.channel,'Current commands are:\n' +
                                  '```$avatar [enter summoner name here] - ' +
                                  'displays summoner icon used in league of legends\n' +
                                  '$rank [enter summoner here] - ' +
                                  'displays rank, tier, division, wins/losses of player\n' +
                                  '$fantasy teams [enter fantasy league ID here] - ' +
                                  'displays teams that exist in fantasy league\n' +
                                  '$fantasy summoners [enter fantasy league ID here] - ' +
                                  'displays players that exist in fantasy league```' +
                                  '$fantasy league [enter fantasy league ID here] - ' +
                                  'displays rankings, players, teams, wins-ties-loss, total points')

    if message.content.startswith('$avatar'):
        summoner_name = message.content[8:].replace(' ', '%20')

        avatar = Misc(summoner_name)
        await avatar.get_avatar()
        await avatar.display_avatar(client, message.channel)
        
    if message.content.startswith('$rank'):
        summoner_name = message.content[6:]
        
        try:
            rank = LOLRank(summoner_name)
            await rank.get_ranked_data()
            rank.summoner = summoner_name
            
            await rank.display_ranked_data(client, message.channel)
        except KeyError:
            await client.send_message(message.channel, 'ERROR! No ranked stats found for this player')
            
    if message.content.startswith('$fantasy teams'):
        fantasyID = message.content[15:].replace (' ', '')
        
        team = LOLFantasy(fantasyID)
        await team.get_team_names()
        await team.display_team_names(client, message.channel)
        
    if message.content.startswith('$fantasy summoners'):
        fantasyID = message.content[19:].replace(' ', '')

        summoner = LOLFantasy(fantasyID)
        await summoner.get_summoner_names()
        await summoner.display_summoner_names(client, message.channel)

    if message.content.startswith('$fantasy league'):
        fantasyID = message.content[15:].replace(' ', '')

        table = LOLFantasy(fantasyID)
        await table.get_summoner_names()
        await table.get_team_names()
        await table.get_total_points()
        await table.get_wins()
        await table.get_ties()
        await table.get_losses()
        await table.display_league(client, message.channel)

    if message.content.startswith('$ow level'):
        battle_tag = message.content[10:].replace('#', '-')

        level = OWStats(battle_tag)
        await level.get_level()
        await level.display_level(client, message.channel)
        
            
#if you want to use email and password, enable below and disable client.run(config.token)
#client.run(config.email, config.password)
client.run(config.token)
