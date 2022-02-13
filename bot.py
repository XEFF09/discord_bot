import discord as disc
from discord.ext import commands as cmds
import os

bot = cmds.Bot(command_prefix='')
#cmds.Bot means that will be considered as disc Bot
token = 'บอกก็ได้'

@bot.event
#event = discord's method whis is a decorator/clothe
async def on_ready():
    #on_ready -> get_event -> back
    #async : proceed while loading
    print('{0.user} bot is now online'.format(bot))

for i in os.listdir(r'D:\vs_saves\discord_bot\cogs'):
    if i.endswith('.py'):

        try:
            i = f"cogs.{i.replace('.py', '')}"
            bot.load_extension(i)
            #loads every module

        except Exception as e:
            print(f'{i} cant be loaded')
            raise e

bot.run(token)




