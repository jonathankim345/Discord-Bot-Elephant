import discord
import os
import requests
import json
import random

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing", "afraid"]

starter_encouragements = [
  "I love you.",
  "Hang in there.",
  "You are a great person!",
  "I am here for you.",
  "I will never leave you.",
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event 
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith ('!inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  msg = message.content

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

client.run(os.getenv('TOKEN'))   