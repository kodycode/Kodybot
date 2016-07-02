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
| $ow competitive [enter battle tag here] | displays level and COMPETITIVE wins, losses, win percentage, time played |
| $ow topfive [enter battle tag here] | displays top five heroes and hours spent on them |
| $ow rtopfive [enter battle tag here] | display COMPETITIVE top five heroes and hours spent on them |
| $ow wins [enter battle tag here] | displays number of wins |
| $ow rwins [enter battle tag here] | displays COMPETITIVE number of wins |
| $ow losses [enter battle tag here] | displays losses |
| $ow rlosses [enter battle tag here] | displays COMPETITIVE losses |
| $ow percentage [enter batle tag here] | displays win percentage |
| $ow rpercentage [enter batle tag here] | displays COMPETITIVE win percentage |
| $ow time [enter battle tag here] | displays time spent in game |
| $ow rtime [enter battle tag here] | displays time spent in COMPETITIVE game |
| $ow level [enter battle tag here] | displays overwatch level of player |

## Setting up
Enter the token credential inside config.py and it should be good to go. 

If you want to use the league api to get ranked stats or if you want to use lolfantasy, just enter the information
needed inside config.py also.

When using the lolfantasy module, you need to download PhantomJS, extract the zip, get the path to phantomjs.exe
and place it inside the directory variable in config.py.

## Goals
- Learn more Python to do more cooler things

- Improve coding structure

- Gather data about players from games they've played

- More to come in the future..

## Credits
FarzaTV (for using his code to create lolrank.py)
