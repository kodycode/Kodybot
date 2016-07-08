#Responsible for running the bot.

from discord.ext import commands
import discord
import logger
import config

initial_extensions = [
    'modules.lolrank',
    'modules.lolmisc',
    'modules.owstats'
]

if (config.enable_fantasy == True):
    initial_extensions.append('modules.lolfantasy')

bot = commands.Bot(command_prefix='$', description='')

@bot.async_event
async def on_ready():
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))
            
    print('Logging in..')
    print('Successfully logged in!')

@bot.event
async def on_message(message):
    await bot.process_commands(message)

bot.run(config.token)
