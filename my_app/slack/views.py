from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.views.generic import TemplateView

from .sendmessage import send_message
from .getmessages import getmessage
import json
from datetime import datetime

@api_view(["POST"])
def sendmessage(request):

# Janssen-5607
  hook0_4 = 'cEgNSO5d4YBqUKiVImKqNzq'
  hook0_3 = '03FSR3V6S3/J'
  hook0_2 = '03A0K7N7MX/B'
  hook0_1 = 'T'

# Janssen-6613
  hook1_4 = 'pOtkCNrlI5T9u6QdJjLzNwx'
  hook1_3 = '03G9PGFSJ0/i'
  hook1_2 = '03A0K7N7MX/B'
  hook1_1 = 'T'

# Janssen-7248
  hook2_4 = 'lrDg3wfZlCa1Z4Bmd02BKer'
  hook2_3 = '03GX6080SC/2'
  hook2_2 = '03A0K7N7MX/B'
  hook2_1 = 'T'

  webhooks = [ hook0_1 + hook0_2 + hook0_3 + hook0_4, hook1_1 + hook1_2 + hook1_3 + hook1_4, hook2_1 + hook2_2 + hook2_3 + hook2_4 ]

  str = request.POST["message"]

  for i in range(len(webhooks)):
     send_message(str, webhooks[i])
  return HttpResponse("")

  #return HttpResponseRedirect('/slack/sendmessage.html')
  #return HttpResponse("")

def get_formatted_messages(request):
  channel_enum = ''
  try:
    channel_enum = request.GET["channel"]
  except:
    channel_enum = '0'
  return HttpResponse(getmessage(channel_enum))


 # return HttpResponse(html)

# Alternative way to load a html page:
# class TestSendMessageView(TemplateView):
#    template_name = "slack/sendmessage.html"
# Dummy text: html = "<b>Slack message data will show here. <br> It is a good platform to learn programming. It is an educational website. Prepare for the Recruitment drive of product based companies like Microsoft, Amazon, Adobe etc with a free online placement preparation course. The course focuses on various MCQ's & Coding question likely to be asked in the interviews & make your upcoming placement season efficient and successful. Also, any geeks can help other geeks by writing articles on the GeeksforGeeks, publishing articles follow few steps that are Articles that need little modification/improvement from reviewers are published first. To quickly get your articles reviewed, please refer existing articles, their formatting style, coding style, and try to make you are close to them. In case you are a beginner, you may refer Guidelines to write an Article</b>"
# Dummy comment to allow a new commit

#  return HttpResponse(get_json_messages())   -- working return message for getting messages from slack

# Working take Slack data and convert to string:
#  str = json.dumps(get_json_messages().data)
#  return HttpResponse(str)