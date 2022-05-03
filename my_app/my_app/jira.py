from urllib import response
from django.http import HttpResponse

#Imports
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import time
import json
import pandas as pd


FLAG = 0

def scrape(request):
    
    #Open txt file that contains test projects and populate url array
    urls = []
    with open("./projects.txt", "r") as f:
        for item in f:
            temp = item.strip()
            urls.append(temp)


    # #Call function to get custom fields
    for url in urls:
        response = getResponse(url)
        data = response.json()

        #WORKS TO GET SCHEDULE FOR EACH PROJECT
        kickoff = data['fields']['customfield_11768']
        cont_exec_date = data['fields']['customfield_11624']
        spec_sign_off = data['fields']['customfield_11770']
        smoke_start = data['fields']['customfield_11886']
        smoke_complete = data['fields']['customfield_11887']
        val_start = data['fields']['customfield_11842']
        val_complete = data['fields']['customfield_11771']
        uat_start = data['fields']['customfield_11763']
        uat_complete = data['fields']['customfield_11843']
        golive = data['fields']['customfield_11765']
        fpi = data['fields']['customfield_11766']
        start = data['fields']['customfield_11654']
        end = data['fields']['customfield_11772']
        name = data['fields']['project']['name']
        key = data['fields']['project']['key']

        toJSON(kickoff, cont_exec_date, spec_sign_off, smoke_start, smoke_complete, val_start, val_complete, uat_start, uat_complete,golive, fpi, start, end, name, key)

    return HttpResponse("""<html><script>window.location.replace('/jira');</script></html>  """)

def toJSON(kickoff,contract, spec, smoke_start, smoke_comp, val_S, val_comp, uat_S, uat_comp, golive, fpi, start, end, name, key):
    #print(name + key + kickoff + start + due)

    data = {
        "Project Name": name,
        "Project Key": key,
        "Schedule": {
            "Contract Executed Date": contract,
            "Kickoff Date": kickoff,
            "Spec Sign Off": spec,
            "Smoke Testing Start": smoke_start,
            "Smoke Testing Complete": smoke_comp,
            "Validation Start": val_S,
            "Validation Complete": val_comp,
            "UAT Start": uat_S,
            "UAT Complete": uat_comp,
            "GoLive": golive,
            "FPI": fpi,
            "Start Date": start,
            "Due Date": end
        }
    }


    with open('schedule.json', 'r+') as file:
        f_data = json.load(file)

        f_data["Projects"].append(data)
        file.seek(0)
        json.dump(f_data, file, indent=4)

        #If it doesnt then append
        #print(f_data['Projects'][0]['Project Key'])

def getResponse(url):
    headers = {
    "Accept": "application/json"
    }

    query = {
        'total': '131'
    }

    response = ''
    while response == '':
        try:
            response = requests.get(url,headers=headers,auth=("psu_capstone@4gclinical.com", "API_KEY"))
            return response
        except:
            print("Connection refused by server..")
            print("Let me sleep for 5 seconds")
            time.sleep(5)
            print("Trying again")
            continue


def customF():
    url = 'https://qa-4gclinical.atlassian.net/rest/api/3/issue/BAYER-2049/'
    response = getResponse(url)    
    data = response.json()

    #print(data['fields']['customfield_11768'])
    kickoff = data['fields']['customfield_11768']
    spec_sign_off = data['fields']['customfield_11770']
    smoke_start = data['fields']['customfield_11886']
    smoke_complete = data['fields']['customfield_11887']
    val_start = data['fields']['customfield_11842']
    val_complete = data['fields']['customfield_11771']
    uat_start = data['fields']['customfield_11763']
    uat_complete = data['fields']['customfield_11843']
    golive = data['fields']['customfield_11765']
    fpi = data['fields']['customfield_11766']
    start = data['fields']['customfield_11654']
    due = data['fields']['duedate']