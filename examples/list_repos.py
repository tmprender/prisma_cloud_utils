from prisma_utils import prisma_utils
import json
import os
import requests

BASE_URL = os.environ.get("BASE_URL") # optional / local override of CSPM_BASE_URL and/or CWP_BASE_URL in prisma_utils
TOKEN = prisma_utils.cspm_login()

headers = {
  'Accept': 'application/json',
  'authorization': TOKEN
}

# list all integrated code repositories
response = requests.request("GET", BASE_URL+"/code/api/v1/repositories", headers=headers, data={})
print(response, response.text)

repos = response.json()

# iterte over repos and find violations within
for repo in repos:
    # format components of previous respone for required format of next logical request - silly API...
    payload = {"repository": repo["owner"] +"/"+ repo["repository"], "sourceTypes": [ repo["source"] ]}
    response = requests.request("POST", BASE_URL+"/code/api/v1/errors/files", headers=headers, data=payload)
    print(response, response.text, "\n")

    

