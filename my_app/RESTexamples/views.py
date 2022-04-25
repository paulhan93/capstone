from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rest_framework.decorators import api_view
from .generatequote import *

@api_view(["GET"])
def quote(request):
    return HttpResponse(random_quote())

@api_view(["POST"])
def postit(request):
    str = request.POST["stringa"]
    return HttpResponse("You submitted: \"" + str + "\"")


#   body_unicode = request.body.decode('utf-8')
#    body_data = json.loads(body_unicode)
#   content = body_data['content']

# Working POST request data code:
# return HttpResponse("You submitted: \"" + request.body.decode('utf-8') + "\"")


# @api_view(["POST"])
# def post_data(request):

# Trial and error: 
    #return  HttpResponse("I choose to run towards my problems and not away from them. Because that's what heroes do. -Thor Ragnarok (2017)")
    #return HttpResponse(generatequote.random_quote())
    #content = {"message": "I choose to run towards my problems and not away from them. Because that's what heroes do. -Thor Ragnarok (2017)"}
    #return JsonResponse(content)

# Import statement attempts:
#from .views import generatequote
#import generatequote
#from RESTexamples.generatequote import 

