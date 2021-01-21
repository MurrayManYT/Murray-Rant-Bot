import discord
from discord.ext import commands
import aiohttp

client = commands.Bot(command_prefix=['=',"!","-","_","#","~"])

@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"cog {extension} successfully loaded")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"cog {extension} successfully unloaded")
    
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    time.sleep(5)
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"cog {extension} successfully reloaded")
    
@client.command(aliases = ["runs","r"],description="sends the number of runs that are awaiting verification in mcbe")
async def rons(ctx):
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
                await ctx.send(f"{totalRuns} awaiting verification")

client.run("bot token")
