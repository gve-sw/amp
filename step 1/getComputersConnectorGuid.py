"""
AMP for Endpoints API
Author: Glenn Quah
Date 30 March 2017

Retrieves a list of computers with given connector_guid
"""
import requests

with open('settings.txt', 'r') as f:
    host = f.readline().replace('\n', '')
    user = f.readline().replace('\n', '')
    password = f.readline().replace('\n', '')
print(host, user, password)

connectorGuid = '7a6d95ee-bc44-4039-b317-728ed5690481'
inputURL = '/computers/' + connectorGuid
url = 'http://' + host + '/v1' + '/' + inputURL
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Accept-Encoding': 'application/gzip'}
response = requests.get(url, auth=(user, password), headers=headers, verify=True)

print(response.json())