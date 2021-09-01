import requests
import json

linkRequest = {
  "destination": "https://github.com/scott-a-code?tab=repositories"
  , "domain": { "fullName": "rebrand.ly" }
}

requestHeaders = {
  "Content-type": "application/json",
  "apikey": "4136a72da0db4073bcf211340b9cfb0c",
}

r = requests.post("https://api.rebrandly.com/v1/links", 
    data = json.dumps(linkRequest),
    headers=requestHeaders)

if (r.status_code == requests.codes.ok):
    link = r.json()
    print("Long URL was %s, short URL is %s" % (link["destination"], link["shortUrl"]))
else:
    print('Sorry there has been the following http error: ' + {{r.status_code}})