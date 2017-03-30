"""
AMP for Endpoints API
Author: Glenn Quah
Date 30 March 2017

Retrieves a list of computers that has observed files with given file name
"""
import requests

with open('settings.txt', 'r') as f:
    host = f.readline().replace('\n', '')
    user = f.readline().replace('\n', '')
    password = f.readline().replace('\n', '')
print(host, user, password)

fileName = 'wsymqyv90.exe'
inputURL = '/computers/activity?q=' + fileName
url = 'http://' + host + '/v1' + '/' + inputURL
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Accept-Encoding': 'application/gzip'}
response = requests.get(url, auth=(user, password), headers=headers, verify=True)

print(response.json())