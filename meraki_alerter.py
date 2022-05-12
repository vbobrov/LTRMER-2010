import json
import requests
import base64
import os

def lambda_handler(event, context):
    webex_api_key=os.environ["webex_api_key"]
    recipient=os.environ["recipient"]
    if event['isBase64Encoded']:
        alert_body=json.loads(base64.b64decode(event["body"]))
    else:
        alert_body=json.loads(event["body"])
    requests.post(
        "https://webexapis.com/v1/messages",
        headers={
            "Authorization": f"Bearer {webex_api_key}"
        },
        data={
            "toPersonEmail": recipient,
            "markdown": alert_body["markdown"]
        }
    ).raise_for_status()
    return {
        'statusCode': 200,
        'body': json.dumps('Alert Processed')
    }
