import discord
from function.StartGame import StartGame as StartGameFunction
from function.Command import Command as CommandFunction
from _env import ENV

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
  print("we have logged in successfully as {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user or message.channel.name != 'bot-test':
    return

  if message.content.startswith('!Command'):
    await message.channel.send(CommandFunction.command_list())

  if message.content.startswith('!menu'):
    await message.channel.send(CommandFunction.main_menu())

  if message.content.startswith('!start'):
    await StartGameFunction.start_game(client, message)


client.run(ENV.TOKEN)
