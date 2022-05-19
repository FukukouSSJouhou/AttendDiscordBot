from discord.ext import commands
import datetime
t_delta=datetime.timedelta(hours=9)
JST=datetime.timezone(t_delta,"JST")
nendo=2022
def isExistAttendCalam(schoolnumber,datekun,timekun,fiscalyear,cur2,conn2):
    '''
    isExistAttendCalam

    :param schoolnumber:school number
    :param datekun: date
    :param timekun: time
    :param fiscalyear: fiscalyear
    :param cur2: cursor
    :param conn2: connection?
    :return: boolkun
    '''
    query=u'''SELECT EXISTS(SELECT * FROM Calender WHERE 
    schoolnumber = ? AND 
    date = ? AND 
    time = ? AND
    fiscalyear = ?)
    
        '''
    for row in  cur2.execute(query,(schoolnumber,datekun,timekun,fiscalyear)):
        for r in row:
            if(r == 0):
                return False
            else:
                return True
def getSchoolNumber(userid,cur2):
    query=u'''SELECT schoolnumber FROM userinfo 
    WHERE id = ?
    '''
    for row in cur2.execute(query, (userid,)):
        return row[0]
    return 0
class ScheduleCategory(commands.Cog, name="schedule"):
    def __init__(self, bot, cur, conn,nendo):
        super().__init__()
        self.bot = bot
        self.cur = cur
        self.conn = conn
        self.nendo=nendo
    @commands.command()
    async def attend(self,ctx):
        idkun=int(ctx.author.id)
        schoolnumber=getSchoolNumber(idkun,self.cur)
        if schoolnumber == 0:
            await ctx.send("no registered!")
            return
        datekun=datetime.datetime.now(JST).strftime("%Y%m%d")
        timekun=datetime.datetime.now(JST).strftime("%H%M%S")
        if isExistAttendCalam(schoolnumber,datekun,timekun,nendo,self.cur,self.conn) == False:
            pass
        await ctx.send("attended!!" + str(schoolnumber))

    @commands.command()
    async def show(self,ctx):
        await ctx.send("show")
