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

payload = {
    "name": "test-new-key", # self
    "serviceAccountName": "vaultSA"  # self
}

# Create a new access key (for current user or specify above)
response = requests.request("POST", BASE_URL+"/access_keys", headers=headers, json=payload)
response.raise_for_status()
new_access_key = response.json()
print(f"DEBUG -- New Access Key created {new_access_key} \n Saving...")

# Validate key, then securely store the new access key and secret

# Replace the old access key with the new one in your application or script

# Deactivate or delete the old access key
# (Assuming you have stored the old key ID you want to deactivate or delete)
old_access_key_id = os.environ.get("ACCESS_KEY_ID")
delete_url = f"{BASE_URL}/access_keys/{old_access_key_id}"
print(f"DEBUG --  Deleting old Access Key {old_access_key_id} " )
#response = requests.delete(delete_url, headers=headers)
exit()
response.raise_for_status()

if response.status_code == 204:
    print("Old access key deactivated/deleted successfully.")
else:
    print("Failed to deactivate/delete old access key.")