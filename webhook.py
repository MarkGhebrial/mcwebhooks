import requests

class Webhook:

    def __init__ (this, URL):
        this.URL = URL

    def postMessage (this, message):
        r = requests.post(this.URL, data = {'content': message})
        if not r.ok:
            print(r)
