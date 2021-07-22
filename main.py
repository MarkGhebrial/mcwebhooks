import json
import time

from webhook import Webhook

# Load config file
f = open('config.json', 'r')
config = json.load(f)

wHook = Webhook(config["webhookURL"])

lastLogEntries =[]
while True:
    log = open(config["serverDirectory"] + '/logs/latest.log', 'r')

    logEntries = []
    for line in log:
        logEntries.append(line)
    
    if len(logEntries) > len(lastLogEntries):
        wHook.postMessage(logEntries[len(logEntries) - 1])

    lastLogEntries = logEntries