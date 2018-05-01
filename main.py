import discord
from discord.ext import commands
import random
import time
import config
class main():
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """"""
        t1 = time.perf_counter()
        await self.bot.send_typing(ctx.message.channel)
        t2 = time.perf_counter()
        em = discord.Embed(color=0x000000)
        em.add_field(name='Ping', value=("\n[Pingtime:](https://artydiscordbot.github.io/index.html#info)\n"
                                                                                       "➠ {}ms".format(str(round((t2-t1)*30)))))
        em.set_thumbnail(url="https://raw.githubusercontent.com/ArtGames101/artgames101.github.io/master/status/img/online.gif")
        await self.bot.say(embed=em)
    @commands.command(pass_context=True)
    async def contact(self, ctx, *, m=""):
        """"""
        author = ctx.message.author
        authorid = ctx.message.author.id
        if m == "":
            await self.bot.say("Please enter something to send!")
        else:
            msg = "{} <@{}>:\n➠ {} ({})".format(author, authorid, m, time.ctime())
            channel = self.bot.get_channel(config.contactchannel)
            await self.bot.send_message(channel, msg)
            await self.bot.say("Sent Message! :e_mail: ")
        

def setup(bot):
    bot.add_cog(main(bot))
