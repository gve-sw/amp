#
#   Cisco AMP for Endpoints Sample App v.02
#
#   Glenn Quah(glqjuah@cisco.com)
#   Vorachat Nantasupawatana (vnantasu@cisco.com)
#   Iman Arifin (imarifin@cisco.com)
#       Feb 2017
#
#       This class provides methods to facilitates
#       access to the Advanced Malware Protection for Endpoints API.
#
#   REQUIREMENTS:
#       Python requests library (issue the 'pip install requests' command in shell or cmd)
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

#host = '198.18.134.28:8080'
host = 'api.apjc.amp.cisco.com'
username = '8a2a49f003566ed3fb0b'
password = '5d97572a-675f-40b6-a98c-2ba67b8e2c92'

#username = 'badc2e9d062af26be4ad'
#password = 'ff7924e3-6e14-404e-b289-d5628b7de7ca'
#username = 'admin'
#password = 'admin'

class Wrapper_API(object) :
    """
    This class is used to interact with the NSO API
    """
    def __init__(self):
        self.host = host
        self.username = username
        self.password = password

    def send_api_request(self, phrase):
        """
        Sends a request to the API for retrieving data.
        """
        url = 'http://' + host + '/v1' + '/' + phrase
        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json',
                   'Accept-Encoding': 'application/gzip'
                   }
        response = requests.get(url, auth=(username, password),
                                headers=headers, verify=False)
        return response.text

    def getComputers(self):
        """
        Retrieves a list of computers
        """
        computersURL = '/computers'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getComputersConnectorGuid(self, connectorGuid):
        """
        Retrieves a list of computers with given connector_guid
        """
        #7a6d95ee-bc44-4039-b317-728ed5690481
        computersURL = '/computers/' + connectorGuid
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getComputersTrajectoryConnectorGuid(self, connectorGuid):
        """
        Retrieves specific computer's trajectory with given connector_guid
        """
        #7a6d95ee-bc44-4039-b317-728ed5690481
        computersURL = '/computers/' + connectorGuid + '/trajectory'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getComputerActivityFileName(self, fileName):
        """
        Retrieves a list of computers that has observed files with given file name
        """
        computersURL = '/computers/activity?q=' + fileName
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getComputerActivitySHA(self, SHA):
        """
        Retrieves a list of computers that has observed files with given SHA-256 value
        """
        #814a37d89a79aa3975308e723bc1a3a67360323b7e3584de00896fe7c59bbb8e
        computersURL = '/computers/activity?q=' + SHA
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getEvent(self):
        """
        Retrieves a list of event sorted in descending order by timestamp
        """
        computersURL = '/events'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getEventConnectorGuid(self, connectorGuid):
        """
        Retrieves a list of event filtered by connector guid
        """
        # 7a6d95ee-bc44-4039-b317-728ed5690481
        computersURL = '/events?connector_guid[]=' + connectorGuid
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getEventGroupGuid(self, groupGuid):
        """
        Retrieves a list of event filtered by group guid
        """
        #b077d6bc-bbdf-42f7-8838-a06053fbd98a
        computersURL = '/events?group_guid[]=' + groupGuid
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getEventDetectionSHA(self, SHA):
        """
        Retrieves a list of event filtered by detection_SHA256
        """
        #3372c1edab46837f1e973164fa2d726c5c5e17bcb888828ccd7c4dfcc234a370
        computersURL = '/events?detection_sha256=' + SHA
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getEventApplicationSHA(self, SHA):
        """
        Retrieves a list of event filtered by application_SHA256
        """
        #3372c1edab46837f1e973164fa2d726c5c5e17bcb888828ccd7c4dfcc234a370&
        computersURL = '/events?application_sha256=' + SHA
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getEventDectectionApplicationSHA(self, detectionSHA, applicationSHA):
        """
        Retrieves a list of event filtered by detection_SHA256 and application_SHA256
        """
        #detection_sha256=3372c1edab46837f1e973164fa2d726c5c5e17bcb888828ccd7c4dfcc234a370
        #application_sha256=3372c1edab46837f1e973164fa2d726c5c5e17bcb888828ccd7c4dfcc234a370
        computersURL = '/events?detection_sha256=' + detectionSHA + '&application_sha256=' + applicationSHA
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getEventTimeStamp(self, timeStamp):
        """
        Retrieves a list of event newer than a given timestamp
        """
        #2015-10-01
        computersURL = '/events?start_date=' + timeStamp
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getEventTypes(self):
        """
        Retrieves a list of event
        """
        computersURL = '/event_types'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getApplicationsBlockingList(self):
        """
        Retrieves a list of application_blocking file_lists
        """
        computersURL = '/file_lists/application_blocking'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getApplicationsBlockingFileListName(self, fileListName):
        """
        Retrieves a list of application_blocking file_lists filtered by name
        """
        #Block_Vorachat
        computersURL = '/file_lists/application_blocking?name[]=' + fileListName
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getApplicationsBlockingFileListGuid(self, fileListGuid):
        """
        Retrieves a list of application_blocking file_lists with given file_list_guid
        """
        #d77abe3d-adfa-4d65-bdd9-ce32b157e7de
        computersURL = '/file_lists/' + fileListGuid
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getCustomDetectionFileListGuid(self, fileListGuid):
        """
        Retrieves simple_custom_detection file list with given file_list_guid
        """
        computersURL = '/file_lists/' + fileListGuid
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getFileListItemFileListGuid(self, fileListGuid):
        """
        Retrieves a list of file items associated with a specific file list with given file_list_guid
        """
        #d77abe3d-adfa-4d65-bdd9-ce32b157e7de
        computersURL = '/file_lists/' + fileListGuid +'/files'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getFileListItemSHAFileListGuid(self, SHA, fileListGuid):
        """
        Retrieves a list of file items with a given SHA-256 and associated with file list for given file_list_guid
        """
        computersURL = '/file_lists/' + fileListGuid + 'files/' + SHA
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getGroups(self):
        """
        Retrieves a list of group
        """
        computersURL = '/groups'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getGroupsGroupGuid(self, groupGuid):
        """
        Retrieves a list group with given group_guid
        """
        #b077d6bc-bbdf-42f7-8838-a06053fbd98a
        computersURL = '/groups/' + groupGuid
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getPolicy(self):
        """
        Retrieves a list of policy
        """
        computersURL = '/policies'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getPolicyPolicyGuid(self, policyGuid):
        """
        Retrieves a list of policy for given policy_guid
        """
        #89912c9e-8dbd-4c2b-a1d8-dee8a0c2bb29
        computersURL = '/policies/' + policyGuid
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

    def getVersion(self):
        """
        Retrieves a list of event
        """
        computersURL = '/version'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(computersURL)
        return apiResponse

