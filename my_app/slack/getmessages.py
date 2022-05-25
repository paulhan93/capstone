import logging
from datetime import datetime
#import os
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
import json
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_html = ''

def getmessage(select):

    global slack_html
    slack_html = ''

    # Obscure the token
    us7 = '25d9654e572ecfcf7f917baf48b8b99'
    us6 = '515940184112-5'
    us5 = '325296356918-3'
    us4 = '340653755745-3'
    us3 = 'p-3'
    us2 = 'ox'
    us1 = 'x'
    # Obscure the channel ids
    cid_5607_02 = '3G45YF3A9'
    cid_5607_01 = 'C0'
    cid_6613_02 = '3GWRKVC4Q'
    cid_6613_01 = 'C0'
    cid_7248_02 = '3G72NEPSP'
    cid_7248_01 = 'C0'

    # Reconstruct tokens
    user_token = us1 + us2 + us3 + us4 + us5 + us6 + us7
    cid_5607 = cid_5607_01 + cid_5607_02
    cid_6613 = cid_6613_01 + cid_6613_02
    cid_7248 = cid_7248_01 + cid_7248_02

    # WebClient instantiates a client that can call API methods
    client = WebClient(token=user_token)
    logger = logging.getLogger(__name__)
    # Store conversation history
    conversation_history = []
    # ID of the channel you want to send the message to

    channel_id = ''

    if select == '0':
        channel_id = cid_5607 # Janssen-5607
    elif select == '1':
        channel_id = cid_6613 # Janssen-6613
    elif select == '2':
        channel_id = cid_7248 # Janssen-7248
    else: 
        channel_id = cid_5607

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

    str_history = json.dumps(history.data, indent=2)
    dict_history = json.loads(str_history)

    # Constants for building the HTML:
    type = ''
    text = ''
    attachments = ''
    slack_username = ''
    str_date = ''
    files = ''
    video_html = ''
    hyperlink = ''

    x = range(0, 99)
    for i in x:
        try:
            type = dict_history['messages'][i]['type']
            text = dict_history['messages'][i]['text']

            try:
                attachments = dict_history['messages'][i]['attachments']
            except KeyError:
                pass

            try:
                video_html = dict_history['messages'][i]['attachments'][0]['video_html']
            except KeyError:
                pass
                
            try:
                hyperlink = dict_history['messages'][i]['files'][0]['url_private']
            except KeyError:
                pass

            try:
                files = dict_history['messages'][i]['files']
            except KeyError:
                pass

            try: 
                slack_user_id = dict_history['messages'][i]['user']
                slack_userdata = client.api_call(api_method='users.info', data={'user':slack_user_id})
                slack_username = slack_userdata['user']['real_name']
            except KeyError:
                slack_username = 'ExampleCodeBot'
    
            input_timestamp = dict_history['messages'][i]['ts']
            float_timestamp = float(input_timestamp)
            timestamp = int(float_timestamp)
            dt = datetime.fromtimestamp(timestamp)
            str_date = dt.strftime('%Y-%m-%d %I:%M %p')

            build_html(slack_username, str_date, hyperlink, video_html, text)

            # Cleanup:
            type = ''
            text = ''
            attachments = ''
            slack_username = ''
            str_date = ''
            files = ''
            video_html = ''
            hyperlink = ''

        except IndexError:
            text = 'IndexError Exception occurred in getmessage().'
            break
    
    return slack_html


def build_html(str_name, str_date, str_hyperlink, str_video_html, str_text):
    global slack_html
    slack_html += '<div class="text_bubble"><span class="slack_username">' + str_name + '</span> <span class="slack_date_time">' + str_date + '</span><br>'
    if str_text:
        slack_html += '<span class="slack_message">' + str_text + '</span><br>'
    if str_hyperlink:
        slack_html += 'File attachment: <span class="slack_hyperlink"><a href="' + str_hyperlink + '" target=_blank>' + str_hyperlink + '</a></span><br>'
    if str_video_html:
        slack_html += str_video_html + '<br>'
    slack_html += '</div>'



# Old working function for getting the raw JSON message data
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

