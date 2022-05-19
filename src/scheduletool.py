from discord.ext import commands

def isExistAttendCalam(schoolnumber,datekun,timekun,fiscalyear,cur2,conn2):
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
        await ctx.send("attended!!" + str(schoolnumber))

    @commands.command()
    async def show(self,ctx):
        await ctx.send("show")
