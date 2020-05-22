from __future__ import print_function

import discord
import datetime
import time
import asyncio

from insults import all
from calendarStuff import *
from dateStuff import *
from redditStuff import *

TOKEN = 'NzEwMzkzNjE0NTA4ODg0MDU5.XsN78Q.53naFkdexm3vUwJFjcdXHFGlY2o'

client = discord.Client()
server = None

@client.event
async def on_ready():
    global server
    print(f'{client.user.name} has connected to Discord!')
    server = client.get_guild(692033460499513346)
    await server.get_channel(710115532992544817).send('Ok som spat')
    client.loop.create_task(memes())

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'WTF jak si sa dostal na tento server??'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(message.author, message.content)

    # elif message.content == '':
    #     response = ''
    #     await message.channel.send(response)

    if message.content == 'idk help':
        response = 'idk help\n' \
                   'idk yeet\n' \
                   'idk time\n' \
                   'idk slaf time\n' \
                   'idk hodina\n' \
                   'idk rozvrh\n' \
                   'idk frik me'
        await message.channel.send(response)

    elif message.content == 'idk yeet':
        response = 'YEEEEEEEEEEEEEEEEEEEEEEEEEEET'
        await message.channel.send(response)

    elif message.content == 'idk time':
        response = datetime.datetime.now().strftime("%H:%M:%S")
        await message.channel.send(response)

    elif message.content == 'idk slaf time':
        EVENTS = getEvents(1)
        now = datetime.datetime.now().strftime("%H:%M:%S")
        date = days_between(str(datetime.date.today()), str(EVENTS[0]['start']['dateTime'][:10]))-1
        response = str(time_diff(datetime.datetime.strptime(now, '%H:%M:%S'), datetime.datetime.strptime(EVENTS[0]['start']['dateTime'][11:-6], '%H:%M:%S')))
        if date > 0:
            response += ' a ' + str(date) + ' d'
        await message.channel.send('Mozes slafovat este: ' + response)

    elif message.content == 'idk hodina':
        EVENTS = getEvents(1)
        time = EVENTS[0]['start']['dateTime'][11:-6]
        response = EVENTS[0]['summary'] + ' ' + time
        await message.channel.send(response)

    elif message.content == 'idk rozvrh':
        EVENTS = getEvents(10)
        response = ''
        for event in EVENTS:
            try:
                date = event['start']['dateTime'][8:10] + '. ' + event['start']['dateTime'][5:7] + '.'
                time = event['start']['dateTime'][11:-9]
                response += date + '\t' + time + '\t' + event['summary'] + '\n'
            except:
                date = event['start']['dateTime'][8:10] + '. ' + event['start']['dateTime'][5:7] + '.'
                time = event['start']['dateTime'][11:-9]
                response += date + '\t' + time + '\t' + event['htmlLink'] + '\n'
        await message.channel.send(response)

    elif message.content == 'idk frik me':
        response = all[random.randint(0, len(all))]
        await message.channel.send(response)
#######################################################################################################################
async def memes():
    global server
    while not client.is_closed():
        channel = server.get_channel(710108232219099176)
        await channel.send(getMemes(1, 'PewdiepieSubmissions'))
        await channel.send(getMemes(1, 'wholesomememes'))
        await channel.send(getMemes(1, 'tumblr'))
        await asyncio.sleep(60 * 30)


client.run(TOKEN)

