import discord
import json
from discord.ext import commands
from discord.ext.commands import Bot
import aiohttp
import asyncio
from aiohttp_requests import requests
from aiohttp import web
import schedule
import time
import datetime
now = datetime.datetime.now()

class Pending(commands.Cog):
    def __init__(self, client):
        self.client = client
        @client.command()
        async def pending(ctx):
            async with aiohttp.ClientSession() as session:
                async with session.get("https://www.speedrun.com/api/v1/runs?game=yd4ovvg1&status=new&max=9999") as resp:
                    data = await resp.json()
                    mcbeRuns = 1
                    for number in data['data']:
                        mcbeRuns+=1
                    print(mcbeRuns)
                    async with session.get("https://www.speedrun.com/api/v1/runs?game=v1po7r76&status=new&max=9999") as resp:
                        data1 = await resp.json()
                        ceRuns = 1
                        for number in data1['data']:
                            ceRuns+=1
                        print(ceRuns)
                        totalRuns = (mcbeRuns + ceRuns)
                        file = open("/home/murraym/Desktop/MCBE-Speedrunning/DailyRuns.csv", "a")
                        file.write(f"\n{datetime.datetime.now()},{totalRuns}")
                        file.close()
                        print("done")
                        await ctx.send ("written to csv file")
                
def setup(bot):
    bot.add_cog(Pending(bot))
