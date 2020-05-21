import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import RPi.GPIO as GPIO
import time
import signal

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
description = 'rpi bot'
bot = commands.Bot(command_prefix='?', description=description)
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


def light_on(led):
    toggle_on(led)
    time.sleep(0.5)
    toggle_off(led)


def RCtime(RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(RCpin, GPIO.IN)
    while GPIO.input(RCpin) == GPIO.LOW:
        reading += 1
    return reading


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def hello(ctx):
    await ctx.send('world')


@bot.command()
async def light_sensor(ctx):
    read_data = RCtime(22)
    await ctx.send('The current light level sensor is at: ' + str(read_data))


@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)


@bot.command()
async def all_lights(ctx):
    for _ in range(10):
        light_on(red_led)
        light_on(blue_led)
        light_on(green_led)


@bot.command()
async def toggle(ctx):
    for _ in range(10):
        light_on(red_led)


@bot.command()
async def air(ctx):
    for _ in range(25):
        light_on(green_led)


def signal_handler(signum, frame):
    print('\nInterrupt detected!!!')
    toggle_off(red_led)
    exit(0)


signal.signal(signal.SIGINT, signal_handler)
bot.run(TOKEN)

print('Shutting down')
