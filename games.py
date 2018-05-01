import discord
from discord.ext import commands
import random

class games():
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def pizza(self, ctx):
        """"""
        author = ctx.message.author
        print("[Command] {} (=pizza)".format(author))
        pizza = ["data/1.jpeg", "data/2.jpeg", "data/3.jpeg", "data/4.jpeg", "data/5.jpeg", "data/6.jpeg"]
        await self.bot.say("Here you go!")
        p = random.choice(pizza)
        if p == "data/1.jpeg":
            await self.bot.say("Pizza `1` of `6`")
        if p == "data/2.jpeg":
            await self.bot.say("Pizza `2` of `6`")
        if p == "data/3.jpeg":
            await self.bot.say("Pizza `3` of `6`")
        if p == "data/4.jpeg":
            await self.bot.say("Pizza `4` of `6`")
        if p == "data/5.jpeg":
            await self.bot.say("Pizza `5` of `6`")
        if p == "data/6.jpeg":
            await self.bot.say("Pizza `6` of `6`")
        await self.bot.upload(random.choice(pizza))
    @commands.command(pass_context=True)
    async def dice(self, ctx):
        """"""
        author = ctx.message.author
        print("[Command] {} (=load)".format(author))
        num = ["1", "2", "3", "4", "5", "6"]
        await self.bot.say("Rolling...")
        await self.bot.say(random.choice(num))

    @commands.command(pass_context=True)
    async def emoji(self, ctx, *, type=""):
        """"""
        author = ctx.message.author
        print("[Command] {} (=emoji)".format(author))
        nem = [":smile:", ":smiley:", ":cry:", ":shell:"]
        iem = ["data/em/thk.gif", "data/em/all.gif", "data/em/trump.gif", "data/em/love.gif", "data/em/love2.gif", "data/em/sad.gif", "data/em/spinning.gif", "data/em/thonk.gif"]
        if type == "":
            await self.bot.say("```\n"
                                                     "! ==== Emoji ==== !\n"
                                                     "\n"
                                                     "Usage : =emoji <type>\n"
                                                     "\n"
                                                     "Types:\n"
                                                     "1. normal\n"
                                                     "2. gif```")
        if type == "normal":
            author = ctx.message.author
            print("[Command] {} (=emoji normal)".format(author))
            await self.bot.say("Heres an Emoji!")
            await self.bot.say(random.choice(nem))
        if type == "gif":
            author = ctx.message.author
            print("[Command] {} (=load)".format(author))
            await self.bot.say("Heres an Emoji!")
            await self.bot.upload(random.choice(iem))

    @commands.command(pass_context=True)
    async def say(self, ctx, *, msg=""):
        """"""
        author = ctx.message.author.id
        message = ctx.message
        if msg == "":
            try:
                await self.bot.delete_message(message)
                await self.bot.say("<@{}> please enter something to say!\n**Usage:** `=say <msg>`".format(author))
            except:
                pass
        else:
            try:
                await self.bot.delete_message(message)
            except:
                pass
            await self.bot.say(msg)

    @commands.command(pass_context=True)
    async def customrole(self, ctx, member: discord.Member, *, role_name=""):
        """"""
        author = ctx.message.author
        print("[Command] {} (=avatar {} {})".format(author, member, role_name))
        role = await self.bot.create_role(author.server, name=role_name)
        await self.bot.add_roles(member, role)
        await self.bot.send_message(member, "Added role!")
    
    @commands.command(pass_context=True)
    async def avatar(self, ctx, member: discord.Member, nitro=""):
        """"""
        author = ctx.message.author
        if nitro == "":
            print("[Command] {} (=avatar {} {})".format(author, member, nitro))
            em = discord.Embed(color=0x000000)
            em.set_author(name="{}'s Avatar".format(member))
            em.set_image(url="https://cdn.discordapp.com/avatars/{}/{}.png?size=2048".format(member.id, member.avatar))
            em.set_footer(text="Have Nitro? use (=avatar -n)") 
            await self.bot.say(embed=em)
        if nitro == "-n":
            print("[Command] {} (=avatar {} {})".format(author, member, nitro))
            em = discord.Embed(color=0x000000)
            em.set_author(name="{}'s Avatar".format(member))
            em.set_image(url="https://cdn.discordapp.com/avatars/{}/{}.gif?size=2048".format(member.id, member.avatar))
            em.set_footer(text="Nitro") 
            await self.bot.say(embed=em)
    @commands.command(pass_context=True)
    async def dog(self, ctx):
        """"""
        dogim = ["data/dog/1.gif", "data/dog/2.gif", "data/dog/3.gif", "data/dog/4.gif", "data/dog/5.gif", "data/dog/6.gif", "data/dog/7.gif", "data/dog/8.gif", "data/dog/9.gif", "data/dog/10.gif", "data/dog/11.gif"]
        em = discord.Embed(color=0x000000)
        await self.bot.say(":dog: **Doggie** :dog:")
        await self.bot.upload(random.choice(dogim))
    
def setup(bot):
    bot.add_cog(games(bot))
