import discord
from discord.ext.commands import Bot
import logging
import config
import random
import sys, os, time
import checks
ok = True
import asyncio
start_time = time.time()
logging.basicConfig(level=logging.INFO) # Configurates the logger
logger = logging.getLogger('discord')
bot = Bot(command_prefix=config.PREFIX) # Sets the client and sets the prefix
startup_extensions = ["server", "games", "bump", "main", "db", "rvid", "google", "profile", "wiki", "moderator"]
bot.remove_command("help")
IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"
def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("\n>>> ").lower().strip()

def fcount(path):
    #Counts the number of files in a directory
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    return count

async def uptime():
    await client.wait_until_ready()
    global minutes
    minutes = 0
    global hour
    hour = 0
    while not client.is_closed:
        await asyncio.sleep(60)
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1

@bot.event
async def on_ready():
    users = len(set(bot.get_all_members()))
    servers = len(bot.servers)
    channels = len([c for c in bot.get_all_channels()])
    shards = ["1", "2", "3", "4"]
    game = "=help | {} Guilds | {} Users".format(servers, users)
    await bot.change_presence(game=discord.Game(type=1, url="https://twitch.tv/hegufefghghfcbugufb", name=game))
    clear_screen()
    if __name__ == "__main__":
        for extension in startup_extensions:
            try:
                bot.load_extension(extension)
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                print('Failed to load extension {}\n{}'.format(extension, exc))
    print("-=-=-=-=-=-=-=-\n"
          "Arty\n"
          "-=-=-=-=-=-=-=-\n")
    print("Servers  {}\n"
          "Channels {}\n"
          "Users    {}\n".format(servers, channels, users))
    print("\n"
          "URL : https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=-1".format(bot.user.id))
    print("\nServers:\n")
    s = 0
    serv = list(bot.servers)
    for x in range(len(bot.servers)):
        s += 1
        print('{} '.format(s)+  serv[x-1].name)
    em = discord.Embed(color=0x000000)
    em.set_author(name='Logged in!')
    em.add_field(name="Guilds", value=(servers))
    em.add_field(name="Users", value=(users))
    em.add_field(name="Channels", value=(channels))
    em.add_field(name="Commands", value=("{}+".format(len(bot.commands))))
    channel = bot.get_channel("436481697043709952")
    await bot.send_message(channel, embed=em)

@bot.event
async def on_member_join(member):
    msg = "Created/Updated Profile file for {}!".format(member)
    uf = open("users/{}.py".format(member), "w+")
    uf.write("server_joinned = '{}'\ntime_joinned = '{}'".format(member.server, time.ctime()))
    uf.close()
    channel = bot.get_channel("437836039432962069")
    await bot.send_message(channel, msg)

@checks.is_owner()
@bot.command(pass_context=True)
async def reload(ctx, *, cog):
    """"""
    try:
        bot.unload_extension(cog)
        bot.load_extension(cog)
        await bot.say(":ok_hand: ")
        print("The cog '{}' was reloaded".format(cog))
    except Exception as e:
        exc = ':x: {}: {}'.format(type(e).__name__, e)
        await bot.say(exc)

@checks.is_owner()
@bot.command(pass_context=True)
async def load(ctx, *, cog):
    """"""
    author = ctx.message.author
    print("[Command] {} (=load)".format(author))
    try:
        bot.load_extension(cog)
        await bot.say(":ok_hand: ")
        print("The cog '{}' was loaded".format(cog))
    except Exception as e:
        exc = ':x: {}: {}'.format(type(e).__name__, e)
        await bot.say(exc)


@bot.command(pass_context=True)
async def pcount(ctx):
    """"""
    import os
    users = len(set(bot.get_all_members()))
    path = r"users" #Read files in folder
    await bot.say("There are currently {}/{} Profiles Registered!".format(fcount(path), users))
@checks.is_owner()
@bot.command(pass_context=True)
async def unload(ctx, *, cog):
    """"""
    author = ctx.message.author
    print("[Command] {} (=unload)".format(author))
    try:
        bot.unload_extension(cog)
        await bot.say(":ok_hand: ")
        print("The cog '{}' was unloaded".format(cog))
    except Exception as e:
        exc = ':x: {}: {}'.format(type(e).__name__, e)
        await bot.say(exc)
        
@checks.is_owner()
@bot.command(pass_context=True)
async def game(ctx, type="-n", *, game=""):
    """"""
    author = ctx.message.author
    print("[Command] {} (=game {})".format(author, game))
    if type == "-n":
        await bot.change_presence(game=discord.Game(name=game))
        await bot.say("Done!")
    if type == "-s":
        stream_title = game
        streamer = "https://www.twitch.tv/ugfegfajgyfjgeyfg"
        game = discord.Game(type=1, url=streamer, name=stream_title)
        await bot.change_presence(game=game)
        await bot.say("Done!")
    if type == "-l":
        stream_title = game
        streamer = "https://www.twitch.tv/ugfegfajgyfjgeyfg"
        game = discord.Game(type=2,  name=stream_title)
        await bot.change_presence(game=game)
        await bot.say("Done!")
    if type == "-w":
        stream_title = game
        streamer = "https://www.twitch.tv/ugfegfajgyfjgeyfg"
        game = discord.Game(type=3, name=stream_title)
        await bot.change_presence(game=game)
        await bot.say("Done!")

@bot.command(pass_context=True)
async def info(ctx):
    """"""
    author = ctx.message.author
    print("[Command] {} (=info)".format(author))
    users = len(set(bot.get_all_members()))
    servers = len(bot.servers)
    channels = len([c for c in bot.get_all_channels()])
    em = discord.Embed(color=0x000000)
    em.set_author(name='Bot Info')
    em.add_field(name='ID', value=(bot.user.id))
    em.add_field(name='Language', value=("discord.py"))
    em.add_field(name='Guilds', value=(servers))
    em.add_field(name='Channels', value=(channels))
    em.add_field(name='Users', value=(users))
    path = r"users" #Read files in folder
    em.add_field(name='Profiles', value=("{}/{}".format(fcount(path), users)))
    em.add_field(name='Commands', value=("{}+".format(len(bot.commands))))
    em.add_field(name='Bot Owner', value=("<@391132891024850945>\n"
                                          "Artucuno#1898"))
    await bot.say(embed=em)

@bot.command(pass_context=True)
async def servers(ctx):
    """"""
    users = len(set(bot.get_all_members()))
    channels = len([c for c in bot.get_all_channels()])
    commands = len(bot.commands)
    author = ctx.message.author
    print("[Command] {} (=servers)".format(author))
    em = discord.Embed(color=0x000000)
    em.add_field(name='Servers\n', value=("{} Guilds\n{} Members\n{} Channels\n\n".format(len(bot.servers), users, channels)))
    s = 0
    serv = list(bot.servers)
    for x in range(len(bot.servers)):
        s += 1
        em.add_field(name='{}'.format(s), value=('   ' +  serv[x-1].name))
        em.set_thumbnail(url='https://cdn.discordapp.com/attachments/434636207159377921/437855331666755584/arty2.png')
    await bot.whisper(embed=em)

@bot.command(pass_context=True)
async def ema(ctx):
    """"""
    em = discord.Embed(color=0x000000)
    em.set_author(name="idk", icon="google.jpeg")
    await self.bot.say(embed=em)

@bot.command(pass_context=True)
async def help(ctx):
    """"""
    author = ctx.message.author
    print("[Command] {} (=help)".format(author))
    em = discord.Embed(color=0x000000)
    em.set_author(name="Arty's Commands")
    em.add_field(name='Music', value=("\n"

                                              "[randomvideo](.) Find a random song\n[play](.) Play a song\n[pause](.)  Pause the current song\n[resume](.)  Play the song from current spot\n[np](.)  Check the song position\n[queue](.)  Check the songs queued!\n"))

    em.add_field(name='User', value=("\n"

                                              "[profile](.) Check the profile of users!\n"
                                              "[profilereg](.)  Create a profile (Creates/Updates Auto)\n"
                                              "[pcount](.) Check how many profiles have been registed in Arty's Database!\n"
                                              "[avatar](.)  Find a user's avatar (Nitro Ready)"))

    em.add_field(name='Games/Fun', value=("\n"

                                              "[pizza](.)  Are You Hungry?\n[dice](.)  Roll the dice and try get `6`!\n[emoji](.)  Emojis everywhere!!!\n[say](.)  Hello?!?!?! (Does not work in DM!)\n[dog](.)  Find Cute Dog images!"))

    em.add_field(name='Server', value=("\n"
                                              "[server](.)  Check Server Statistics\n[bump](.)  Bump your server!"))

    em.add_field(name='Moderation', value=("\n"

                                              "[kick](.)  Kick a user\n[ban](.)  Ban a user\n[warn](.)  Warn a user"))

    em.add_field(name='Misc', value=("\n"
                                              "[help](.)  See Help\n[setperms](.)  Setup my server permissions!\n[info](.)  See Bot info\n[ping](.)  How fast am i running?!?!\n[contact](.)  Need some help?\n[google](.) Search Google for images maps and more!\n[wikipedia](.)  Search wikipedia for something?"))
    await bot.whisper(embed=em)
    em = discord.Embed(color=0x000000)
    em.add_field(name='Links', value=("\n"
                                              "[Website](https://artydiscordbot.github.io)**|**[Discord](https://discord.gg/JJ7vrKH)**|**[Invite](https://discordapp.com/oauth2/authorize?client_id=434618135203545098&scope=bot&permissions=-1) "))
    await bot.whisper(embed=em)
    await bot.say("You Have Mail! :mailbox_with_mail:")

@checks.is_owner()
@bot.command(pass_context=True)
async def hold(ctx):
    """"""
    author = ctx.message.author
    print("[Command] {} (=hold)".format(author))
    await bot.change_presence(game=discord.Game(name='Currently on hold!'))
    await bot.say("Now on hold!")
    await bot.say("Nobody will be able to use commands while on hold!")
    choice = user_choice()
    users = len(set(bot.get_all_members()))
    servers = len(bot.servers)
    channels = len([c for c in bot.get_all_channels()])
    shards = ["1", "2", "3", "4"]
    game = "=help | {} Guilds | {} Users".format(servers, users)
    await bot.say("Taken off hold!")
    await bot.change_presence(game=discord.Game(name=game))
@checks.is_owner()
@bot.command(pass_context=True)
async def gamec(ctx):
    """"""
    author = ctx.message.author
    print("[Command] {} (=gamec)".format(author))
    print("Choose a Game name")
    choice = user_choice()
    await bot.change_presence(game=discord.Game(name=choice))
    print("Done!")

@checks.is_owner()
@bot.command(pass_context=True)
async def ev(ctx, *, eva="await bot.say('Say Something!')"):
    """"""
    try:
        eval(eva)
        await bot.say(":ok_hand:")
    except Exception as e:
        exc = ':x: {}: {}'.format(type(e).__name__, e)
        await bot.say(exc)
        

@checks.is_owner()
@bot.command(pass_context=True)
async def cl(ctx, *, msg=""):
    """"""
    em = discord.Embed(color=0x000000)
    em.add_field(name='Changelog', value=("```diff\n"
                                          "{}\n"
                                          "```".format(msg)))
    em.set_footer(text="Want to recieve updates? use =contact and staff will get back to you!")
    channel = bot.get_channel("438196864781647872")
    await bot.send_message(channel, embed=em)
    
@bot.command(pass_context=True)
async def setperms(ctx, role="Arty Perms"):
    """"""
    server = ctx.message.server
    if ctx.message.author.server_permissions.administrator:
        await bot.whisper("**__Setting Up My Perms!__**\n"
                          "\n"
                          "Create a role called `Arty Perms` in your server\n"
                          "Move it to a position in **Server Settings > Roles**\n"
                          "\n"
                          "You dont have to move my Default Role (`Arty`)\n"
                          "\n"
                          "When you move the `Arty Perms` role it gives me Extra server permissions!")
                          
bot.run(config.token)
