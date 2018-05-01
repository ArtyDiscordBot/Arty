import discord
from discord.ext import commands
import random

class rvid():
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def randomvideo(self, ctx, *, vtype=""):
        """"""
        mv = ["[Spinning Monkeys](https://www.youtube.com/watch?v=mWo3woi9Uro)\nTaken from [dead4now.xyz](https://dead4now.xyz)", "[Sneaky Snitch](https://www.youtube.com/watch?v=4CRr7S5wvQw)\nTaken from [dead4now.xyz](https://dead4now.xyz)", "[Ice Flow](https://www.youtube.com/watch?v=a91IpbxjCxk)\nTaken from [dead4now.xyz](https://dead4now.xyz)"]
        if vtype == "":
            em = discord.Embed(color=0x000000)
            em.set_author(name='Random Video')
            em.add_field(name="Usage", value=("`=randomvideo <vtype>`"))
            await self.bot.say(embed=em)
        if vtype == "music":
            em = discord.Embed(color=0x000000)
            em.set_author(name='Music Video')
            em.add_field(name="\a", value=(random.choice(mv)))
            await self.bot.say(embed=em)
            
            
def setup(bot):
    bot.add_cog(rvid(bot))
