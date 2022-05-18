from discord.ext import commands
class AdminCategory(commands.Cog,name="admin"):
    def __init__(self,bot):
        super().__init__()
        self.bot=bot
        