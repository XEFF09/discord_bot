import discord as disc
from discord.ext import commands as cmds
import requests as req
import datetime as dt

class covid(cmds.Cog):
    #inheritance "Cog" means that will be considered as Cog

    def __init__(self, bot):
        #set the default of bot related to bot.py
        #bot : cmds.Bot = considered as Bot

        self.bot = bot

    @cmds.command()
    async def cov(self, ctx, name=None):
        #cov = method which is belong to class or object

        try:
            if name is None:
                box01 = disc.Embed(title='REMINDER: Name Required', colour=0xff0000)
                await ctx.send(embed=box01)

            else:
                url = f'https://disease.sh/v3/covid-19/countries/{name}'
                geturl = req.get(url)
                pydict = geturl.json()
                #cvt json into pydict

                country = pydict['country']
                updated = pydict['updated'] // 1000
                cases = pydict['cases']
                todayCases = pydict['todayCases']
                deaths = pydict['deaths']
                todayDeaths = pydict['todayDeaths']
                recovered = pydict['recovered']
                countryInfo = pydict['countryInfo']
                flag = countryInfo['flag']

                date = dt.datetime.fromtimestamp(updated).strftime('%Y-%m-%d')

                box02 = disc.Embed(title=f'COVID-19 in {country.upper()}', colour=0xff0000)
                box02.add_field(name='DATE:', value=f'> {date}', inline=True)
                box02.add_field(name='CASES:', value=f'> {cases}', inline=True)
                box02.add_field(name='T-CASES:', value=f'> {todayCases}', inline=True)
                box02.add_field(name='DEATHS:', value=f'> {deaths}', inline=True)
                box02.add_field(name='RECOV:', value=f'> {recovered}', inline=True)
                box02.add_field(name='T-DEATHS:', value=f'> {todayDeaths}', inline=True)

                box02.set_thumbnail(url=flag)
                await ctx.send(embed=box02)

        except:
            box03 = disc.Embed(title='ERROR', description=f'{name.upper()} IS NOT FOUND', colour=0xff0000)
            await ctx.send(embed=box03)

def setup(bot):
    #setup bot by...
    bot.add_cog(covid(bot))
    #add cog or covid(bot) into a Bot                                                                                         

