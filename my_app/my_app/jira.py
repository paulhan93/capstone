from asyncio import constants
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
    #Assigned Projects
    myProjects()
    
    #Other Projects
    
    #Open txt file that contains test projects and populate url array
    # urls = []
    # with open("./projects.txt", "r") as f:
    #     for item in f:
    #         temp = item.strip()
    #         urls.append(temp)


    # # #Call function to get custom fields
    # for url in urls:
    #     response = getResponse(url)
    #     data = response.json()

    #     #WORKS TO GET SCHEDULE FOR EACH PROJECT
    #     kickoff = data['fields']['customfield_11768']
    #     cont_exec_date = data['fields']['customfield_11624']
    #     spec_sign_off = data['fields']['customfield_11770']
    #     smoke_start = data['fields']['customfield_11886']
    #     smoke_complete = data['fields']['customfield_11887']
    #     val_start = data['fields']['customfield_11842']
    #     val_complete = data['fields']['customfield_11771']
    #     uat_start = data['fields']['customfield_11763']
    #     uat_complete = data['fields']['customfield_11843']
    #     golive = data['fields']['customfield_11765']
    #     fpi = data['fields']['customfield_11766']
    #     start = data['fields']['customfield_11654']
    #     end = data['fields']['customfield_11772']
    #     name = data['fields']['project']['name']
    #     key = data['fields']['project']['key']

    #     toJSON(kickoff, cont_exec_date, spec_sign_off, smoke_start, smoke_complete, val_start, val_complete, uat_start, uat_complete,golive, fpi, start, end, name, key)

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


def getResponse(url):
    headers = {
    "Accept": "application/json"
    }

    response = ''
    while response == '':
        try:
            response = requests.get(url,headers=headers,auth=("psu_capstone@4gclinical.com", "iwK4GNzvsNfg0hnGx2Vl492A"))
            return response
        except:
            print("Connection refused by server..")
            print("Let me sleep for 5 seconds")
            time.sleep(5)
            print("Trying again")
            continue

def myProjects():
    url = "https://qa-4gclinical.atlassian.net/rest/api/3/search?jql=assignee=currentuser()"
    response = getResponse(url)

    data = response.json()

    urls = []
    for issue in data['issues']:
        urls.append(issue['self'])
    print(urls)

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

        print(kickoff , cont_exec_date)

        #Send to JSON
        toJSON(kickoff, cont_exec_date, spec_sign_off, smoke_start, smoke_complete, val_start, val_complete, uat_start, uat_complete,golive, fpi, start, end, name, key)


