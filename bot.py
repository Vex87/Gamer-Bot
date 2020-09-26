# -- // Variables \\ --

Settings = {
    "Main": {
        "CommandPrefix": "!",
        "Token": "NzU5MTQ3MzY4NDAyMTI0ODEx.X25RFA.kXNeYiy9YBI7Q8w4wfn7jS95TZg"
    }
}

import random
import discord
from discord.ext import commands

# -- // Variables \\ --

client = commands.Bot(command_prefix = Settings["Main"]["CommandPrefix"])

# -- // Events \\ --

    # Main Events

@client.event
async def on_ready():
    print("Bot is ready")
    
@client.event
async def on_member_join(member):
    print(str(member) + " has joined the server")

@client.event
async def on_member_remove(member):
    print(str(member) + " has left the server")

    # Commands

@client.command()
async def ping(ctx):
    await ctx.send("Your ping is " + str(round(client.latency * 1000)) + "ms")

@client.command(aliases = ["8ball"])
async def _8ball(ctx, *, question):
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    await ctx.send("**Question:** " + question + "\n**Answer:** " + random.choice(responses))

@client.command()
async def clear(ctx, amount = 1):

    if amount == "all":
        amount = float("inf")

    await ctx.channel.purge(limit = amount + 1)
    
    if amount == 1:
        message = await ctx.send(str(amount) + " message will be deleted")
    else:
        message = await ctx.send(str(amount) + " messages will be deleted")   

    await message.delete(delay = 3)

# -- // Run \\ --

client.run(Settings["Main"]["Token"])