import discord
from discord.ext import commands
import random
import time

class profile():
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def profile(self, ctx, *, user=""):
        """"""
        if user == "":
            await self.bot.say(":x: Please enter a username!")
        else:
            try:
                await self.bot.say("**{}'s Profile Data**\n"
                                                         "all data is logged in .py file(s)\n\n".format(user))
                await self.bot.upload("users/{}.py".format(user))
            except Exception as e:
                await self.bot.say(":x: The User you have entered does not exist in our servers! :x: \n"
                                                         "\n   :x:Please Make sure you have not mentioned the user! :x:\n"
                                                          "\n                   Usage: `=profile MrBackPack#5852`")
    @commands.command(pass_context=True)
    async def profilereg(self, ctx):
        """"""
        server = ctx.message.server
        author = ctx.message.author
        p = open("users/{}.py".format(author), "w+")
        p.write("server_joinned = '{}'\ntime_joinned = '{}'".format(server, time.ctime()))
        p.close()
        await self.bot.whisper("Profile Created/Updated!\n"
                               "\n"
                               "**Note:** Your Profile is automatically Created/Updated when you join a server!") 
def setup(bot):
    bot.add_cog(profile(bot))
