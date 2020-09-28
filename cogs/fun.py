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

        await ctx.send(message)    

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
        responses = [
            "https://youtu.be/JNecYo0e3f4",
            "https://youtu.be/4Be5U18-F9A",
            "https://youtu.be/8apD9WWDy4s",
            "https://youtu.be/v8wQnnoq3lc",
            "https://youtu.be/PPG_uKS72kE",
            "https://youtu.be/tm-guFu9HLM"
            "https://youtu.be/FAvjx8bmJOQ",
            "https://youtu.be/z89nNyVKHcc",
            "https://youtu.be/Mi2cJ8kNeQ4",
            "https://youtu.be/uRew3iHAQp0",
            "https://youtu.be/l3eo5okFcvY",
            "https://youtu.be/j4EvDMlFOS8",
            "https://youtu.be/2YrHqH2Jqhw",
            "https://youtu.be/j4EvDMlFOS8",
            "https://youtu.be/l3eo5okFcvY",
            "https://youtu.be/c98T1ra_RdE",
            "https://youtu.be/_N_Uqd7JBcM",
            "https://youtu.be/fC7oUOUEEi4",
            "https://youtu.be/dQw4w9WgXcQ",
            "https://youtu.be/3TrR6eMvwEU",
            "https://youtu.be/KDo9dFcucI4",
            "https://youtu.be/C8ZiivGHJy0",
            "https://youtu.be/M0_BNwXUhTA",
            "https://youtu.be/pSgZTLrQJYk",
            "https://youtu.be/-_w0yhl-jig",
            "https://youtu.be/_lLmodkv8R4",
            "https://youtu.be/Myhi96jKEoM",
            "https://youtu.be/g-njtZmmUw4",
            "https://youtu.be/yDbF34oy_FY",
            "https://youtu.be/Pm_ZYTWA7BI",
            "https://youtu.be/IdgQDZtDlJA",
            "https://youtu.be/I707ZUPZmdo",
            "https://youtu.be/3ikD7VaVZ-w",
            "https://youtu.be/PHnPNoxdsMA",
            "https://youtu.be/qfaddk0GXF4",
            "https://youtu.be/XCrFDR6UIc8",
            "https://youtu.be/8KAwAR7iFGI",
            "https://youtu.be/64V_KO3ikN0",
            "https://youtu.be/59-ikOobzSw",
            "https://youtu.be/PYLgBYjXAxI",
            "https://youtu.be/zviVWnuKGkE",
            "https://youtu.be/S9XsKGkOmQ4",
            "https://youtu.be/80LEPMs7t6g"
            "https://youtu.be/CS6tETxcm9k",
            "https://youtu.be/rsOuWXHWSXY",
            "https://youtu.be/optyFJlowTo",
            "https://youtu.be/bnvgXVt3EoQ",
            "https://youtu.be/sj7DUuIiWF0",
            "https://youtu.be/PobpXY4nNzY",
            "https://youtu.be/9Jp3MDavWBo",
            "https://youtu.be/n8kGjrfoxao",
            "https://youtu.be/VpCIS5LZ2K8",
            "https://youtu.be/NxlVERr14DE",
            "https://youtu.be/qhtU4csm84s",
            "https://youtu.be/qhtU4csm84s",
            "https://youtu.be/5qeYmuEfCvA",
            "https://youtu.be/q3paDVkprIg",
            "https://youtu.be/BwA58AUGSsw",
            "https://youtu.be/4bJPuAnlDaM",
            "https://youtu.be/-95c2AD-8JA",
            "https://youtu.be/4Km7yeXDe4s",
            "https://youtu.be/ZrP91rShA7I",
            "https://youtu.be/-evzF_9sjPg",
            "https://youtu.be/RMuAwTInBhc",
            "https://youtu.be/tHN4-QWxJpk",
            "https://youtu.be/5Gvj4ks5694",
            "https://youtu.be/AdtyvFvdzi8",
            "https://youtu.be/kUk4RIv97MQ",
            "https://youtu.be/-wdWh7ci6rM",
            "https://youtu.be/7Uxq-lxhx_M",
            "https://youtu.be/T91Qx1gdqgQ",
            "https://youtu.be/RINHjxsPOEg",
            "https://youtu.be/7OZmRQkg9G0",
            "https://youtu.be/JP_sdUWnMAQ",
            "https://youtu.be/N4xcmw9hcx0",
            "https://youtu.be/N4xcmw9hcx0",
            "https://youtu.be/ZSYxlISANCg",
            "https://youtu.be/lu1xofwlTU4",
            "https://youtu.be/NvIGAuMVeoM",
            "https://youtu.be/xEzc09cKKzU",
            "https://youtu.be/Ph39ujCAHDY",
            "https://youtu.be/Yua1VY_IqRM",
            "https://youtu.be/q84t9ORBf40",
            "https://youtu.be/yi8WrSCDfTY",
            "https://youtu.be/oLMkUKAiVDY",
            "https://youtu.be/GaC1JXMidW0",
            "https://youtu.be/MMY_SUuobww",
            "https://youtu.be/m10MUR4Ig40",
            "https://youtu.be/RoNGYohIOag",
            "https://youtu.be/TVl9qR89bYk",
            "https://youtu.be/Wge2epiREOQ",
            "https://youtu.be/k9ep-HULpR0",
            "https://youtu.be/jh5F-q2Lwow",
            "https://youtu.be/yiXasq-gJDs",
            "https://youtu.be/wtx0fdzRAp8",
            "https://youtu.be/3fZXMb-3dFc",
            "https://youtu.be/ttIJfII5SFc",
            "https://youtu.be/t8laQv41EV0?list=TLPQMjYwNzIwMjD9u5SiHoWXSQ",
            "https://youtu.be/iMdLSpm-o8I?list=TLPQMjYwNzIwMjD9u5SiHoWXSQ",
            "https://youtu.be/Pj3omYTynac?list=TLPQMjYwNzIwMjD9u5SiHoWXSQ",
            "https://youtu.be/aJ0U4kDLAqA",
            "https://youtu.be/ttaJXjf2NxI",
            "https://youtu.be/s7sCJ75ZXrw",
            "https://youtu.be/ODLVY5B_2NE",
            "https://youtu.be/IpPAW1qX73E",
            "https://youtu.be/MogG83lV9Qw",
            "https://youtu.be/g9uwXzPylmg",
            "https://youtu.be/kmb3jZwT49o",
            "https://youtu.be/Vw_NxbSbxf8",
            "https://youtu.be/Q33r041ZHc0",
            "https://youtu.be/C86dMMJBvTs"
        ]

        for x in range(int(amount)):
            await ctx.send(random.choice(responses))   

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