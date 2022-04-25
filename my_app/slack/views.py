from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.views.generic import TemplateView

from .sendmessage import send_message

@api_view(["POST"])
def sendmessage(request):
    str = request.POST["message"]
    send_message(str)
    return HttpResponse("You submitted: \"" + str + "\"")

# Alternative way to load a html page:
# class TestSendMessageView(TemplateView):
#    template_name = "slack/sendmessage.html"

