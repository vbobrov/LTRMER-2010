import requests
import json
import os

url="https://webhook.site/eb21edee-955e-459d-aef3-d86e3a7da8c6"
post_data={
    "fname": "john",
    "lname": "smith"
}
api_key=os.envion.get("API_KEY")

req=requests.post(url, \
                headers={
                    "Content-Type": "application/json",
                    "API-Key": api_key
                    },
                data=json.dumps(post_data)
                )

print(f"Response code: {req.status_code}")