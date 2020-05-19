import RPi.GPIO as GPIO
import time
import signal

red_led = 18
blue_led = 23
green_led = 25

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(blue_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)


def toggle_on(led_id):
    GPIO.output(led_id, GPIO.HIGH)
    print(f'led {led_id}: on')


def toggle_off(led_id):
    GPIO.output(led_id, GPIO.LOW)
    print(f'led {led_id}: off')


def signal_handler(signum, frame):
    print('\nInterrupt detected!!!')
    toggle_off(red_led)
    toggle_off(blue_led)
    toggle_off(green_led)
    exit(0)


def light_on(led):
    toggle_on(led)
    time.sleep(1)
    toggle_off(led)


def all_lights(how_many):
    while how_many >= 0:
        how_many = how_many - 1
        light_on(red_led)
        light_on(blue_led)
        light_on(green_led)


signal.signal(signal.SIGINT, signal_handler)

while True:
    user_input = input('Press "q" to quit: ')
    if 'q' in user_input:
        break
    if user_input == 'r':
        light_on(red_led)
    if user_input == 'g':
        light_on(green_led)
    if user_input == 'b':
        light_on(blue_led)
    if user_input == 'a':
        sec_input = int(input('How many cycles?: '))
        all_lights(sec_input)

print('Shutting down')
