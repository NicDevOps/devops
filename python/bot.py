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

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(red_led, GPIO.OUT)


def toggle_on(led_id):
  GPIO.output(led_id, GPIO.HIGH)
  print(f'led {led_id}: on')


def toggle_off(led_id):
  GPIO.output(led_id, GPIO.LOW)
  print(f'led {led_id}: off')


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
async def add(ctx, left : int, right : int):
    await ctx.send(left + right)


@bot.command()
async def toggle(ctx):
    for _ in range(10):
        toggle_on(red_led)
        time.sleep(0.5)
        toggle_off(red_led)
        time.sleep(0.5)


def signal_handler(signum, frame):
  print('\nInterrupt detected!!!')
  toggle_off(red_led)
  exit(0)


signal.signal(signal.SIGINT, signal_handler)
bot.run(TOKEN)

print('Shutting down')

