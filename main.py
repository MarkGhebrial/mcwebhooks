import json
import time

from webhook import Webhook

# Load config file
f = open('config.json', 'r')
config = json.load(f)

wHook = Webhook(config["webhookURL"])

logPath = config["serverDirectory"] + '/logs/latest.log'

lastLogEntries =[]
while True:
    try:
        log = open(logPath, 'r')

        logEntries = []
        for line in log:
            logEntries.append(line)

        if len(logEntries) > len(lastLogEntries):
            wHook.postMessage(logEntries[len(logEntries) - 1])

        lastLogEntries = logEntries

        log.close()
    except FileNotFoundError:
        print("File '%s' not found, trying again in 5 seconds" %logPath)
        time.sleep(5)
        
