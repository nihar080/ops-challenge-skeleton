import requests
import json
import os
import sys, getopt


node_api_endpoint = "https://rpc.cosmos.network/block_results?height"

res = requests.get(url = node_api_endpoint, headers = {"Content-Type":"application/json"}, verify=True)

result_data = res.json()
print(result_data['result']['height'])

print(res.status_code)

# with open('/mnt/c/Users/sahun/Downloads/ops-challenge-skeleton/ops-challenge-skeleton/playbooks/roles/cosmos/templates/test_details.json') as json_file:
#     data = json.load(json_file)
 
#     # Print the type of data variable
#     print(type(data['peers']['seeds']))

#     printable_str = ""
#     for items in data['peers']['seeds']:
#         printable_str = printable_str + f",{items['id']}@{items['address']}"

#     print(printable_str)
#     printable_str2 = ""
#     for items in data['peers']['persistent_peers']:
#         printable_str2 = printable_str2 + f",{items['id']}@{items['address']}"

#     print(printable_str2)





# nd_url = "https://github.com/cosmos/chain-registry/blob/master/cosmoshub/chain.json"

# res = requests.get(url = nd_url, headers = {"Content-Type":"application/json"}, verify=True)
# print(res)
# result_data = res.json()
# print(result_data)

# print(dir(res))
