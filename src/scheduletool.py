import discord
from discord.ext import commands
import datetime

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, "JST")
nendo = 2022


def isExistAttendCalam(schoolnumber, datekun, fiscalyear, cur2, conn2):
    '''
    isExistAttendCalam

    :param schoolnumber:school number
    :param datekun: date
    :param fiscalyear: fiscalyear
    :param cur2: cursor
    :param conn2: connection?
    :return: boolkun
    '''
    query = u'''SELECT EXISTS(SELECT * FROM Calender WHERE 
    schoolnumber = ? AND 
    date = ? AND 
    fiscalyear = ?)
    
        '''
    for row in cur2.execute(query, (schoolnumber, datekun, fiscalyear)):
        for r in row:
            if (r == 0):
                return False
            else:
                return True


def getSchoolNumber(userid, cur2):
    query = u'''SELECT schoolnumber FROM userinfo 
    WHERE id = ?
    '''
    for row in cur2.execute(query, (userid,)):
        return row[0]
    return 0

def getCalenders(datekun,cur2):
    query=u'''SELECT \"schoolnumber\",\"time\" from Calender
    WHERE date = ?
    '''
    kaesuhairetu=[]
    for row in cur2.execute(query,(datekun,)):
        kaesuhairetu.append([row[0],row[1]])
    return kaesuhairetu

class ScheduleCategory(commands.Cog, name="schedule"):
    def __init__(self, bot, cur, conn, nendo):
        super().__init__()
        self.bot = bot
        self.cur = cur
        self.conn = conn
        self.nendo = nendo

    def sql_add_Calender(self, schoolnumber, datekun, timekun, nendo):
        query = u'''INSERT INTO Calender (\"schoolnumber\",\"date\",\"time\",\"fiscalyear\")
        VALUES (?,?,?,?)
        '''
        self.cur.execute(query, (schoolnumber, datekun, timekun, nendo))
        self.conn.commit()
    @commands.command()
    async def attend(self, ctx):
        idkun = int(ctx.author.id)
        schoolnumber = getSchoolNumber(idkun, self.cur)
        if schoolnumber == 0:
            await ctx.send("no registered!")
            return
        datekun = datetime.datetime.now(JST).strftime("%Y%m%d")
        timekun = datetime.datetime.now(JST).strftime("%H%M%S")
        if isExistAttendCalam(schoolnumber, datekun, nendo, self.cur, self.conn) == False:
            self.sql_add_Calender(schoolnumber,datekun,timekun,nendo)
            await ctx.send(str(schoolnumber) + " is attended!!")
        else:
            await ctx.send("Already attended!")

    @commands.command()
    async def show(self, ctx):
        datekun = datetime.datetime.now(JST).strftime("%Y%m%d")
        calenders=getCalenders(datekun,self.cur)
        embed=discord.Embed(title=f"__** ????????????????????? **__", color=0x03f8fc,timestamp= ctx.message.created_at)

        for rowkun in calenders:
            embed.add_field(name=f'**{rowkun[0]}**',
                            value=f'> time:{rowkun[1]}',
                            inline=False)
        await ctx.send(embed=embed)
