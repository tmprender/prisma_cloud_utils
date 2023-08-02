from prisma_utils import prisma_utils
import urllib3

# stop no cert warning
urllib3.disable_warnings()

# prints token to stdout - pipe to env_var
print(prisma_utils.cwp_login())