from datetime import datetime
from time import sleep
import signal
import sys

def handler(signum, frame):
    print('shutting down')
    sys.exit(99)

signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)

print('running')

while True:
    print('hello world: ' + str(datetime.now()))
    sleep(1)
