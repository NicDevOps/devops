from prometheus_client import start_http_server, Gauge
import Adafruit_DHT
import time

t = Gauge('temperature', 'Temperature')
h = Gauge('humidity', 'Humidity')

start_http_server(5000)
while True:

    try:
      humidity, temperature = Adafruit_DHT.read_retry(11, 17)
    except Exception as e:
        print('!!!! we caught an exception !!!!')
        print(e)

    t.set(temperature)
    h.set(humidity)

    print(f'temperature: {temperature}\nhumidity: {humidity}')

    time.sleep(1)

