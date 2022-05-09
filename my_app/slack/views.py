from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.views.generic import TemplateView

from .sendmessage import send_message

@api_view(["POST"])
def sendmessage(request):

  # Random:
  hooka4 = 'iWnWYg4bZiwSaebPGfMgV8n' 
  hooka3 = '03E9G3TW4W/y'
  hooka2 = '03A0K7N7MX/B'
  hooka1 = 'T'

  # General:
  hookb4 = 'cSEyV3xpOvxT4bRQqRLN8fw' 
  hookb3 = '03EG5WCW0K/p'
  hookb2 = '03A0K7N7MX/B'
  hookb1 = 'T'

  webhooks = [ hooka1 + hooka2 + hooka3 + hooka4,  hookb1 + hookb2 + hookb3 + hookb4 ]

  str = request.POST["message"]

  for i in range(len(webhooks)):
    send_message(str, webhooks[i])

  return HttpResponse("You submitted: \"" + str + "\"")

# Alternative way to load a html page:
# class TestSendMessageView(TemplateView):
#    template_name = "slack/sendmessage.html"

# Dummy comment to allow a new commit

