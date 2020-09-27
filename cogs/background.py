import discord, time
from discord.ext import tasks, commands

def convertTime(sec):
    return time.strftime('%H:%M:%S', time.gmtime(sec))

class Background(commands.Cog):
    def __init__(self, client):
        self.up_time = 0
        self.client = client
        self.printer.start()

    @tasks.loop(seconds = 5)
    async def printer(self):
        self.up_time += 5
        newtime = str(convertTime(self.up_time))
        await self.client.change_presence(status = discord.Status.online, activity = discord.Game(f".help | {newtime}"))

    @printer.before_loop
    async def before_printer(self):
        print("Bot Starting...")
        await self.client.wait_until_ready()  

def setup(client):
    client.add_cog(Background(client))