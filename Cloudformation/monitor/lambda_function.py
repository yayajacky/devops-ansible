import os
import certifi
import urllib3

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where()
)

# This is trigger when a record is inserted into DISCOVERY-TESTING table
def lambda_handler(event, context):
    print("HI, going to check status on HIT_URL: {}".format(os.environ.get('HIT_URL', None)))
    r = http.request('GET', os.environ.get('HIT_URL', None))
    print(r.status)
    if r.status == 200:
        print(r.data)
        return {"statusCode": 200, 'body': 'Nothing to report'}
    else:
        print("Oh no! Received {}".format(r.status))
        http.request('GET', os.environ.get('SLACK_URL', None))
        return {"statusCode": 200, "body": "notified slack"}
