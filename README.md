# LoLDiscordBot
A WIP Discord Bot for League of Legends created using Python 3.5 along with the API Wrapper written by Rapptz.

## Requirements
* Python 3.5+

* discord.py from https://github.com/Rapptz/discord.py

* ```requests``` library

## Features
As of right now, this bot only has the ability to return the ranked stats of a given player using $rank.

For example, if you type "$rank -summoner name here-" into the discord chat the results:
```
-Summoner Name Here-
--------------------
Tier: -tier here-
Division: -division here-
LP: -# of LP here-
Wins: -# of wins here-
Losses: -# of losses here-
```

## Usage
If you wish to use a separate account to run the bot, then you can just fill in the email, password, LoL API Key, and
region inside. You must also enable the client to use the email and password in lolbot.py and disable it from using
the token. (By default, the bot will use the token. I'll probably make this more user-friendly in the near future.)

If not, then you can just enter the Token, LoL API Key, and region inside config.py.

Once you're done either of the above, then you can just run the .bat file and it should be good to go.

## Goals
- Learn more Python to do more cooler things

- Improve coding structure

- Implement LoL Fantasy commands that returns certain stats, teams w/l ratio, etc.

- More to come in the future..

## Credits
FarzaTV (for using his code to create lolrank.py)
