import prisma_utils
import time

# example of using helper methods to renew token for CWP
def renew_cwp_token():
    #print("TOKEN BEFORE: ", prisma_utils.CWP_TOKEN)
    response = prisma_utils.cwp_api(endpoint="/authenticate/renew", request_type="GET", querystring={})
    # update runtime variable - classless, only updates for running process
    prisma_utils.CWP_TOKEN = response.json().get("token")

# example script
prisma_utils.cwp_api("/hosts", "GET", {})
prisma_utils.cspm_api("/cloud", "GET", {})
time.sleep(120)  # simulate delay between API calls
renew_cwp_token()
prisma_utils.cwp_api("/defenders", "GET", {})
