#!/usr/bin/env python3
import discord
import settings
import sqlite3
from admins import AdminCategory
from discord.ext import commands
TOKEN=settings.APIKEY
dbname = 'main.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS \"userinfo\" (\"schoolnumber\"	INTEGER NOT NULL UNIQUE,\"id\"	INTEGER NOT NULL UNIQUE,PRIMARY KEY(\"id\"))")
cur.execute("CREATE TABLE IF NOT EXISTS \"Calender\" (\"schoolnumber\" INTEGER  NOT NULL,\"date\" TEXT NOT NULL,\"time\" TEXT NOT NULL,\"fiscalyear\" INTEGER NOT NULL)")
bot = commands.Bot(command_prefix='/')
@bot.command()
async def attend(ctx):
    idkun=int(ctx.author.id)

    await ctx.send("attended!!")
@bot.command()
async def show(ctx):
    await ctx.send("show")
bot.add_cog(AdminCategory(bot=bot,cur=cur,conn=conn))
bot.run(TOKEN)
conn.close()