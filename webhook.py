import requests
import time
import json

class Webhook:

    def __init__ (this, URL):
        this.URL = URL

    def postMessage (this, message):
        r = requests.post(this.URL, data = {'content': message})
        if not r.ok:
            
            # Handle reaching rate limits
            if r.status_code == 429:
                seconds = json.loads(r.text)["retry_after"]
                print("Rate limited for %s seconds" %seconds)
                # Pause until rate limiting expires
                time.sleep(seconds)
                
            print("%s, %r" %(r.status_code, r.reason))
            print(r.text)
