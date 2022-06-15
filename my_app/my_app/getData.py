from asyncio import constants
from django.http import HttpResponse

#Imports
import requests
import time
import json


def scrape(request):
    #Assigned Projects
    myProjects()

    return HttpResponse("""<html><script>window.location.replace('/jira');</script></html>  """)

def toJSON(kickoff,contract, spec, smoke_start, smoke_comp, val_S, val_comp, uat_S, uat_comp, golive, fpi, start, end, name, key):
    #print(name + key + kickoff + start + due)

    '''data = {
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
    }'''

    with open('schedule.json', 'r+') as file:
        schedule_data = json.load(file)

        for index in schedule_data["Projects"]:
            if index["Project Name"] == name:
                index["Schedule"]["Contract Executed Date"] = contract
                index["Schedule"]["Kickoff Date"] = kickoff
                index["Schedule"]["Spec Sign Off"] = spec
                index["Schedule"]["Smoke Testing Start"] = smoke_start
                index["Schedule"]["Smoke Testing Complete"] = smoke_comp
                index["Schedule"]["Validation Start"] = val_S
                index["Schedule"]["Validation Complete"] = val_comp
                index["Schedule"]["UAT Start"] = uat_S
                index["Schedule"]["UAT Complete"] = uat_comp
                index["Schedule"]["GoLive"] = golive
                index["Schedule"]["FPI"] = fpi
                index["Schedule"]["Start Date"] = start
                index["Schedule"]["Due Date"] = end

        file.seek(0)
        json.dump(schedule_data, file, indent=4)

def getResponse(url):
    headers = {
    "Accept": "application/json"
    }

    response = ''
    while response == '':
        try:
            response = requests.get(url,headers=headers,auth=("psu_capstone@4gclinical.com", "B7iDc5S7K5HUatMBczhK6A65"))
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
        name = data['fields']['summary']
        key = data['fields']['project']['key']

        #Send to JSON
        toJSON(kickoff, cont_exec_date, spec_sign_off, smoke_start, smoke_complete, val_start, val_complete, uat_start, uat_complete,golive, fpi, start, end, name, key)


