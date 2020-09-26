# Variables

Settings = {
    "Main": {
        "CommandPrefix": "!",
        "Token": "NzU5MTQ3MzY4NDAyMTI0ODEx.X25RFA.kXNeYiy9YBI7Q8w4wfn7jS95TZg"
    }
}

import random
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = Settings["Main"]["CommandPrefix"])

# Events

## Main Events

### OnReady    
@client.event
async def on_ready():
    print("Bot is ready")
    await client.change_presence(status = discord.Status.online, activity = discord.Game("Active"))
    
#### On Error
async def on_error():
    print("Error")
    await client.change_presence(status = discord.Status.do_not_disturb, activity = discord.Game("Error"))

### On Member Join
@client.event
async def on_member_join(member):
    print(str(member) + " has joined the server")

### On Member Leave
@client.event
async def on_member_remove(member):
    print(str(member) + " has left the server")

    # Commands

## Commands

### Ping
@client.command()
async def ping(ctx):
    await ctx.send("Your ping is " + str(round(client.latency * 1000)) + "ms")

### 8ball
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

### Clear
@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount = 1):

    if amount == "all":
        amount = float("inf")

    await ctx.channel.purge(limit = amount + 1)
    
    if amount == 1:
        message = await ctx.send(str(amount) + " message will be deleted")
    else:
        message = await ctx.send(str(amount) + " messages will be deleted")   

    await message.delete(delay = 3)

### Kick
@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send(str(member) + " was kicked")

### Ban
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(str(member) + " was banned")

### Unban
@client.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, *, member):
    bannedUsers = await ctx.guild.bans()
    memberName, memberDiscriminator = member.split("#")

    for banEntry in bannedUsers:
        user = banEntry.user

        if (user.name, user.discriminator) == (memberName, memberDiscriminator):
            await ctx.guild.unban(user)
            await ctx.send(str(user) + " was unbanned")
            return

# Run

client.run(Settings["Main"]["Token"])