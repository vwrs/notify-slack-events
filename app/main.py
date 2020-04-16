import os
import json
import requests
from dotenv import load_dotenv
from slackeventsapi import SlackEventAdapter
from flask import Flask


load_dotenv(verbose=True)

WEBHOOK_URL = os.environ.get('WEBHOOK_URL', '')
SLACK_SIGNING_SECRET = os.environ.get('SLACK_SIGNING_SECRET', '')
slack_events_adapter = SlackEventAdapter(SLACK_SIGNING_SECRET, endpoint="/slack/events")


def post_by_webhook(text, username='events-app'):
    response = requests.post(
        WEBHOOK_URL,
        data=json.dumps({
            'text': text,
            'username': username,
            # 'icon_emoji': ':slack:'
            'link_names': 1
        }),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError(response.text)
    print(response)


@slack_events_adapter.on('user_change')
def user_change(event_data):
    '''Create an event listener for "user_change" events'''
    event = event_data['event']
    profile = event['user']['profile']
    name = profile['display_name'] or profile['real_name']
    text = f"{name}: {profile['status_emoji']} {profile['status_text']}"
    print(text)
    post_by_webhook(text)


@slack_events_adapter.on('reaction_added')
def reaction_added(event_data):
    '''Create an event listener for "reaction_added" events'''
    event = event_data['event']
    emoji = event['reaction']
    user = event['user']
    # item_user = event['item_user'] or 'someone'
    text = f'@{user} added a reaction :{emoji}:.'
    print(text)
    post_by_webhook(text)


if __name__ == '__main__':
    # Start the server on port 3000
    slack_events_adapter.start(port=3000, debug=True)
