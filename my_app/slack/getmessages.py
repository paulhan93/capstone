from ctypes import c_int16
import logging
import os
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def get_json_messages():
    # Obscure the token
    us7 = '25d9654e572ecfcf7f917baf48b8b99'
    us6 = '515940184112-5'
    us5 = '325296356918-3'
    us4 = '340653755745-3'
    us3 = 'p-3'
    us2 = 'ox'
    us1 = 'x'
    # Obscure the channel id
    ci2 = '039N12TVA7'
    ci1 = 'C'

    # Reconstruct tokens
    user_token = us1 + us2 + us3 + us4 + us5 + us6 + us7
    channel_id = ci1 + ci2

    # WebClient instantiates a client that can call API methods
    client = WebClient(token=user_token)
    logger = logging.getLogger(__name__)
    # Store conversation history
    conversation_history = []
    # ID of the channel you want to send the message to

    try:
        # Call the conversations.history method using the WebClient
        # conversations.history returns the first 100 messages by default
        # These results are paginated, see: https://api.slack.com/methods/conversations.history$pagination
        result = client.conversations_history(channel=channel_id)

        conversation_history = result["messages"]


        # Print results
        logger.info("{} messages found in {}".format(len(conversation_history), id))

    except SlackApiError as e:
        logger.error("Error creating conversation: {}".format(e))

    history = client.api_call(api_method='conversations.history',data={'channel':channel_id})
    
    return history

