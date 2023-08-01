# Prisma Cloud API Utils
*Helper Methods and Example Code for getting started with Prisma Cloud APIs*

## Usage

* Set the base URL for Prisma Cloud API (NOTE: both can be set):
  * **CSPM_BASE_URL** `export CSPM_BASE_URL=https://api.prismacloud.io/`
  
  and/or
  * **CWP_BASE_URL** `export CWP_BASE_URL=https://us-west1.cloud.twistlock.com/us-1-2345678`

* Set the following required environment variable(s) for auth: 
  * **KEY_FILE** (string) a file path to Prisma Cloud API key file in .csv format `/path/to/file`

  or
  * **KEY_ID** (string) and **SECRET_KEY** (string) sourced from API Key File

* Use the helper methods to authenticate (login/renew) to Prisma Cloud and retreive an API Token

## Example

* Set token value to env_var in CLI to make subsequent API calls with another script/cURL:

`export CWP_TOKEN=$(python login_cwp.py)`

* Auth and renew within python script by importing 
``` 
import prisma_utils

TOKEN = prisma_utils.cspm_login()
# make some API calls ... iterate over results ... minutes go by ... 
response = requests.request("POST", BASE_URL+"/resource", headers=headers, json=payload)
...
...

TOKEN = prisma_utils.cspm_renew(TOKEN)

```

## More
For a robust Python SDK: https://github.com/PaloAltoNetworks/prismacloud-api-python
