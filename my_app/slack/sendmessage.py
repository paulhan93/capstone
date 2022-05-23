import requests
#import sys
from django.http import HttpResponse
#import getopt

def send_message(message):
  payload = '{"text":"%s"}' % message
  response = requests.post('https://hooks.slack.com/services/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', data=payload)
  print(response.text)

def main(argv):

  message = "https://youtu.be/KHPrY2LHR_8"
  
  #try: opts, args = getopt.getopt(argv, "hm:", ["message="])

  #except getopt.GetoptError:
  #  print('To use the script, type: main.py -m "<message>"')
  #  return HttpResponse("""<html><script>window.location.replace(');</script></html>""")
  #  sys.exit(2)

  #for opt, arg in opts:
  #  if opt == '-h':
  #    print('main.py -m <message>')
  #    return HttpResponse("""<html><script>window.location.replace(');</script></html>""")
  #    sys.exit()
  # elif opt in ("-m", "--message"):
  #    message = arg
  
  send_message(message)
  return HttpResponse("""<html><script>window.location.replace(');</script></html>""")

#if __name__ == "__main__":
#  main(sys.argv[1:])