from discord.ext import commands


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

        await ctx.send("attended!!" + str(idkun))
    @commands.command()
    async def show(self,ctx):
        await ctx.send("show")
