import random, discord, json
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Your ping is " + str(round(self.client.latency * 1000)) + "ms")

    @commands.command(aliases = ["8ball"])
    async def _8ball(self, ctx, *, question):
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

    @commands.command()
    async def senddudes(self, ctx, amount = 1):
        message = ""

        with open("settings.json", "r") as f:
            settings = json.load(f)
            responses = settings["server_data"][str(ctx.guild.id)]["dude_images"]

            for x in range(int(amount)):
                message = f"{message}\n{random.choice(responses)}"

        await ctx.send(message)    

    @commands.command()
    async def adddudes(self, ctx, *, link):
        with open("settings.json", "r") as f:
            settings = json.load(f)
            settings["server_data"][str(ctx.guild.id)]["dude_images"].append(link)

            with open("settings.json", "w") as f:
                json.dump(settings, f, indent = 4)

        await ctx.send(f"`{str(link)}` was added to `yt` command.")

    @commands.command()
    async def bordem(self, ctx, amount = 1):
        responses = [
            "Among Us",
            "Fall Guys",
            "Apex",
            "Smash",
            "GTA",
            "Consoles 2",
            "Xbox 1",
            "PC",
            "PS4",
            "Switch",
            "DS",
            "Gamecube",
            "Xbox360",
            "Gameboy",
            "Youtube cause why not",
            "Minecraft",
            "Crash Bandicoot",
            "Spyro",
            "Roblox",
            "outside bruh",
            "Call of Duty",
            "Halo",
            "Sonic",
            "Rayman",
            "fortnite",
            "zelda",
            "chess but in real life"
        ]

        for x in range(int(amount)):
            await ctx.send(random.choice(responses))    

    @commands.command()
    async def votemf(self, ctx, amount = 1):
        responses = [
            "https://vignette.wikia.nocookie.net/among-us-wiki/images/a/a6/1_red.png/revision/latest/scale-to-width-down/140?cb=20200912125145",
            "https://vignette.wikia.nocookie.net/among-us-wiki/images/8/8e/2_blue.png/revision/latest/scale-to-width-down/140?cb=20200912125155",
            "https://vignette.wikia.nocookie.net/among-us-wiki/images/3/34/3_green.png/revision/latest/scale-to-width-down/140?cb=20200912125201",
            "https://vignette.wikia.nocookie.net/among-us-wiki/images/9/9b/4_pink.png/revision/latest/scale-to-width-down/140?cb=20200912125206",
            "https://vignette.wikia.nocookie.net/among-us-wiki/images/f/f1/5_orange.png/revision/latest/scale-to-width-down/140?cb=20200912125212",
            "https://vignette.wikia.nocookie.net/among-us-wiki/images/5/54/6_yellow.png/revision/latest/scale-to-width-down/140?cb=20200912125217",
            "https://vignette.wikia.nocookie.net/among-us-wiki/images/5/55/7_black.png/revision/latest/scale-to-width-down/140?cb=20200912125223",
            "https://vignette.wikia.nocookie.net/among-us-wiki/images/e/e1/8_white.png/revision/latest/scale-to-width-down/140?cb=20200912125229",
            "https://vignette.wikia.nocookie.net/among-us-wiki/images/7/72/9_purple.png/revision/latest/scale-to-width-down/140?cb=20200912125234",
            "https://vignette.wikia.nocookie.net/among-us-wiki/images/b/b2/10_brown.png/revision/latest/scale-to-width-down/140?cb=20200912125240",
            "https://vignette.wikia.nocookie.net/among-us-wiki/images/f/f2/11_cyan.png/revision/latest/scale-to-width-down/140?cb=20200912125246",
            "https://vignette.wikia.nocookie.net/among-us-wiki/images/f/fd/12_lime.png/revision/latest/scale-to-width-down/140?cb=20200912125258",
            
        ]

        for x in range(int(amount)):
            await ctx.send(random.choice(responses))    

    @commands.command()
    async def yt(self, ctx, amount = 1):
        message = ""
        
        with open("settings.json", "r") as f:
            settings = json.load(f)
            responses = settings["server_data"][str(ctx.guild.id)]["yt_links"]

            for x in range(int(amount)):
                message = f"{message}\n{random.choice(responses)}"

        await ctx.send(message)    

    @commands.command()
    async def ytadd(self, ctx, *, link):
        with open("settings.json", "r") as f:
            settings = json.load(f)
            settings["server_data"][str(ctx.guild.id)]["yt_links"].append(link)

            with open("settings.json", "w") as f:
                json.dump(settings, f, indent = 4)

        await ctx.send(f"`{str(link)}` was added to `yt` command.")

def setup(client):
    client.add_cog(Fun(client))