import requests
import json

url="https://webhook.site/eb21edee-955e-459d-aef3-d86e3a7da8c6"
post_data={
    "fname": "john",
    "lname": "smith"
}

req=requests.post(url, \
                headers={
                    "Content-Type": "application/json",
                    "API-Key": "password123"
                    },
                data=json.dumps(post_data)
                )

print(f"Response code: {req.status_code}")