"""
AMP for Endpoints API
Retrieves list of computers
"""

import requests

host = 'api.apjc.amp.cisco.com'
user = '8a2a49f003566ed3fb0b'
password = '5d97572a-675f-40b6-a98c-2ba67b8e2c92'

SHA = '814a37d89a79aa3975308e723bc1a3a67360323b7e3584de00896fe7c59bbb8e'
inputURL = '/computers/activity?q=' + SHA
url = 'http://' + host + '/v1' + '/' + inputURL
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Accept-Encoding': 'application/gzip'}
response = requests.get(url, auth=(user, password), headers=headers, verify=True)

print(response.json())