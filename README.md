# Kodybot
A WIP Discord Bot using Python 3.5 along with the API Wrapper written by Rapptz.

## Requirements
* Python 3.5+

* discord.py from https://github.com/Rapptz/discord.py
 
* ```requests``` package
 
* ```beautifulsoup4``` package

* ```urllib3``` package


##### If you want to use the FantasyLCS commands

* ```selenium``` package 

* PhantomJS

## Commands


####League of Legends:
```You can get the fantasy league ID here when you go to your fantasy league page. When you look at the URL, there will be numbers displayed at the end (i.e http://fantasy.na.lolesports.com/en-US/league/[ID found here])```

| Commands      | Output        |
| ------------- |:-------------:|
| $help | displays available commands |
| $avatar [enter summoner name here]      | displays summoner icon used in league of legends |
| $rank [enter summoner here]      | displays rank, tier, division, wins/losses of player      |
| $fantasy league [enter fantasy league ID here] | displays rankings, players, teams, wins-ties-loss, total points|
| $fantasy teams [enter fantasy league ID here] | displays teams that exist in fantasy league      |
| $fantasy summoners [enter fantasy league ID here] | displays players that exist in fantasy league |

####Overwatch:
```Currently obtains PC player data only```

| Commands      | Output        |
| ------------- |:-------------:|
| $ow quick [enter battle tag here] | displays level, wins, losses, win percentage, time played |
| $ow topfive [enter battle tag here] | displays top five heroes and hours spent on them |
| $ow wins [enter battle tag here] | displays number of wins |
| $ow losses [enter battle tag here] | displays losses |
| $ow percentage [enter batle tag here] | displays win percentage |
| $ow time [enter battle tag here] | displays time spent in game |
| $ow level [enter battle tag here] | displays overwatch level of player |




## Setting up
If you wish to use a separate account to run the bot, then you can just fill in the email, password, LoL API Key, and
region inside config.py. You must also enable the client to use the email and password in lolbot.py and disable it from using
the token. (By default, the bot will use the token. I'll probably make this more user-friendly in the near future.)

If you wish to use oauth2, then you can just enter the Token, LoL API Key, and region inside config.py.

When using the lolfantasy module, you need to download PhantomJS, extract the zip, get the path to phantomjs.exe
and place it inside the directory variable in config.py.

## Goals
- Learn more Python to do more cooler things

- Improve coding structure

- Gather data about players from games they've played

- More to come in the future..

## Credits
FarzaTV (for using his code to create lolrank.py)
