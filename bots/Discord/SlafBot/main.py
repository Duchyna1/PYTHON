from __future__ import print_function

import os

import discord

import datetime
import random
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from insults import all
########################################################################################################################


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

EVENTS = []

def getEvents(next):
    global  EVENTS
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=next, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
        return None
    return events

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
        response = str(time_diff(datetime.datetime.strptime(now, '%H:%M:%S'), datetime.datetime.strptime(EVENTS[0]['start']['dateTime'][11:-6], '%H:%M:%S')))
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

def time_diff(start, end):
    if isinstance(start, datetime.time):
        assert isinstance(end, datetime.time)
        start, end = [datetime.datetime.combine(datetime.datetime.min, t) for t in [start, end]]
    if start <= end:
        return end - start
    else:
        end += datetime.timedelta(1)
        assert end > start
        return end - start

client.run(TOKEN)
