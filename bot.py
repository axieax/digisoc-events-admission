import os
from dotenv import load_dotenv
import discord
from discord.utils import get
from app import start_server

load_dotenv()
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} online')


@client.event
async def on_message(message):
    # respond to messages from the #waiting-room channel
    if message.channel.name == 'waiting-room':
        server = message.guild
        # extract user from discord tag
        tag = message.embeds[0].fields[2].value.split('#')
        user = get(server.members, name=tag[0], discriminator=tag[1])

        # admit user
        admitted_role = get(server.roles, name='Admitted')
        await user.add_roles(admitted_role)

        # react to message
        await message.add_reaction('✅')


if __name__ == '__main__':
    start_server()
    client.run(os.getenv('TOKEN'))
