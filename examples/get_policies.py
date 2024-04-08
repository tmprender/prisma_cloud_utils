from prisma_utils import prisma_utils
import json
import os
import requests

BASE_URL = os.environ.get("CSPM_BASE_URL") # optional / local override of CSPM_BASE_URL and/or CWP_BASE_URL in prisma_utils
TOKEN = prisma_utils.cspm_login()

headers = {
  'Accept': 'application/json',
  'x-redlock-auth': TOKEN
}

# list all platform policies
response = requests.request("GET", BASE_URL+"/policy", headers=headers, data={})
#print(response, response.text)

policies = response.json()

#print(policies)

pc_ckv = []
# find PC policies that map to checkov policies
for policy in policies:
    if policy['rule'].get('children') is not None:
        for child in policy['rule']['children']:
          if child.get("metadata").get("checkovId"):
              pc_ckv.append( {"policyId": policy['policyId'], "name": policy['name'], "checkovId": child['metadata']['checkovId']})

print("TOTAL: ", len(pc_ckv), "\n", json.dumps(pc_ckv))


