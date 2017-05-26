"""
AMP for Endpoints API
Author: Glenn Quah, Iman Arifin
Date 30 March 2017

Retrieves a list of application_blocking file_lists filtered by name
"""

import requests

with open('settings.txt', 'r') as f:
    host = f.readline().replace('\n', '')
    user = f.readline().replace('\n', '')
    password = f.readline().replace('\n', '')
print(host, user, password)

fileListName = 'Block_Vorachat'
inputURL = '/file_lists/application_blocking?name[]=' + fileListName
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Accept-Encoding': 'application/gzip'}
response = requests.get(url, auth=(user, password), headers=headers, verify=True)

print(response.json())