from prisma_utils import prisma_utils
import json
import os
import requests

BASE_URL = os.environ.get("CSPM_BASE_URL") # optional / local override of CSPM_BASE_URL and/or CWP_BASE_URL in prisma_utils
TOKEN = prisma_utils.cspm_login()

# Get CSPM alerts using POST /v2/alerts, example contains filters and timerange

headers = {
  'Content-Type': 'application/json; charset=UTF-8',
  'Accept': '*/*',
  'x-redlock-auth': TOKEN
}

payload = { 
    "filters": 
    [ 
        { "name": "asset.severity",
          "operator": "=",
          "value": "high"
        }
    ] 
}

response = requests.request("POST", BASE_URL+"/v2/resource/scan_info", headers=headers, data=json.dumps(payload)) # or use json=payload

print(response.text)
