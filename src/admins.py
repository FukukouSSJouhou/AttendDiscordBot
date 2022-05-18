from discord.ext import commands
def sqlite_register_user(userid,schoolnumber,cur2,conn2):
    query=u'''replace into \"userinfo\"
    (\"schoolnumber\",\"id\")
    values (?,?)
        '''
    cur2.execute(query,(schoolnumber,userid))
    conn2.commit()
class AdminCategory(commands.Cog,name="admin"):
    def __init__(self,bot,cur,conn):
        super().__init__()
        self.bot=bot
        self.cur=cur
        self.conn=conn
    @commands.command()
    async def registry(self,ctx, gakusekinumber):
        sqlite_register_user(int(ctx.author.id), int(gakusekinumber),self.cur,self.conn)
        await ctx.send("registred:" + gakusekinumber + " author: " + str(ctx.author.id))