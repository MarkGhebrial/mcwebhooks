import subprocess
from time import sleep

class ServerWrapper:
    def __init__ (self, command = 'java -Xmx1024M -Xms1024M -jar server.jar nogui'):
        self.command = command
        self.isRunning = False

    def start (this):
        this.process = subprocess.Popen(this.command,
                         stdout=subprocess.PIPE,
                         stdin=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=False,
                         encoding='utf-8')
        #this.isRunning = True

    def getOutput (this):
        return this.process.stdout.read()

    def sendCommand (this, command):
        this.process.stdin.write((command+ "\n"))

if __name__ == "__main__":
    s = ServerWrapper('java -Xmx1024M -Xms1024M -jar server.jar')
    s.start()
    print('hello?')
    while(True):
        print(s.getOutput())
        sleep(.1)