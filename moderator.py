import discord
from discord.ext import commands
import random
import time
import json
import asyncio

class mod():
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def kick(self, ctx, user: discord.User):
        """"""
        server = ctx.message.server
        if ctx.message.author.server_permissions.kick:
            await self.bot.kick(user)
            await self.bot.say("Kicked {}!".format(user))
        else:
            await self.bot.say("You dont have permission to use this command!")
    
    @commands.command(pass_context=True)
    async def ban(self, ctx, user: discord.User):
        """"""
        server = ctx.message.server
        if ctx.message.author.server_permissions.ban:
            await self.bot.ban(user)
            await self.bot.say("Banned {}!".format(user))
        else:
            await self.bot.say("You dont have permission to use this command!")
    
    @commands.command(pass_context=True)
    async def botpurge(self, ctx):
        """"""
        def is_me(m):
            return m.author == self.bot.user
        channel = ctx.message.channel
        deleted = await self.bot.purge_from(channel, limit=100, check=is_me)
        if ctx.message.author.server_permissions.manage_messages:
            try:
                await self.bot.send_message(channel, 'Deleted {} of my message(s)!'.format(len(deleted)))
            except:
                await self.bot.say("I was unable to delete My Messages!")
        else:
            await self.bot.say("You dont have permission to use this command!")
        
    @commands.command(pass_context=True)
    async def warn(self, ctx, user: discord.User, *, msg):
        """"""
        server = ctx.message.server
        if ctx.message.author.server_permissions.kick:
            author = ctx.message.author.id
            em = discord.Embed(color=0x000000)
            em.set_author(name='! Warning !')
            em.add_field(name="Moderator", value=("<@{}>".format(author)))
            em.add_field(name="Reason", value=(msg))
            em.add_field(name="Time", value=(time.ctime()))
            await self.bot.send_message(user, embed=em)
            await self.bot.say("Warned {}! :warning:".format(user))
        else:
            await self.bot.say("You dont have permission to use this command!")

    @commands.command(pass_context=True)
    async def setlog(self, ctx, channel=""):
        """"""
        server = ctx.message.server
        if ctx.message.author.server_permissions.administrator:
            if channel == "":
                await self.bot.say("Please choose a channel\n**Usage:** =setlog <channel_id>")
            else:
                s = open("log/{}.data".format(server.id), "w+")
                s.write("id = '{}'".format(channel))
                s.close()
                await self.bot.say("Data Saved!")

def setup(bot):
    bot.add_cog(mod(bot))
