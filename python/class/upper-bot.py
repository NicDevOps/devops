import os
import discord

upper_bot_token = os.environ.get('UPPER_BOT_TOKEN', 'missing token')


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        await message.channel.send(message.content.upper())

        # if message.content == 'ping':
        #     await message.channel.send('pong')


client = MyClient()
client.run(upper_bot_token)