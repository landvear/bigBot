import random
import diceFunctions
import discord
from discord.ext.commands import Bot
from discord import Game

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


@Bot.command(name='muz',
             description='play a video from youtube URL',
             brief=' - audio from YT',
             pass_context=True)
async def muz(context, url):
    if url == 'quit':
        await Bot.disconnect()
    else:
        currentChan = context.message.author.voice_channel
        voiceJoin = await Bot.join_voice_channel(channel=currentChan)
        player = await voiceJoin.create_ytdl_player(url)
        player.start()


@Bot.command(name='quit',
             description='disconnect bigBot from current vocal channel',
             brief=' - disconnect from vocal')

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

Bot.run('NDQ3NDE2MzY2NTM4OTQ4NjE4.DeL5Vw.3rFPZ_ZrKGcm-zZ0Ns73BL49zjM')
