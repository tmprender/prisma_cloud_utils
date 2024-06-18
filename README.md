# Prisma Cloud API Utils
*Helper Methods and Example Code for getting started with Prisma Cloud APIs*

## Setup

`git clone https://github.com/tmprender/prisma_cloud_utils.git`

`pip install prisma_cloud_utils/` 

`pip install -r prisma_cloud_utils/requirements.txt` 

## Usage

* Set the base URL for Prisma Cloud API (NOTE: both can be set):
  * **CSPM_BASE_URL** `export CSPM_BASE_URL=https://api.prismacloud.io/`
  
  and/or
  * **CWP_BASE_URL** `export CWP_BASE_URL=https://us-west1.cloud.twistlock.com/us-1-2345678`

* Set the file path to Prisma Cloud API creds (.csv file downloaded from management cosole): 
  * **PRISMA_KEY_FILE** `export PRISMA_KEY_FILE=/full/path/to/cred_file.csv`

  
  * Optionally set **KEY_ID**  and **SECRET_KEY** directly instead of reading from key file

* Use the helper methods to authenticate (login/renew) to Prisma Cloud and retreive an API Token

## Example

* Set token value to env_var in CLI to make subsequent API calls with another script/cURL:

`export CWP_TOKEN=$(python login_cwp.py)`

* Auth and renew within python script by importing (clone and install with pip)
``` 
from primsa_utils import prisma_utils

TOKEN = prisma_utils.cspm_login()
# make some API calls ... iterate over results ... minutes go by ... 
response = requests.request("POST", BASE_URL+"/resource", headers=headers, json=payload)
...
...

TOKEN = prisma_utils.cspm_renew(TOKEN)

```

## More
For a robust Python SDK: https://github.com/PaloAltoNetworks/prismacloud-api-python
