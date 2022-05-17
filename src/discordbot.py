#!/usr/bin/env python3
import discord
import settings
from discord.ext import commands
TOKEN=settings.APIKEY
bot = commands.Bot(command_prefix='/')
@bot.command()
async def attend(ctx):
    await ctx.send("attended!!")
bot.run(TOKEN)