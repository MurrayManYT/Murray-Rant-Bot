import discord
from discord.ext import commands
from discord.ext.commands import Bot

def channelcheck():
    if message.channel.id == 684787316489060422:
        pass

class Furry(commands.Cog):
    def __init__(self,client):
        self.client = client
        @client.command()
        async def test(ctx):
            await ctx.send("hello world")

        @client.command()
        async def hewwo(ctx):
            channelcheck
            await ctx.send("hewwo wowwd")
                
        @client.command()
        async def suicide(ctx):
            channelcheck
            await ctx.send("fucking kill me please help put me out of this misery fucking end my suffering please")
            
        @client.command()
        async def hewp(ctx):
            channelcheck
            await ctx.send("This is the Help Section of Fuwwy Muwway's Bot. Might be updated. Check github for updates (if muwway adds me to gihub that is uwu).\n```UwU is my prefix.\nUse UwU alongside my commands to trigger them, uwu.``` Might make a list of commands if Muwway is feewing cute uwu. Bye fow now fuwwy fwiends uwu.")
                
        @client.command()
        async def invite(ctx):
            channelcheck
            await ctx.send("Heres's my invite link: https://discord.com/api/oauth2/authorize?client_id=798553197652344872&permissions=0&scope=bot")

        @client.command(description = "we make youw wowds into fuwwy wowds uwu")
        async def owoify (ctx, *, message):
            channelcheck
            owoed = message.replace("r","w")
            owoedfull = owoed.replace("l","w")
            await ctx.send(owoedfull)

        @client.command()
        async def BritishOwOify(ctx,*,message):
            channelcheck
            owoed = message.replace("r","w")
            owoedfull = owoed.replace("l","w")
            brish = owoedfull.replace("th","v")
            britishify = brish.replace("t","'")
            await ctx.send(britishify)

def setup(bot):
    bot.add_cog(Furry(bot))
