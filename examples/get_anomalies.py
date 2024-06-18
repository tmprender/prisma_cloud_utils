from prisma_utils import prisma_utils
import json
import os
import requests

BASE_URL = os.environ.get("CSPM_BASE_URL") # optional / local override of CSPM_BASE_URL and/or CWP_BASE_URL in prisma_utils
TOKEN = prisma_utils.cspm_login()

# Get anomalies, example contains filters and timerange

headers = {
  'Accept': 'application/json; charset=UTF-8',
  'x-redlock-auth': TOKEN
}

payload = {}
querystring = {"type": "dns"}

response = requests.request("GET", BASE_URL+"/anomalies/settings", headers=headers, params=querystring, json=(payload)) # or use json=payload

print(response.text)

# alerts = response.json()
# print(alerts)

