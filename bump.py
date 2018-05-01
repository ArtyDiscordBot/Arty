import discord
from discord.ext import commands
import random
import config

class bump():
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def bump(self, ctx):
        """Bump your server"""
        
        try:
            server = ctx.message.server
            channel = self.bot.get_channel(config.bumpchannel)
            em = discord.Embed(color=0x000000)
            em.add_field(name='\a', value=("[{}]({})\n"
                                           "> Join [Here]({})\n"
                                           "**Users** : {}\n"
                                           "Owner : [{}](.)\n"
                                           "\n"
                                           "> [{}](.)".format(server.name, await self.bot.create_invite(server), await self.bot.create_invite(server), server.member_count, server.owner, server.default_channel.topic)))
            em.set_thumbnail(url=server.icon_url)
            await self.bot.send_message(channel, embed=em)
            em = discord.Embed(color=0x000000)
            em.add_field(name='Bumped!', value=("Your server was bumped!\n"
                                            "> [Server Invite](https://discord.gg/HhT52fn)"))
            await self.bot.say(embed=em)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            em = discord.Embed(color=0x000000)
            em.add_field(name='Opps! :x:', value=("Opps! Something went wrong! but we will bump your server anyway just maybe without invite or description!\n\nError : `{}`".format(exc)))
            await self.bot.say(embed=em)
            try:
                server = ctx.message.server
                channel = self.bot.get_channel(config.bumpchannel)
                em = discord.Embed(color=0x000000)
                em.add_field(name='\a', value=("[{}](.)\n"
                                           "> Join :x:\n"
                                           "**Users** : {}\n"
                                           "Owner : [{}](.)\n"
                                           "\n"
                                           "> [{}](.)".format(server.name, server.member_count, server.owner, server.default_channel.topic)))
                em.set_thumbnail(url=server.icon_url)
                await self.bot.send_message(channel, embed=em)
                em = discord.Embed(color=0x000000)
                em.add_field(name='Bumped!', value=("Your server was bumped!\n"
                                                "> [Server Invite](https://discord.gg/HhT52fn)"))
                await self.bot.say(embed=em)
            except:
                try:
                    server = ctx.message.server
                    channel = self.bot.get_channel(config.bumpchannel)
                    em = discord.Embed(color=0x000000)
                    em.add_field(name='\a', value=("[{}]({})\n"
                                               "> Join [here]({})\n"
                                               "**Users** : {}\n"
                                               "Owner : [{}](.)\n"
                                               "\n"
                                               "> [:x:](.)".format(server.name, await self.bot.create_invite(server), await self.bot.create_invite(server), server.member_count, server.owner, server.default_channel.topic)))
                    em.set_thumbnail(url=server.icon_url)
                    await self.bot.send_message(channel, embed=em)
                    em = discord.Embed(color=0x000000)
                    em.add_field(name='Bumped!', value=("Your server was bumped!\n"
                                                    "> [Server Invite](https://discord.gg/HhT52fn)"))
                    await self.bot.say(embed=em)
                except:
                    try:
                        server = ctx.message.server
                        channel = self.bot.get_channel(config.bumpchannel)
                        em = discord.Embed(color=0x000000)
                        em.add_field(name='\a', value=("[{}](.)\n"
                                                   "> Join :x:\n"
                                                   "**Users** : {}\n"
                                                   "Owner : [{}](.)\n"
                                                   "\n"
                                                   "> [ :x: ](.)".format(server.name, server.member_count, server.owner)))
                        em.set_thumbnail(url=server.icon_url)
                        await self.bot.send_message(channel, embed=em)
                        em = discord.Embed(color=0x000000)
                        em.add_field(name='Bumped!', value=("Your server was bumped!\n"
                                                        "> [Server Invite](https://discord.gg/HhT52fn)"))
                        await self.bot.say(embed=em)
                    except:
                        await self.bot.say(":x: Opps! You may be in DM's or this may be a bug please contact the Pikachu Staff for help!")

def setup(bot):
    bot.add_cog(bump(bot))
