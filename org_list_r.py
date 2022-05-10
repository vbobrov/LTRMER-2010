import requests
import json
import os

base_url="https://api.meraki.com/api/v1"
meraki_api_key=os.environ.get("MERAKI_API_KEY")

req=requests.get(f"{base_url}/organizations", \
                headers={
                    "Content-Type": "application/json",
                    "X-Cisco-Meraki-API-Key": meraki_api_key
                    }
                )

org_list=json.loads(req.text)
print("id,name")
for org in org_list:
    print(f"{org['id']},{org['name']}")