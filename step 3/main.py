#
#   Cisco AMP for Endpoints Sample App
#       v.03
#
#   Glenn Quah (glquah@cisco.com)
#   Vorachat Nantasupawatana (vnantasu@cisco.com)
#   Iman Arifin (imarifin@cisco.com)
#       Mar 2017
#
#       This class provides methods to facilitate
#       access to the Advanced Malware Protection API.
#
#   REQUIREMENTS:
#       Python sys library
#       AMP Wrapper_API module to access the AMP API
#
#   WARNING:
#       This script is meant for educational purposes only.
#       Any use of these scripts and tools is at
#       your own risk. There is no guarantee that
#       they have been through thorough testing in a
#       comparable environment and we are not
#       responsible for any damage or data loss
#       incurred with their use.
#
#   INFORMATION:
#       If you have further questions about this API and script, please contact GVE. Here are the contact details:
#           For internal Cisco gve-programmability@cisco.com
#           For Cisco partners, open a case at www.cisco.com/go/ph

import sys
import json
from AMP_API import Wrapper
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
@app.route("/")
def dashboard():
    return render_template('index.html')

@app.route("/download.html")
def download():
    return render_template('download.html')

@app.route("/index.html", methods=["GET", "POST"])
def selectOption():
    """
    Initialise Wrapper object
    """
    ampWrapper = Wrapper(hostname, username, password)
    print(request.form.getlist("computer"))
    if request.form.get("computer"):
        print("checked computer")
    if request.form.get("event"):
        print("checked event")
    if request.form.get("eventType"):
        print("eventType")
    return redirect('/')

def outputJson():
    """
    Main method for our initializing our Wrapper API and calling functions
    """

    """
    Retrieve API keys from settings.txt
    """
    with open('settings.txt', 'r') as f:
        hostname = f.readline().replace('\n', '')  # removes linefeed at the end of everyline
        username = f.readline().replace('\n', '')
        password = f.readline().replace('\n', '')
    print(hostname, username, password)

    """
    Initialise Wrapper object
    """
    ampWrapper = Wrapper(hostname, username, password)

    """
    Retrieves a list of computers
    """
    getComputersJson = ampWrapper.getComputers()
    with open('computerList.json', 'w', encoding='utf-8') as outfile:
        json.dump(getComputersJson, outfile, skipkeys=True, indent=2, ensure_ascii=True, separators=(',', ':'),sort_keys=True)
    #print("printing list of computers")
    #print(getComputersJson)

    """
    Retrieves a list of event types
    """
    getEventTypeJson = ampWrapper.getEventTypes()
    with open('eventTypeList.json', 'w', encoding='utf-8') as outfile:
        json.dump(getEventTypeJson, outfile, skipkeys=True, indent=2, ensure_ascii=True, separators=(',', ':'),sort_keys=True)
    #print("printing list of event types")
    #print(getEventTypeJson)

    """
    Retrieves a list of event sorted in descending order by timestamp
    """
    getEventJson = ampWrapper.getEvent()
    with open('eventList.json', 'w', encoding='utf-8') as outfile:
        json.dump(getEventJson, outfile, skipkeys=True, indent=2, ensure_ascii=True, separators=(',', ':'),sort_keys=True)
    #print("printing list of events")
    #print(getEventJson)

    """
    Retrieves a list of application blocking lists
    """
    getApplicationsBlockingListJson = ampWrapper.getApplicationsBlockingList()
    with open('applicationBlockingList.json', 'w', encoding='utf-8') as outfile:
        json.dump(getApplicationsBlockingListJson, outfile, skipkeys=True, indent=2, ensure_ascii=True, separators=(',', ':'),sort_keys=True)
    #print("printing list of application blocking lists")
    #print(getApplicationsBlockingListJson)

    """
    Retrieves a list of groups
    """
    getGroupsJson = ampWrapper.getGroups()
    with open('groups.json', 'w', encoding='utf-8') as outfile:
        json.dump(getGroupsJson, outfile, skipkeys=True, indent=2, ensure_ascii=True, separators=(',', ':'),sort_keys=True)
    #print("printing list of groups")
    #print(getGroupsJson)

    """
    Retrieves a list of policies
    """
    getPolicyJson = ampWrapper.getPolicy()
    with open('policy.json', 'w', encoding='utf-8') as outfile:
        json.dump(getPolicyJson, outfile, skipkeys=True, indent=2, ensure_ascii=True, separators=(',', ':'),sort_keys=True)
    #print("printing list of policies")
    #print(getPolicyJson)

    """
    Retrieves a list of event after specified time
    """
    #getEventTimeStampJson = ampWrapper.getEventTimeStamp('2017-03-01')
    #with open('eventListTimeStamp.json', 'w', encoding='utf-8') as outfile:
    #    json.dump(getEventTimeStampJson, outfile, skipkeys=True, indent=2, ensure_ascii=True, separators=(',', ':'))
    #print("printing list of events after specified time")
    #print(getEventTimeStampJson)


    """
    Retrieves a list of computers with given connector_guid
    """
    #getComputersConnectorGuidJson = ampWrapper.getComputersConnectorGuid('5be84e5c-2c2f-40f6-bcc6-3a53cd335b3f')
    #with open('computerListGuid.json', 'w', encoding='utf-8') as outfile:
    #    json.dump(getComputersConnectorGuidJson, outfile, skipkeys=True, indent=2, ensure_ascii=True, separators=(',', ':'))
    #print("printing list of computers with given guid")
    #print(getComputersConnectorGuidJson)

    """
    Merges json objects and output as a single file
    """
    outJson = { 'computerList': getComputersJson, 'eventTypeList' : getEventJson, 'eventList' : getEventJson, 'applicationBlockingList' : getApplicationsBlockingListJson, 'groups' : getGroupsJson, 'policy' : getPolicyJson }
    print(outJson)
    with open('out.json', 'w', encoding='utf-8') as outfile:
        json.dump(outJson, outfile, skipkeys=True, indent=2, ensure_ascii=True, separators=(',', ':'),sort_keys=True)


if __name__ == '__main__':
    #outputJson()
    app.run()
    #sys.exit(outputJson())
