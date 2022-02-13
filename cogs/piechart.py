import matplotlib.pyplot as plt
import discord as disc
import requests as req
import matplotlib as mpl
import io
from discord.ext import commands as cmds

class piechart(cmds.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cmds.command()
    async def pie(self, ctx, name=None):
        try:
            if name is None:
                box01 = disc.Embed(title='Reminder: Name Required', colour=0xff0000)
                await ctx.send(embed=box01)

            else:
                url = f'https://disease.sh/v3/covid-19/countries/{name}'
                geturl = req.get(url)
                pydict = geturl.json()

                recovered = pydict['recovered']
                deaths = pydict['deaths']
                cases = pydict['cases']
                active = pydict['active']
                country = pydict['country']
                countryInfo = pydict['countryInfo']
                flag = countryInfo['flag']
                
                types = ['RECOV', 'DEATHS', 'ACTIVE']
                data = [recovered, deaths, active]
                clr = ['#6d904f' ,'#fc4f30', '#008fd5']

                fp = mpl.font_manager.FontProperties(size=12)

                part, word, num = plt.pie(data, labels=types, autopct='%2.1f%%', colors=clr, shadow=True)
                plt.setp(word+num,fontproperties=fp,color='#FFFFFF')
                plt.legend(loc='upper left')
                plt.savefig('D:\png01\piechart.png', transparent=True)

                with open('D:\png01\piechart.png', 'rb') as f:
                    file = io.BytesIO(f.read())

                img = disc.File(file, filename='piechart.png')
                box02 = disc.Embed(title='> PieChart อัตราต่างๆ เมื่อเทียบกับคนติด', url=f'https://disease.sh/v3/covid-19/countries/{country}', colour=0xff0000)
                box02.set_thumbnail(url=flag)
                box02.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                box02.add_field(name='COUNTRY:', value=f'> {country}', inline=True)
                box02.add_field(name='รักษา / คนติด:', value=f'> ≈ {format((recovered * 100)/cases, ".2f")} %', inline=True)
                box02.add_field(name='เสียชีวิต / คนติด:', value=f'> ≈ {format((deaths * 100)/cases, ".2f")} %', inline=True)
                
                if active or cases != 0:
                    dc_result = (active * 100)/cases
                    box02.add_field(name='จำนวนผู้ที่กำลังเข้ารับการรักษา / จำนวนคนติด:', value=f'> ≈ {format(dc_result, ".2f")} %', inline=True)
                
                else:
                    box02.add_field(name='จำนวนผู้ที่กำลังเข้ารับการรักษา / จำนวนคนติด:', value='> There is no +Active :))', inline=True)

                await ctx.send(file=img, embed=box02)
                plt.close()

        except:
            box03 = disc.Embed(title='ERROR', description=f'{name.upper()} IS NOT FOUND', colour=0xff0000)
            await ctx.send(embed=box03)

def setup(bot):
    bot.add_cog(piechart(bot))  

