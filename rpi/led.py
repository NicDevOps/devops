import RP1.GPIO as GPIO
import time

GPIO.setwarnings(false)
GPIO.setmode(GPIO.BOARD)

ledPin = 12

GPIO.setup(ledpin, GPIO.OUT)

fori in range(5):

print("LED turning on")
GPIO.output(ledpin, GPIO.HIGH)
time.sleep(0.5)

print("LED turning off")
GPIO.output(ledpin, GPIO.LOW)
time.sleep(0.5)