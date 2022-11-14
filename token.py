import requests
import json
from getpass import getpass
from requests.auth import HTTPBasicAuth

USER = input('Enter your username for DNAC: ')
PASS = getpass('Enter your pasword for DNAC: ')

BASEURL = 'https://sandboxdnac.cisco.com'
#authAPI = '/dna/intent/api/v1/certificate'
authAPI = '/dna/system/api/v1/auth/token'

payload={}
headers = {
	'Content-Type': 'application/json',
	'Accept': 'application/json'
#	'Authorization': 'Basic ZGV2bMv0DxnLCJPdAXNJBZeYmYe=' 
	}

dnaAuth = BASEURL + authAPI

response = requests.post(dnaAuth, auth=HTTPBasicAuth(USER, PASS), headers=headers, data=payload)

TOKEN = tokenJSON['Token']

print('Your token was successfully generated. The value of your token is:\n' + TOKEN)
