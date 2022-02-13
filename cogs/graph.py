import discord as disc
from discord.ext import commands as cmds
import io
import requests as req
import matplotlib.pyplot as plt
import datetime as dt

class graph(cmds.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cmds.command()
    async def gph(self, ctx, name1=None, name2=None, name3=None, name4=None):
        try:
            if name1 and name2 and name3 and name4 is None:
                box01 = disc.Embed(title='REMINDER: 4 Params Needed', colour=0xff0000)
                await ctx.send(embed=box01)

            else:
                url1 = f'https://disease.sh/v3/covid-19/countries/{name1}'
                url2 = f'https://disease.sh/v3/covid-19/countries/{name2}'
                url3 = f'https://disease.sh/v3/covid-19/countries/{name3}'
                url4 = f'https://disease.sh/v3/covid-19/countries/{name4}'

                clist = [url1, url2, url3, url4]
                cname = []
                ccases = []
                recov = []
                cinfo = []

                for i in clist:
                    geturl = req.get(i)
                    pydict = geturl.json()
                    
                    recovered = pydict['recovered']
                    cases = pydict['cases']
                    updated = pydict['updated'] // 1000
                    country = pydict['country']
                    cname.append(country)
                    ccases.append(cases)
                    recov.append(recovered)

                    if recovered and cases != None:
                        cal = ((recovered * 100) / cases)
                        cinfo.append(cal)

                date = dt.datetime.fromtimestamp(updated).strftime('%Y-%m-%d')
                
                plt.style.use('ggplot')
                plt.bar(cname, cinfo)
                plt.xlabel('COUNTRIES')
                plt.ylabel('RECOV %')
                plt.savefig('D:\png01\graph.png', transparent=True)

                with open('D:\png01\graph.png', 'rb') as f:
                    #read binary stuff
                    file = io.BytesIO(f.read())
                    #to mimic a file

                img = disc.File(file, filename='graph.png')
                box02 = disc.Embed(title='> Comparision of RECOVRATE in 4 Sample Countries', colour=0xff0000)
                box02.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

                recovrate = []

                for i in cinfo:
                    i = format(i, ".2f")
                    i = i + " %"
                    recovrate.append(i)

                box02.add_field(name='DATE:', value=f'> {date}', inline=True)
                box02.add_field(name='RECOV:', value=f'> {recov}', inline=True)
                box02.add_field(name='CASES:', value=f'> {ccases}', inline=True)
                box02.add_field(name='COUNTRIES:', value=f'> {cname}', inline=False)
                box02.add_field(name='RECOVRATE:', value=f'> {recovrate}', inline=False)
                box02.set_image(url='attachment://graph.png')

                await ctx.send(file=img, embed=box02)
                plt.close()
        
        except:
            box03 = disc.Embed(title='ERROR', description='NOT FOUND', colour=0xff0000)
            await ctx.send(embed=box03)

def setup(bot):
    bot.add_cog(graph(bot))











