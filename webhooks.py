import requests

webhookURL = 'https://discordapp.com/api/webhooks/867812946171658310/TMLUAz_8s6VhaZTtra-IO0yfOWptnBWZuFrqyT-xnBnKjxUJ_wCc5iRK1mziJ_AeQjQs'

for i in range(5):
    r = requests.post(webhookURL, data = {'content': i})
    print(r)
