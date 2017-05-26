"""
AMP for Endpoints API
Author: Glenn Quah, Iman Arifin
Date 30 March 2017

Retrieves a list of file items associated with a specific file list with given file_list_guid
"""

import requests

with open('settings.txt', 'r') as f:
    host = f.readline().replace('\n', '')
    user = f.readline().replace('\n', '')
    password = f.readline().replace('\n', '')
print(host, user, password)

fileListGuid = 'd77abe3d-adfa-4d65-bdd9-ce32b157e7de'
inputURL = '/file_lists/' + fileListGuid +'/files'
url = 'http://' + host + '/v1' + '/' + inputURL
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Accept-Encoding': 'application/gzip'}
response = requests.get(url, auth=(user, password), headers=headers, verify=True)

print(response.json())