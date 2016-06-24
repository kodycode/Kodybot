# LoLDiscordBot
A WIP Discord Bot for League of Legends created using Python 3.5 along with the API Wrapper written by Rapptz.

## Requirements
* Python 3.5+

* discord.py from https://github.com/Rapptz/discord.py
 
* ```requests``` package
 
* ```selenium``` package
 
* ```beautifulsoup4``` package
 
* PhantomJS

## Commands
| Commands      | Output        |
| ------------- |:-------------:|
| $avatar [enter summoner name here]      | displays summoner icon used in league of legends |
| $rank [enter summoner here]      | displays rank, tier, division, wins/losses of player      |
| $fantasy teams [enter fantasy league ID here] | displays teams that exist in fantasy league      |
| $fantasy summoners [enter fantasy league ID here] | displays players that exist in fantasy league |


## Setting up
If you wish to use a separate account to run the bot, then you can just fill in the email, password, LoL API Key, and
region inside config.py. You must also enable the client to use the email and password in lolbot.py and disable it from using
the token. (By default, the bot will use the token. I'll probably make this more user-friendly in the near future.)

If you wish to use oauth2, then you can just enter the Token, LoL API Key, and region inside config.py.

When using the lolfantasy module, you need to download PhantomJS, extract the zip, get the path to phantomjs.exe
and place it inside the directory variable in config.py.

Once you're done either of the above, then you can just run the .bat file and it should be good to go.

## Goals
- Learn more Python to do more cooler things

- Improve coding structure

- Implement LoL Fantasy commands that returns certain stats, teams w/l ratio, etc.

- More to come in the future..

## Credits
FarzaTV (for using his code to create lolrank.py)
