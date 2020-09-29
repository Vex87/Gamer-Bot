import discord, time
from datetime import datetime
from discord.ext import tasks, commands

def convertTime(sec):
    return time.strftime('%H:%M:%S', time.gmtime(sec))

class Background(commands.Cog):
    def __init__(self, client):
        self.start_time = str(datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
        self.up_time = 0
        self.formatted_up_time = str(convertTime(self.up_time))
        self.client = client
        self.printer.start()

    @tasks.loop(seconds = 5)
    async def printer(self):
        self.up_time += 5
        self.formatted_up_time = str(convertTime(self.up_time))
        await self.client.change_presence(status = discord.Status.online, activity = discord.Game(f".help | {self.formatted_up_time}"))

    @printer.before_loop
    async def before_printer(self):
        print("Bot Starting...")
        await self.client.wait_until_ready()  

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(
            title = "Bot Info",
            colour = discord.Colour.green()
        )
        embed.add_field(name = "Start Time", value = self.start_time, inline = False)
        embed.add_field(name = "Uptime", value = str(self.formatted_up_time), inline = False)
        embed.add_field(name = "Connected Servers", value = str(len(self.client.guilds)), inline = False)
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Background(client))