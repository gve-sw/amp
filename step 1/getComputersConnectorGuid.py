"""
AMP for Endpoints API
Retrieves list of computers
"""

import requests

host = 'api.apjc.amp.cisco.com'
user = '8a2a49f003566ed3fb0b'
password = '5d97572a-675f-40b6-a98c-2ba67b8e2c92'

connectorGuid = '7a6d95ee-bc44-4039-b317-728ed5690481'
inputURL = '/computers/' + connectorGuid
url = 'http://' + host + '/v1' + '/' + inputURL
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Accept-Encoding': 'application/gzip'}
response = requests.get(url, auth=(user, password), headers=headers, verify=True)

print(response.json())