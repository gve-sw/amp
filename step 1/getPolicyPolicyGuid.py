"""
AMP for Endpoints API
Author: Glenn Quah, Iman Arifin
Date 30 March 2017

Retrieves a list of policy for given policy_guid
"""

import requests

with open('settings.txt', 'r') as f:
    host = f.readline().replace('\n', '')
    user = f.readline().replace('\n', '')
    password = f.readline().replace('\n', '')
print(host, user, password)

policyGuid = '89912c9e-8dbd-4c2b-a1d8-dee8a0c2bb29'
inputURL = '/policies/' + policyGuid
url = 'http://' + host + '/v1' + '/' + inputURL
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Accept-Encoding': 'application/gzip'}
response = requests.get(url, auth=(user, password), headers=headers, verify=True)

print(response.json())