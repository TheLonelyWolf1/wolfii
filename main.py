import discord
import discord.ext
from discord.ext import commands
import datetime
import asyncio
import random
from random import randint
import sys
import time

import Config
import SECRETS


bot = commands.Bot(command_prefix=Config.PREFIX, description=" ")
bot.remove_command(help)
token = SECRETS.TOKEN
bot_version = Config.VERSION

epoch = datetime.datetime.utcfromtimestamp(0)

title = "Happy Discord Hack Week!"


enemys =(
        "Demon goblin",
        "Demon viking",
        "Demon king",
        "Demon wolf",
        "")

result = (
        "He defeats his enemy with just one attack and is a now-proven hero of the empire!",
        "He defeats his enemy, but is so excausted, that he dies too. A sad ending for the hero!",
        "He hits his enemy, but the enemy isn't much hurted and strikes back. After a long fight, he is dead and the enemy is still living!"
        "The enemy kills he before he can even hit the enemy."
)


# ------------------------------
# On_Ready Output
# ------------------------------
# ------------------------------


@bot.event
async def on_ready():
    print("Date: " + datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S") + "| Running on: " + sys.platform)
    print("Bot Name: " + bot.user.name)
    if SECRETS.SHOWCASE == "false":
        print("Bot ID: " + bot.user.id)
    if bot.user.id == "591690480702586901":
        print("Bot Version: " + bot_version)
    print("Discord Version: " + discord.__version__)
    print("Connected on '" + str(len(bot.servers)) + "' servers and overwatching '" + str(len(set(bot.get_all_members()))) + "' players!")
    await bot.change_presence(game=discord.Game(name=title))
    print("Current Playing-Title: " + title)
    print("---------------------------------------------------------")
    print("Log starts here:")
    print("---------------------------------------------------------")


# ------------------------------
# On_Message Output
# ------------------------------
# ------------------------------


@bot.event
@commands.bot_has_permissions(mention_everyone=True)
@commands.has_permissions(manage_messages=True)
@commands.bot_has_permissions(manage_messages=True)
@commands.has_permissions(kick_members=True)
@commands.bot_has_permissions(kick_members=True)
@commands.has_permissions(ban_members=True)
@commands.bot_has_permissions(ban_members=True)
async def on_message(message):
    author = message.author
    channel = message.channel
    server = message.server
    content = message.content
    if message.author != bot.user:
        print("[MESSAGE] Server:" + str(server) + " | Channel:" + str(channel) + " | Name:" + str(author) + " | Message:" + str(content))
    else:
        print("[MESSAGE] Bot answered!")
    input = message.content.split()
    output = ":loudspeaker:"

    # Change Presence
    if message.content.startswith(str(Config.PREFIX) + "cp"):
        await bot.delete_message(message)
        output2 = " "
        print("[EXECUTOR]Cp executed by " + str(author))
        if author.id == "261179915892686849":
            author = message.author
            for word in input[1:]:
                output2 += word
                output2 += " "
            await bot.change_presence(game=discord.Game(name=(output2)))
            await bot.send_message(channel, "`Changed Title to: " + output2 + "`")
        else:
            bot.send_message(channel, "You are not allowed to do this")

    # Say Command
    if message.content.startswith(str(Config.PREFIX) + "say"):
        await bot.delete_message(message)
        print("[EXECUTOR]Say executed by " + str(author))
        author = message.author
        for word in input[1:]:
            output += word
            output += " "
        await bot.send_message(channel, output)

    # Help Command
    if message.content.startswith(str(Config.PREFIX) + "help"):
        await bot.delete_message(message)
        print("[EXECUTOR]Help executed by " + str(author))
        box = discord.Embed(color=discord.Color.blue(), description="These are my Functions:")
        if author.id == "261179915892686849":
            box.add_field(name="cp:", value="Changes the playing text", inline=True)
        box.add_field(name="info:", value="Info of the bot.", inline=True)
        box.add_field(name="help:", value="This message.", inline=True)
        box.add_field(name="adventure:", value="Go on a mission and attack one enemy of the empire.", inline=True)
        box.set_footer(text=bot_version)
        await bot.send_message(author, embed=box)

    # Info Command
    if message.content.startswith(str(Config.PREFIX) + "info"):
        await bot.delete_message(message)
        print("[EXECUTOR]Info executed by " + str(author))
        avatar = bot.user.avatar_url
        box = discord.Embed(color=discord.Color.dark_red(), description="This is Wolfii:")
        box.set_thumbnail(url=avatar)
        box.add_field(name="Name:", value=bot.user.name)
        box.add_field(name="My Prefix:", value=Config.PREFIX)
        box.add_field(name="Master:", value="TheLonelyWolf")
        box.add_field(name="Version:", value=bot_version)
        box.add_field(name="Discord Version:", value=discord.__version__)
        box.add_field(name="Connected on(Servers):", value=str(len(bot.servers)))
        box.add_field(name="Overwatching(Players/Bots):", value=str(len(set(bot.get_all_members()))))

        box.add_field(name="Purpose:", value ="I'm a fun and entertaining Bot. I was created by my Master for the Discord Hack Week")
        await bot.send_message(channel, embed=box)

    # Mission Command
    if message.content.startswith(str(Config.PREFIX) + "adventure"):
        await bot.delete_message(message)
        print("[EXECUTOR]Mission executed by " + str(author))
        text = str(message.author.mention)
        choice = enemys[random.randrange(0, len(enemys))]
        text = text + " wants to fight a " + choice + "! Will he survive?"
        await bot.send_message(channel, text)
        await asyncio.sleep(2)
        await bot.send_message(channel, "He attacks the enemy!")
        choice2 = result[random.randrange(0, len(result))]
        await asyncio.sleep(1)
        await bot.send_message(channel, choice2)

    # Dice Command
    if message.content.startswith(str(Config.PREFIX) + "dicerole"):
        await bot.delete_message(message)
        print("[EXECUTOR]Dice executed by " + str(author))
        await bot.send_message(channel, "`Rolling the dice...`")
        await asyncio.sleep(1)
        for word in input[1:]:
            if word == "1":
                dice_result = randint(1, 6)
                text = "Result: " + str(dice_result)
                await bot.send_message(channel, text)
            elif word == "2":
                dice_result = randint(1, 6)
                dice_result2 = randint(1, 6)
                text = "Result: " + str(dice_result) + " | " + str(dice_result2)
                await bot.send_message(channel, text)
            elif word == "3":
                dice_result = randint(1, 6)
                dice_result2 = randint(1, 6)
                dice_result3 = randint(1, 6)
                text = "Result: " + str(dice_result) + " | " + str(dice_result2) + " | " + str(dice_result3)
                await bot.send_message(channel, text)
            else:
                text = "None - Your input was incorrect! `wolfii:dicerole 1,2,3`"
                await bot.send_message(channel, text)

    if message.content.startswith(str(Config.PREFIX) + "ping"):
        before = time.monotonic()
        await bot.delete_message(message)
        ping = (time.monotonic() - before) * 1000
        await bot.send_message(channel, content=f":ping_pong: Pong! :ping_pong: Jokes aside, i'm currently running with: `{int(ping)}ms` :rotating_light: ")


bot.run(token)
