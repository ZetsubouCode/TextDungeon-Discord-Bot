import discord
from function.StartGame import StartGame as StartGameFunction
from _env import ENV

client = discord.Client()

@client.event
async def on_ready():
    print("we have logged in successfully as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!hello') and message.channel.name == 'bot-test':
        print(message.channel)
        await message.channel.send('Hello!')

    if message.content.startswith('!start'):
        await StartGameFunction.start_game(client, message)

client.run(ENV.TOKEN)