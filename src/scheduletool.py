from discord.ext import commands


class ScheduleCategory(commands.Cog, name="schedule"):
    def __init__(self, bot, cur, conn):
        super().__init__()
        self.bot = bot
        self.cur = cur
        self.conn = conn
