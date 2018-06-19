import random
import diceFunctions
import cineSearch
import discord
from discord.ext.commands import Bot
from discord import Game
import json

botPrefix = ("!", "?")
Bot = Bot(command_prefix=botPrefix)


@Bot.command(name='ping',
             description='test if the bot is available',
             brief=' - bot test',
             aliases=['Ping', 'p1ng', 'pinG'],
             pass_context=True)
async def ping(context):
    await Bot.say(context.message.author.mention + ' pong')


@Bot.command(name='dice',
             description='roll a dice',
             brief=' - roll dice',
             pass_context=True)
async def dice(context, *args):
    print('input operation ' + ''.join(args))
    result = diceFunctions.dice(''.join(args))

    # await Bot.say(context.message.author.mention + ' ' + embed=result)
    try:
        await Bot.say(embed=result)
    except:
        await Bot.say(context.message.author.mention + " je n'ai pas compris...")


@Bot.command(name='join',
             pass_context=True,
             description='Connect bigBot to user channel',
             brief=' - connect to a vocal channel')
async def join(context):
    currentChan = context.message.author.voice_channel
    try:
        await Bot.join_voice_channel(currentChan)
        print('joined ' + str(currentChan))
    except discord.ClientException:
        await Bot.say(' Je suis déjà dans un autre channel')
    except discord.InvalidArgument:
        await Bot.say(' Ce channel est invalide')


@Bot.command(name='play',
             pass_context=True,
             description='play a video from youtube on a discord voice channel',
             brief=' - audio from YT')
async def play(context, url):
    currentChan = context.message.author.voice_channel
    for vc in Bot.voice_clients:
        if (vc.server == context.message.server):
            player = await vc.create_ytdl_player(url)
            player.start()



@Bot.command(name='quit',
             description='disconnect bigBot from current vocal channel',
             brief=' - disconnect from vocal',
             pass_context=True)
async def quit(context):
    for vc in Bot.voice_clients:
        if (vc.server == context.message.server):
            return await vc.disconnect()


@Bot.command(name='cinema',
             description='look for infos about a movie on betaseries',
             brief=' - info on a movie',
             pass_context=True)
async def cinema(context, *args):
    # result = cineSearch.getMovieInfo(469)
    result = cineSearch.searchTitle(str(args))
    await Bot.say(embed=result)



@Bot.event
async def on_message(message):
    if message.author != Bot.user and 'jojo' in message.content:
        await Bot.send_message(message.channel, 'Is that a jojo refrence ???')
        await Bot.send_file(message.channel, 'img/jojo_ref.jpg')
    elif message.author != Bot.user and 'niko niko ni' in message.content:
        await Bot.send_message(message.channel, 'ANATA NO FILS DE PUTE !!!')
        await Bot.send_file(message.channel, 'img/anime_fuck_yourself.jpg')
    await Bot.process_commands(message)


@Bot.event
async def on_ready():
    await Bot.change_presence(game=Game(name='liquid'))
    print('Logged in as')
    print(Bot.user.name)
    print(Bot.user.id)
    print('------')


@Bot.event
async def on_error():
    await Bot.say("Je n'ai pas compris...")

with open("./bot.conf", "r") as file:
    conf = json.load(file)
Bot.run(conf["token"])
