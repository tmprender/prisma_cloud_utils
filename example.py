import prisma_utils
import time


# # # # # # # # # #
# Example scripts #
# # # # # # # # # #

# CSPM examples
response = prisma_utils.cspm_api(endpoint="/check", request_type="GET")
print(response.text, "\n")



# Code Security examples - uses CSPM API URL
response = prisma_utils.cspm_api("/code/api/v1/repositories", "GET")
repos = response.json()
print(repos, "\n")
for repo in repos:
    payload = {"repository": repo["owner"] +"/"+ repo["repository"], "sourceTypes": [ repo["source"] ]}
    response = prisma_utils.cspm_api("/code/api/v1/errors/files", "POST", {}, payload)  # {} = empty QueryString positional arg
    print(response.text, response, "\n")



# CWP examples
response = prisma_utils.cwp_api("/images", "GET", querystring={"sort":"scanTime"})
# curl equivalent -> curl -k -H "Authorization: Bearer $CWP_TOKEN" -X GET $CWP_BASE_URL/api/v1/images?sort="scanTime"

# use a helper method to renew token for CWP
def renew_cwp_token():
    response = prisma_utils.cwp_api(endpoint="/authenticate/renew", request_type="GET", querystring={})
    # update runtime variable - only updates for running process, not persistent on OS/shell env var
    prisma_utils.CWP_TOKEN = response.json().get("token")

print("doing some analysis...")
time.sleep(5)  # simulate delay, token nearing expiration...
print("refreshing token")
renew_cwp_token()

# formatting examples - filter results for last hour
querystring = {"timeType":"relative", "timeAmount": "1", "timeUnit": "hour"}
response = prisma_utils.cwp_api("/images", "GET", querystring)
print(response.text)

