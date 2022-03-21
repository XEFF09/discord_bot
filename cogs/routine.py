import discord as disc
import datetime as dt
from discord.ext import commands as cmds

dict = {
    "initiation_list": ["08:10", "08:30", "09:20", "10:10", "11:00", "11:50", "12:40", "13:30", "14:20", "15:10", "16:00", "16:50",
                        "17:40", "18:30", "19:20", "20:10"],
    "day_dict" : {
        "Monday":["โฮมรูม", "ชุมนุม", "ชีวะ", "ชีวะ", "คณิต(เพิ่ม)", "คณิต(เพิ่ม)", "พักกลางวัน", "อังกฤษ", "ไทย", "สาธารณะประโยชน์"],
        "Tuesday":["โฮมรูม", "ชีวะ", "ฟิสิกส์", "ฟิสิกส์", "English", "สังคม", "พักกลางวัน", "เหตุการณ์และโลกปัจจุบัน", "โฮมรูม", "บำเพ็ญประโยชน์"],
        "Wednesday":["โฮมรูม", "เคมี", "สังคม", "English", "คณิต(เพิ่มเติม)", "คณิต(เพิ่มเติม)", "พักกลางวัน", "ฟิสิกส์", "อังกฤษ", "โฮมรูมว่างมั้ง"],
        "Thursday":["โฮมรูม", "การงานอาชีพ", "ไทย", "ประวัติศาสตร์", "คณิต(พื้น)", "ศิลปะ", "พักกลางวัน", "การออกแบบและเทคโนโลยี", "การออกแบบและเทคโนโลยี", "โฮมรูม"],
        "Friday":["โฮมรูม", "วิทยาศาสตร์โลกและอวกาศ", "วิทยาศาสตร์โลกและอวกาศ", "คณิต(พื้น)", "แนะแนว", "สุขศึกษา", "พักกลางวัน", "เคมี", "เคมี", "ประชุม"],
        "Saturday":["โฮมรูม", "วิทยาศาสตร์โลกและอวกาศ", "วิทยาศาสตร์โลกและอวกาศ", "คณิต(พื้น)", "แนะแนว", "สุขศึกษา", "พักกลางวัน", "เคมี", "เคมี", "ประชุม"]
    } 
}

class routine(cmds.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cmds.command()
    async def yo(self, ctx):

        now = str(dt.datetime.now().strftime("%H:%M"))
        today = str(dt.datetime.today().strftime("%A"))
        initiation_list = dict['initiation_list']
        day_dict = dict['day_dict']

        def limit():
        
            for i in range(len(initiation_list)):
                print(i)
                if i >= 15:
                #ไอ้เหี้ยมัน max ที่15
                    return i
                elif now > initiation_list[i] and now < initiation_list[i + 1]:
                    return i
            
        x = limit()
        if today in day_dict and x < 15:
            box01 = disc.Embed(title=f"{day_dict[f'{today}'][x]} {initiation_list[x]} - {initiation_list[x + 1]}", colour=0xff0000)
            await ctx.send(embed=box01)
        else:
            box02 = disc.Embed(title='None In Shift', colour=0xff0000)
            await ctx.send(embed=box02)

def setup(bot):
    bot.add_cog(routine(bot))

                

            


