"""
AMP for Endpoints API
Author: Glenn Quah, Iman Arifin
Date 30 March 2017

Retrieves a list group with given group_guid
"""

import requests

with open('settings.txt', 'r') as f:
    host = f.readline().replace('\n', '')
    user = f.readline().replace('\n', '')
    password = f.readline().replace('\n', '')
print(host, user, password)

groupGuid = 'b077d6bc-bbdf-42f7-8838-a06053fbd98a'
inputURL = '/groups/' + groupGuid
url = 'http://' + host + '/v1' + '/' + inputURL
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Accept-Encoding': 'application/gzip'}
response = requests.get(url, auth=(user, password), headers=headers, verify=True)

print(response.json())