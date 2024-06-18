from prisma_utils import prisma_utils
import json
import os
import requests
import urllib3 

# stop no cert warning
urllib3.disable_warnings()

BASE_URL = os.environ.get("CWP_BASE_URL") # optional / local override of CSPM_BASE_URL and/or CWP_BASE_URL in prisma_utils
TOKEN = prisma_utils.cwp_login()

# list images from Prisma Cloud Compute (CWP/Twistlock)

headers = {'Accept': 'application/json', "Authorization": "Bearer " + TOKEN}
querystring = {"sort":"scanTime", "timeType":"relative", "timeAmount": "1", "timeUnit": "day"}

response = requests.request("GET", BASE_URL+"/api/v1/audits/runtime/host", headers=headers, params=querystring, verify=False)
print(response.text)
#print(response, response.text)