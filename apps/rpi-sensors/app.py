from prometheus_client import start_http_server, Gauge
import Adafruit_DHT
import time
import RPi.GPIO as GPIO, time, os

GPIO.setmode(GPIO.BCM)

t = Gauge('temperature', 'Temperature')
h = Gauge('humidity', 'Humidity')
i = Gauge('illuminance', 'Illuminance')


def RCtime(RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(RCpin, GPIO.IN)
    # This takes about 1 millisecond per loop cycle
    while GPIO.input(RCpin) == GPIO.LOW:
        reading += 1
    return reading


start_http_server(5000)
while True:

    try:
        humidity, temperature = Adafruit_DHT.read_retry(22, 17)
        illuminance = RCtime(22)
    except Exception as e:
        print('!!!! we caught an exception !!!!')
        print(e)

    if temperature:
        t.set(temperature)

    if humidity:
        h.set(humidity)
    
    i.set(999)

    if temperature and humidity:
        print(f'temperature: {temperature}\nhumidity: {humidity}\nilluminance: {illuminance}')

    time.sleep(1)

