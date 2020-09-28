import os, discord, json
from discord.ext import commands

def get_prefix(client, msg):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(msg.guild.id)]

token = "NzU5MTQ3MzY4NDAyMTI0ODEx.X25RFA.kXNeYiy9YBI7Q8w4wfn7jS95TZg"
client = commands.Bot(command_prefix = get_prefix)
client.remove_command("help")

@client.command()
async def load(ctx, extention):
    client.load_extension(f"cogs.{extention}")
    await ctx.send(f"{extention} was loaded")

@client.command()
async def unload(ctx, extention):
    client.unload_extension(f"cogs.{extention}")
    await ctx.send(f"{extention} was unloaded")

@client.command()
async def reload(ctx, extention):
    client.reload_extension(f"cogs.{extention}")
    await ctx.send(f"{extention} was reloaded")

@client.command()
async def checkforupdates(ctx):

    for fileName in os.listdir("./cogs"):
        if fileName.endswith(".py"):
            client.reload_extension(f"cogs.{fileName[:-3]}")

    await ctx.send("Bot Up To Date")

for fileName in os.listdir("./cogs"):
    if fileName.endswith(".py"):
        client.load_extension(f"cogs.{fileName[:-3]}")

client.run(token)