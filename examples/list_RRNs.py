from prisma_utils import prisma_utils
import os
import requests
import time
import json

BASE_URL = os.environ.get("BASE_URL") # optional / local override of CSPM_BASE_URL and/or CWP_BASE_URL in prisma_utils
TOKEN = prisma_utils.cspm_login()

# list RRNs and iterate over each resource, benchmark 'RRN count', 'starttime' and 'endtime'

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'x-redlock-auth': TOKEN
}

querystring = {"timeType":"relative", "timeAmount": "2", "timeUnit": "minute"}

response = requests.request("GET", BASE_URL+"/resource/scan_info", headers=headers, data=json.dumps(querystring))
#print(response.text)  # for jq testing
resources = response.json().get("resources")
rrnList = []
for resource in resources:
    if resource.get('rrn') is not None:
        rrnList.append(resource['rrn'])

print("COUNT: ", len(rrnList))

start = time.time()

for rrn in rrnList:
    payload = {"rrn": rrn }
    response = requests.request("POST", BASE_URL+"/resource", headers=headers, json=payload)
    print(response, response.text, "\n")

end = time.time()

print("COUNT: ", len(rrnList), "\nSTART: ", start, "\nEND: ", end)