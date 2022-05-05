from urllib import response
from django.http import HttpResponse

#Imports
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import time
import json

def scrape(request):
    
    #Open txt file that contains test projects and populate url array
    urls = []
    with open("./projects.txt", "r") as f:
        for item in f:
            temp = item.strip()
            urls.append(temp)

    #Call function to get custom fields
    for url in urls:
        response = getResponse(url)
        data = response.json()

        #From editmete grab the customfield name of Kickoff Data
        custom_array = data["fields"]
        for custom_field in custom_array:
            if data["fields"][custom_field]["name"] == "Kickoff Date":
                key = data["fields"][custom_field]["key"]

            if data["fields"][custom_field]["name"] == "Start date":
                key2 = data["fields"][custom_field]["key"]
            
            if data["fields"][custom_field]["name"] == "Due date":
                key3 = data["fields"][custom_field]["key"]


        getDate(key, url, key2, key3)
            

    return HttpResponse("""<html><script>window.location.replace('/jira');</script></html>  """)

def getDate(key, url, key2, key3):
    t_url = url.replace("/editmeta", "")
    response = getResponse(t_url)
    data = response.json()

    #get custom field option
    kickoff = data["fields"][key]
    start = data["fields"][key2]
    due = data["fields"][key3]

    #get name and project key
    name = data["fields"]["project"]["name"]
    proj_key = data["fields"]["project"]["key"]

    #Prints all the data
    print(name + " " + proj_key)
    #print(kickoff + " " + start + " " + due)
    #print(name + " " + kickoff + " " + start )

    #Send to JSON file or from here use function to use contents
    

def schedule(request):
    data = ""
    with open("./schedule.json", 'r') as fp:
        data = json.load(fp)

    print(type(data))
    print(data["PROJECT_KEY"])

    return HttpResponse("""<html><script>window.location.replace('/jira');</script></html>  """)

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
            response = requests.get(url,headers=headers,params=query,auth=("psu_capstone@4gclinical.com", "uMQ06ygSo2idk9No6jjn06CD"))
            return response
        except:
            print("Connection refused by server..")
            print("Let me sleep for 5 seconds")
            time.sleep(5)
            print("Trying again")
            continue
