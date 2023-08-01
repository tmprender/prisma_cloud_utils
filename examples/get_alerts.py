import prisma_utils
import json
import time
import os
import requests

BASE_URL = os.environ.get("BASE_URL") # optional / local override of CSPM_BASE_URL and/or CWP_BASE_URL in prisma_utils
TOKEN = os.environ.get("TOKEN")

# Get CSPM alerts using POST /v2/alerts, example contains filters and timerange

headers = {
  'Content-Type': 'application/json; charset=UTF-8',
  'Accept': '*/*',
  'x-redlock-auth': TOKEN
}

payload = {
    "detailed": "true",
    "filters": [
        {
            "name": "alert.status",
            "operator": "=",
            "value": "resolved"
        }
    ],
    "timeRange": {
        "type": "relative",
        "value": {
            "amount": 1,
            "unit": "day"
        }
    }
}

response = requests.request("POST", BASE_URL+"/v2/alert", headers=headers, data=json.dumps(payload)) # or use json=payload

print(response, response.text)

alerts = response.json()
print(alerts)

