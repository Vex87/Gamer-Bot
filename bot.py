Settings = {
    "Main": {
        "CommandPrefix": ".",
        "Token": "NzU5MTQ3MzY4NDAyMTI0ODEx.X25RFA.kXNeYiy9YBI7Q8w4wfn7jS95TZg"
    }
}

import os, discord
from discord.ext import commands

client = commands.Bot(command_prefix = Settings["Main"]["CommandPrefix"])
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

client.run(Settings["Main"]["Token"])