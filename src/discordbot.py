#!/usr/bin/env python3
import discord
import settings
TOKEN=settings.APIKEY
client=discord.Client()
@client.event
async def on_Ready():
    print("logined!")
client.run(TOKEN)