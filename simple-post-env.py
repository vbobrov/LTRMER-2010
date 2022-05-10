import requests
import json
import os

url=os.environ.get("URL")
api_key=os.environ.get("API_KEY")
post_data={
    "fname": "john",
    "lname": "smith"
}

req=requests.post(url, \
                headers={
                    "Content-Type": "application/json",
                    "API-Key": api_key
                    },
                data=json.dumps(post_data)
                )

print(f"Response code: {req.status_code}")