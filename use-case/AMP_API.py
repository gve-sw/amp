#
#   Cisco AMP for Endpoints Sample App
#       v.03
#
#   Glenn Quah (glquah@cisco.com)
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

import requests

def send_api_request(phrase, host, username, password):
    """
    Sends a request to the API for retrieving data.
    """
    url = 'http://' + host + '/v1' + '/' + phrase
    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json',
               'Accept-Encoding': 'application/gzip'
               }
    response = requests.get(url, auth=(username, password),
                            headers=headers, verify=True)
    return response.json()

class Wrapper(object) :
    """
    This class is used to interact with the AMP API
    """
    def __init__(self, hostname, username, password):
        self.host = hostname
        self.username = username
        self.password = password



    def getComputers(self):
        """
        Retrieves a list of computers
        """
        inputURL = '/computers'
        apiResponse = send_api_request(inputURL, self.host, self.username, self.password)
        return apiResponse

    def getComputersConnectorGuid(self, connectorGuid):
        """
        Retrieves a list of computers with given connector_guid
        """
        #7a6d95ee-bc44-4039-b317-728ed5690481
        inputURL = '/computers/' + connectorGuid
        apiResponse = send_api_request(inputURL, self.host, self.username, self.password)
        return apiResponse

    def getComputersTrajectoryConnectorGuid(self, connectorGuid):
        """
        Retrieves specific computer's trajectory with given connector_guid
        """
        #7a6d95ee-bc44-4039-b317-728ed5690481
        inputURL = '/computers/' + connectorGuid + '/trajectory'
        apiResponse = send_api_request(inputURL, self.host, self.username, self.password)
        return apiResponse

    def getComputersActivityFileName(self, fileName):
        """
        Retrieves a list of computers that has observed files with given file name
        """
        inputURL = '/computers/activity?q=' + fileName
        apiResponse = send_api_request(inputURL, self.host, self.username, self.password)
        return apiResponse

    def getComputersActivitySHA(self, SHA):
        """
        Retrieves a list of computers that has observed files with given SHA-256 value
        """
        #814a37d89a79aa3975308e723bc1a3a67360323b7e3584de00896fe7c59bbb8e
        inputURL = '/computers/activity?q=' + SHA
        apiResponse = send_api_request(inputURL, self.host, self.username, self.password)
        return apiResponse

    def getEvent(self):
        """
        Retrieves a list of event sorted in descending order by timestamp
        """
        inputURL = '/events'
        apiResponse = send_api_request(inputURL, self.host, self.username, self.password)
        return apiResponse

    def getEventConnectorGuid(self, connectorGuid):
        """
        Retrieves a list of event filtered by connector guid
        """
        # 7a6d95ee-bc44-4039-b317-728ed5690481
        inputURL = '/events?connector_guid[]=' + connectorGuid
        apiResponse = send_api_request(inputURL, self.host, self.username, self.password)
        return apiResponse

    def getEventGroupGuid(self, groupGuid):
        """
        Retrieves a list of event filtered by group guid
        """
        #b077d6bc-bbdf-42f7-8838-a06053fbd98a
        inputURL = '/events?group_guid[]=' + groupGuid
        apiResponse = send_api_request(inputURL, self.host, self.username, self.password)
        return apiResponse

    def getEventDetectionSHA(self, SHA):
        """
        Retrieves a list of event filtered by detection_SHA256
        """
        #3372c1edab46837f1e973164fa2d726c5c5e17bcb888828ccd7c4dfcc234a370
        inputURL = '/events?detection_sha256=' + SHA
        apiResponse = send_api_request(inputURL, self.host, self.username, self.password)
        return apiResponse

    def getEventApplicationSHA(self, SHA):
        """
        Retrieves a list of event filtered by application_SHA256
        """
        #3372c1edab46837f1e973164fa2d726c5c5e17bcb888828ccd7c4dfcc234a370&
        inputURL = '/events?application_sha256=' + SHA
        apiResponse = send_api_request(inputURL, self.host, self.username, self.password)
        return apiResponse

    def getEventDectectionApplicationSHA(self, detectionSHA, applicationSHA):
        """
        Retrieves a list of event filtered by detection_SHA256 and application_SHA256
        """
        #detection_sha256=3372c1edab46837f1e973164fa2d726c5c5e17bcb888828ccd7c4dfcc234a370
        #application_sha256=3372c1edab46837f1e973164fa2d726c5c5e17bcb888828ccd7c4dfcc234a370
        inputURL = '/events?detection_sha256=' + detectionSHA + '&application_sha256=' + applicationSHA
        apiResponse = send_api_request(inputURL, self.host, self.username, self.password)
        return apiResponse

    def getEventTimeStamp(self, timeStamp):
        """
        Retrieves a list of event newer than a given timestamp
        """
        #2015-10-01
        inputURL = '/events?start_date=' + timeStamp
        apiResponse = send_api_request(inputURL, self.host, self.username, self.password)
        return apiResponse

    def getEventTypes(self):
        """
        Retrieves a list of event
        """
        inputURL = '/event_types'
        apiResponse = send_api_request(inputURL, self.host, self.username, self.password)
        return apiResponse

    def getApplicationsBlockingList(self):
        """
        Retrieves a list of application_blocking file_lists
        """
        inputURL = '/file_lists/application_blocking'
        apiResponse = send_api_request(inputURL, self.host, self.username, self.password)
        return apiResponse

    def getApplicationsBlockingFileListName(self, fileListName):
        """
        Retrieves a list of application_blocking file_lists filtered by name
        """
        #Block_Vorachat
        inputURL = '/file_lists/application_blocking?name[]=' + fileListName
        apiResponse = send_api_request(inputURL, self.host, self.username, self.password)
        return apiResponse

    def getApplicationsBlockingFileListGuid(self, fileListGuid):
        """
        Retrieves a list of application_blocking file_lists with given file_list_guid
        """
        #d77abe3d-adfa-4d65-bdd9-ce32b157e7de
        inputURL = '/file_lists/' + fileListGuid
        apiResponse = send_api_request(inputURL, self.host, self.username, self.password)
        return apiResponse

    def getCustomDetectionFileListGuid(self, fileListGuid):
        """
        Retrieves simple_custom_detection file list with given file_list_guid
        """
        inputURL = '/file_lists/' + fileListGuid
        apiResponse = send_api_request(inputURL, self.host, self.username, self.password)
        return apiResponse

    def getFileListItemFileListGuid(self, fileListGuid):
        """
        Retrieves a list of file items associated with a specific file list with given file_list_guid
        """
        #d77abe3d-adfa-4d65-bdd9-ce32b157e7de
        inputURL = '/file_lists/' + fileListGuid +'/files'
        apiResponse = send_api_request(inputURL, self.host, self.username, self.password)
        return apiResponse

    def getFileListItemSHAFileListGuid(self, SHA, fileListGuid):
        """
        Retrieves a list of file items with a given SHA-256 and associated with file list for given file_list_guid
        """
        inputURL = '/file_lists/' + fileListGuid + 'files/' + SHA
        apiResponse = send_api_request(inputURL, self.host, self.username, self.password)
        return apiResponse

    def getGroups(self):
        """
        Retrieves a list of group
        """
        inputURL = '/groups'
        apiResponse = send_api_request(inputURL, self.host, self.username, self.password)
        return apiResponse

    def getGroupsGroupGuid(self, groupGuid):
        """
        Retrieves a list group with given group_guid
        """
        #b077d6bc-bbdf-42f7-8838-a06053fbd98a
        inputURL = '/groups/' + groupGuid
        apiResponse = send_api_request(inputURL, self.host, self.username, self.password)
        return apiResponse

    def getPolicy(self):
        """
        Retrieves a list of policy
        """
        inputURL = '/policies'
        apiResponse = send_api_request(inputURL, self.host, self.username, self.password)
        return apiResponse

    def getPolicyPolicyGuid(self, policyGuid):
        """
        Retrieves a list of policy for given policy_guid
        """
        #89912c9e-8dbd-4c2b-a1d8-dee8a0c2bb29
        inputURL = '/policies/' + policyGuid
        apiResponse = send_api_request(inputURL, self.host, self.username, self.password)
        return apiResponse

    def getVersion(self):
        """
        Retrieves the version
        """
        inputURL = '/version'
        apiResponse = send_api_request(inputURL, self.host, self.username, self.password)
        return apiResponse

