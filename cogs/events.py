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
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)
        
        prefixes[str(guild.id)] = "."

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent = 4)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)
        
        prefixes.pop(str(guild.id))

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent = 4)

    @commands.Cog.listener()
    async def on_guild_available(self, guild):

        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

            if not str(guild.id) in prefixes:
                print(f"{guild} does NOT have a prefix, adding default now...")
                
                prefixes[str(guild.id)] = "."
                with open("prefixes.json", "w") as f:
                    json.dump(prefixes, f, indent = 4)

def setup(client):
    client.add_cog(Events(client))