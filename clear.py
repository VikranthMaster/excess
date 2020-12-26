import discord
from discord.ext import commands

def read_token():
    with open("token.txt","r") as f:
        lines = f.readlines()
        return lines[0].strip()

client = commands.Bot(command_prefix="/")

@client.event
async def on_ready():
    print ("bot is ready!")

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

client.run(read_token())