import os
from datetime import datetime, time as datetime_time, timedelta

import discord

########################################################################################################################


########################################################################################################################
TOKEN = 'NzEwMzkzNjE0NTA4ODg0MDU5.XrzzwA.dSIfKaiT04dwSJlbIWOFTIqQeJw'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

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

    # elif message.content == '':
    #     response = ''
    #     await message.channel.send(response)

    if message.content == 'idk help':
        response = 'idk help\n' \
                   'idk yeet\n' \
                   'idk time\n' \
                   'idk slaf time'
        await message.channel.send(response)

    elif message.content == 'idk yeet':
        response = 'YEEEEEEEEEEEEEEEEEEEEEEEEEEET'
        await message.channel.send(response)

    elif message.content == 'idk time':
        response = datetime.now().strftime("%H:%M:%S")
        await message.channel.send(response)

    elif message.content == 'idk slaf time':
        now = datetime.now().strftime("%H:%M:%S")
        response = str(time_diff(datetime.strptime(now, '%H:%M:%S'), datetime.strptime('9:00:00', '%H:%M:%S')))
        await message.channel.send('Mozes slafovat este: ' + response)

    elif message.content == 'idk hodina':
        response = ''
        await message.channel.send(response)

#######################################################################################################################

def time_diff(start, end):
    if isinstance(start, datetime_time):
        assert isinstance(end, datetime_time)
        start, end = [datetime.combine(datetime.min, t) for t in [start, end]]
    if start <= end:
        return end - start
    else:
        end += timedelta(1)
        assert end > start
        return end - start

client.run(TOKEN)