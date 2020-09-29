import discord, json
from discord.ext import commands

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot Is Ready")   
        await self.client.change_presence(status = discord.Status.online, activity = discord.Game("Active"))
    
    @commands.Cog.listener()
    async def on_error(self):
        print("Error")
        await self.client.change_presence(status = discord.Status.do_not_disturb, activity = discord.Game("Error"))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(str(member) + " has joined the server")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(str(member) + " has left the server")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(f"**ERROR:** {str(error)}")

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print(f"Bot added to {guild.name}")
        with open("settings.json", "r") as f:
            settings = json.load(f)

            if not str(guild.id) in settings["server_data"]:
                print(f"{guild} does not have data, adding default data now...")
                settings["server_data"][str(guild.id)] = settings["default_data"].copy()

                with open("settings.json", "w") as f:
                    json.dump(settings, f, indent = 4)
                    print(f"Default data added to {guild.name}")

    @commands.Cog.listener()
    async def on_guild_available(self, guild):
        print(f"{guild.name}'s bot started")
        with open("settings.json", "r") as f:
            settings = json.load(f)

            if not str(guild.id) in settings["server_data"]:
                print(f"{guild} does not have data, adding default data now...")
                settings["server_data"][str(guild.id)] = settings["default_data"].copy()

                with open("settings.json", "w") as f:
                    json.dump(settings, f, indent = 4)
                    print(f"Default data added to {guild.name}")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        print(f"Bot removed from {guild.name}, removing data now...")

        with open("settings.json", "r") as f:
            settings = json.load(f)
            del settings["server_data"][str(guild.id)]

            with open("settings.json", "w") as f:
                json.dump(settings, f, indent = 4)
                print(f"Data removed from {guild.name}")

def setup(client):
    client.add_cog(Events(client))