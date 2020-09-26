Settings = {
    "Main": {
        "CommandPrefix": "!",
        "Token": "NzU5MTQ3MzY4NDAyMTI0ODEx.X25RFA.kXNeYiy9YBI7Q8w4wfn7jS95TZg"
    }
}

import os, discord
from discord.ext import commands

client = commands.Bot(command_prefix = Settings["Main"]["CommandPrefix"])

@client.command()
@commands.has_permissions(administrator = True)
async def load(ctx, extention):
    client.load_extension(f"cogs.{extention}")
    await ctx.send(f"{extention} was loaded")

@client.command()
@commands.has_permissions(administrator = True)
async def unload(ctx, extention):
    client.unload_extension(f"cogs.{extention}")
    await ctx.send(f"{extention} was unloaded")

@client.command()
@commands.has_permissions(administrator = True)
async def reload(ctx, extention):
    client.unload_extension(f"cogs.{extention}")
    await ctx.send(f"{extention} was unloaded")

    client.load_extension(f"cogs.{extention}")
    await ctx.send(f"{extention} was loaded")

    await ctx.send(f"{extention} was fully reloaded")

for fileName in os.listdir("./cogs"):
    if fileName.endswith(".py"):
        client.load_extension(f"cogs.{fileName[:-3]}")

client.run(Settings["Main"]["Token"])