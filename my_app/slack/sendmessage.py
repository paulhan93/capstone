import requests
import sys
import getopt
from django.http import HttpResponse


def send_message(message, webhook):
  payload = '{"text":"%s"}' % message

  hook3 = 'lack.com/services/'
  hook2 = 'ooks.s'
  hook1 = 'https://h'

  response = requests.post( hook1 + hook2 + hook3 + webhook, data=payload)







