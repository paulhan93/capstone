from django.http import JsonResponse
from django.shortcuts import render
import json

def index(request):

    f = open('schedule.json')

    schedule = json.load(f)

    
    return JsonResponse({'schedule' : schedule})