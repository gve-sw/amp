"""
AMP for Endpoints API
Author: Glenn Quah, Iman Arifin
Date 30 March 2017

Retrieves a list of event filtered by application_SHA256
"""

import requests

with open('settings.txt', 'r') as f:
    host = f.readline().replace('\n', '')
    user = f.readline().replace('\n', '')
    password = f.readline().replace('\n', '')
print(host, user, password)

SHA = '3372c1edab46837f1e973164fa2d726c5c5e17bcb888828ccd7c4dfcc234a370'
inputURL = '/events?application_sha256=' + SHA
url = 'http://' + host + '/v1' + '/' + inputURL
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Accept-Encoding': 'application/gzip'}
response = requests.get(url, auth=(user, password), headers=headers, verify=True)

print(response.json())