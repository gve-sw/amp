#
#   Cisco AMP for Endpoints Sample App
#       v.03
#
#   Glenn Quah (glqjuah@cisco.com)
#   Vorachat Nantasupawatana (vnantasu@cisco.com)
#   Iman Arifin (imarifin@cisco.com)
#       Mar 2017
#
#       This class provides methods to facilitates
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
from Wrapper_API import Wrapper

def main():
    """
    Main method for our initializing our Wrapper API and calling functions
    """

    """
    Retrieve API keys from settings.txt
    """
    with open('settings.txt', 'r') as f:
        hostname = f.readline().replace('\n', '')
        username = f.readline().replace('\n', '')
        password = f.readline().replace('\n', '')
    print(hostname, username, password)

    """
    Initialise Wrapper
    """
    getWrapperAPI = Wrapper(hostname, username, password)

    """
    Retrieves a list of computers
    """
    getComputersJson = getWrapperAPI.getComputers()
    with open('computerList.json', 'w', encoding='utf-8') as outfile:
        json.dump(getComputersJson, outfile, skipkeys=True, indent=2, ensure_ascii=True, separators=(',', ':'))
    print("printing list of computers")
    print(getComputersJson)

    """
    Retrieves a list of event sorted in descending order by timestamp
    """
    getEventJson = getWrapperAPI.getEvent()
    with open('eventList.json', 'w', encoding='utf-8') as outfile:
        json.dump(getEventJson, outfile, skipkeys=True, indent=2, ensure_ascii=True, separators=(',', ':'))
    print("printing list of events")
    print(getEventJson)
    
    """
    Retrieves a list of event after specified time
    """
    getEventTimeStampJson = getWrapperAPI.getEventTimeStamp('2017-03-01')
    with open('eventListTimeStamp.json', 'w', encoding='utf-8') as outfile:
        json.dump(getEventTimeStampJson, outfile, skipkeys=True, indent=2, ensure_ascii=True, separators=(',', ':'))
    print("printing list of events after specified time")
    print(getEventTimeStampJson)


    """
    Retrieves a list of computers with given connector_guid
    """
    getComputersConnectorGuidJson = getWrapperAPI.getComputersConnectorGuid('5be84e5c-2c2f-40f6-bcc6-3a53cd335b3f')
    with open('computerListGuid.json', 'w', encoding='utf-8') as outfile:
        json.dump(getComputersConnectorGuidJson, outfile, skipkeys=True, indent=2, ensure_ascii=True, separators=(',', ':'))
    print("printing list of computers with given guid")
    print(getComputersConnectorGuidJson)

    """
    Retrieves a list of computers that has observed files with given file name
    """
    getComputerActivityFileNameJson = getWrapperAPI.getComputerActivityFileName('wsymqyv90.exe')
    with open('computerListFileName.json', 'w', encoding='utf-8') as outfile:
        json.dump(getComputerActivityFileNameJson, outfile, skipkeys=True, indent=2, ensure_ascii=True, separators=(',', ':'))
    print("printing list of computers with given filename")
    print(getComputerActivityFileNameJson)

if __name__ == '__main__':
    sys.exit(main())