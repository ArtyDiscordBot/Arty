import discord
from discord.ext import commands
import random

class server():
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def server(self, ctx, option=""):
        """"""
        author = ctx.message.author
        print("[Command] {} (=server)".format(author))
        server = ctx.message.server
        if option == "":
            await self.bot.say("```\n"
                               "=server [option]\n"
                               "\n"
                               "Commands:\n"
                               "name  name of your server\n"
                               "id   id of your server\n"
                               "region  region of your server\n"
                               "info  all your server info\n```")
        if option == "name":
            await self.bot.say(server.name)
        if option == "id":
            await self.bot.say(server.id)
        if option == "region":
            await self.bot.say(server.region)
        if option == "info":
            em = discord.Embed(color=0x000000)
            em.set_author(name='Server Info')
            em.add_field(name="Name", value=(server.name))
            em.add_field(name="ID", value=(server.id))
            em.add_field(name="Owner", value=(server.owner.mention))
            em.add_field(name="Region", value=(server.region))
            em.add_field(name="Member Count", value=(server.member_count))
            try:
                em.add_field(name="Description", value=(server.default_channel.topic))
            except:
                em.add_field(name="Description", value=("none"))
                em.add_field(name="ICON DOWNLOAD", value=("[here]({})".format(server.icon_url)))
                em.set_thumbnail(url=server.icon_url)
                await self.bot.say(embed=em)

    @commands.command(pass_context=True)
    async def serveremojis(self, ctx):
        """"""
        await self.bot.say("**Emojis for {}**\n{}".format(ctx.message.server.name, ctx.message.server.emojis))

    @commands.command(pass_context=True)
    async def serverroles(self, ctx):
        """"""
        await self.bot.say("**Roles for {}**\n{}".format(ctx.message.server.name, ctx.message.server.roles.name))

    @commands.command(pass_context=True)
    async def panic(self, ctx):
        author = ctx.message.author
        # await self.bot.create_role(author.server, name="PANIC ALARM!!!")
        # await self.bot.create_channel(author.server, name='arty_panic')

def setup(bot):
    bot.add_cog(server(bot))
