#
#   Cisco AMP for Endpoints Sample App
#       v.02
#
#   Glenn Quah(glqjuah@cisco.com)
#   Vorachat Nantasupawatana (vnantasu@cisco.com)
#   Iman Arifin (imarifin@cisco.com)
#       Feb 2017
#
#       This class provides methods to facilitates
#       access to the Network Services Orchestrator API.
#
#   REQUIREMENTS:
#       Python sys library
#       NSO Wrapper_API module to access the NSO API
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
from Wrapper_API import  Wrapper_API

# NOT ABLE TO WORK IF DCLOUD IS NOT RUNNING
def main():
    """
    Main method for our initializing our Wrapper API and calling functions
    """
    getWrapperAPI = Wrapper_API()

    """
    Retrieves a list of computers
    """
    getComputersStr = getWrapperAPI.getComputers()
    getComputersJson = json.loads(getComputersStr)
    with open('getComputers.json', 'w', encoding='utf-8') as outfile:
        json.dump(getComputersJson, outfile, skipkeys=True, indent=2, ensure_ascii=True, separators=(',',':'))
    print("printing list of computers")
    print(getComputersJson)

    """
    Retrieves a list of computers with given connector_guid
    """
    getComputersConnectorGuidStr = getWrapperAPI.getComputersConnectorGuid('7a6d95ee-bc44-4039-b317-728ed5690481')
    getComputersConnectorGuidJson = json.loads(getComputersConnectorGuidStr)
    with open('getComputersGuid.json', 'w', encoding='utf-8') as outfile:
        json.dump(getComputersConnectorGuidJson, outfile, skipkeys=True, indent=2, ensure_ascii=True, separators=(',',':'))
    print("printing list of computers with given guid")
    print(getComputersConnectorGuidJson)

    """
    Retrieves a list of computers that has observed files with given file name
    """
    getComputerActivityFileNameStr = getWrapperAPI.getComputerActivityFileName('SearchProtocolHost.exe')
    getComputerActivityFileNameJson = json.loads(getComputerActivityFileNameStr)
    with open('getComputerActivityFileName.json', 'w', encoding='utf-8') as outfile:
        json.dump(getComputerActivityFileNameJson, outfile, skipkeys=True, indent=2, ensure_ascii=True, separators=(',',':'))
    print(getComputerActivityFileNameJson)

    """
    Retrieves a list of event sorted in descending order by timestamp
    """
    getEventStr = getWrapperAPI.getEvent()
    getEventJson = json.loads(getEventStr)
    with open('getEvent.json', 'w', encoding='utf-8') as outfile:
        json.dump(getEventJson, outfile, skipkeys=True, indent=2, ensure_ascii=True, separators=(',',':'))
    print(getEventJson)


if __name__ == '__main__':
    sys.exit(main())