import random, discord
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
        responses = [
            # Atla
            "https://th.bing.com/th/id/OIP.yAlM-gWu2kSFQLNBbFdPpwAAAA?w=152&h=184&c=7&o=5&pid=1.7",
            "https://th.bing.com/th/id/OIP.Zpb9cHjA3Ci7Y3C0fUrATwHaEG?w=331&h=184&c=7&o=5&pid=1.7",
            "https://th.bing.com/th/id/OIP.Jyo1VsQrSZzqCQOUAEkyRQHaFj?w=245&h=184&c=7&o=5&pid=1.7",
            "https://th.bing.com/th/id/OIP.KV60AY9Ahwmb_mjDTq4j1AAAAA?w=218&h=176&c=7&o=5&pid=1.7",
            "https://th.bing.com/th/id/OIP.W0IH0oD4rRj930qhDCuvYAHaFs?w=211&h=180&c=7&o=5&pid=1.7",
            "https://th.bing.com/th/id/OIP.2d244s0chIKJmglW-0ndEwHaFj?w=217&h=180&c=7&o=5&pid=1.7",
            "https://th.bing.com/th/id/OIP.IlU2YiFyMV9N9XD8bJMaQAHaDt?w=334&h=175&c=7&o=5&pid=1.7",
            "https://th.bing.com/th/id/OIP.reaeKgH64bn0I4mdj4ZiQQHaEb?w=277&h=180&c=7&o=5&pid=1.7",
            "https://th.bing.com/th/id/OIP.kb98Fp86KuPiRdi_o5YZZQAAAA?w=224&h=176&c=7&o=5&pid=1.7",
            "https://th.bing.com/th/id/OIP.drC4lYXM8PxWICsxiJ_utQHaEH?w=308&h=180&c=7&o=5&pid=1.7",
            "https://th.bing.com/th/id/OIP.nlyVzBqKJYVElj5HeY5e2QAAAA?w=223&h=176&c=7&o=5&pid=1.7",
            "https://th.bing.com/th/id/OIP.RroC7EXOFkqLHS56suhLRQHaFj?w=228&h=180&c=7&o=5&pid=1.7",
            "https://th.bing.com/th/id/OIP.KQBOe7D8xUTD_37VMUiengHaDy?w=325&h=178&c=7&o=5&pid=1.7",
            "https://th.bing.com/th/id/OIP.v-OKccpOGE56Dp0wioOabAHaEK?w=321&h=180&c=7&o=5&pid=1.7",
            "https://th.bing.com/th/id/OIP.tDZG0FUEJu67GIo8DSeNBgHaHq?w=174&h=180&c=7&o=5&pid=1.7",
            "https://th.bing.com/th/id/OIP.aadmrMHt0QnJRZQAmWtAYwHaHq?w=174&h=180&c=7&o=5&pid=1.7",
            "https://th.bing.com/th/id/OIP.voTQNFHuF6cLzMT1Pv6p0QHaHq?w=151&h=180&c=7&o=5&pid=1.7",
            "https://th.bing.com/th/id/OIP.rtdu7rbeXnHfkevF5-wHhAHaEK?pid=Api&rs=1",
            "https://th.bing.com/th/id/OIP.GKX4Aei5T1qatxvY5dulSAHaEK?w=312&h=180&c=7&o=5&pid=1.7",
            "https://th.bing.com/th/id/OIP.t8OjIzJJRylX84aqjaM3EgHaEL?w=284&h=180&c=7&o=5&pid=1.7",       
            # Random
            "https://cdn.discordapp.com/attachments/746441503811043429/759833569546862602/89ff9d1.jpg",
            "https://cdn.discordapp.com/attachments/746441503811043429/759833586333122571/7pzho8scpt021.jpg",
            "https://cdn.discordapp.com/attachments/746441503811043429/759833598902796298/66237e69e275d3a1.jpg",
            "https://cdn.discordapp.com/attachments/746441503811043429/759833617445683220/0e6.jpg",
            "https://cdn.discordapp.com/attachments/746441503811043429/759833664761757786/ALVIN.png",
            "https://cdn.discordapp.com/attachments/746441503811043429/759833684164870174/5557170200_1033f7fd99_z.jpg",
            "https://cdn.discordapp.com/attachments/746441503811043429/759833730088042506/buuuuuuttttt.png",
            "https://cdn.discordapp.com/attachments/746441503811043429/759833752108138496/Apex-Legends-player-pulls-off-one-in-a-million-Octane-clutch.jpg",
            "https://cdn.discordapp.com/attachments/746441503811043429/759833781925969960/20200716_184911.jpg",
            "https://cdn.discordapp.com/attachments/746441503811043429/759833827773644800/cupdead.png",
            "https://cdn.discordapp.com/attachments/746441503811043429/759833871310127165/download_2.jpg",
            "https://cdn.discordapp.com/attachments/746441503811043429/759833900783894538/download_5.jpg",
            "https://cdn.discordapp.com/attachments/746441503811043429/759833924553408532/download_19.jpg",
            "https://cdn.discordapp.com/attachments/746441503811043429/759833981256073256/image0-54.jpg",
            "https://cdn.discordapp.com/attachments/746441503811043429/759834459054276609/image0.jpg"
        ]

        message = ""
        for x in range(int(amount)):
            message = f"{message}\n{random.choice(responses)}"

        for x in range(int(amount)):
            await ctx.send(message)    

    @commands.command(description = "yes")
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
    async def test(self, ctx):
        await ctx.send("test")

def setup(client):
    client.add_cog(Fun(client))