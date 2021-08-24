import discord
import os
import requests
import json
import random
import asyncio
from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix = "-")

@client.command()
async def delete(msg, amount = 0):
  channel = msg.channel
  all_roles = msg.author.roles
  print(all_roles)
  
  if amount <= 15:
    for role in all_roles:
      if role.name == "Owner" and amount == 0:
        await msg.send("Please confirm if you would like to delete all messages in this channel by typing yes. Otherwise wait for 10 seconds till cooldown.")

        def check(m):
          return m.content == 'yes' and m.channel == channel
        msg_ = await client.wait_for('message', check=check, timeout= 10)

        a = 5
        while a >= 0:
          await channel.send(f"Deleting in {a}")
          await asyncio.sleep(1)
          a -= 1
        await msg.channel.purge()
        await channel.send("Successfully deleted")

        break
    for role1 in all_roles:
      if role1.name == "Goat":
        print("Hello")
        if amount == 0 and role.name != "Owner":
          await msg.send("Please enter a value")
        
        elif amount != 0 and role.name != "Owner":
          await msg.channel.purge(limit = amount + 1)
  else:
    await channel.send("Please enter a value less than 15")


keep_alive()

client.run(os.getenv('TOKEN'))
