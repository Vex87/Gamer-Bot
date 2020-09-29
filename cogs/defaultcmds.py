import discord, json
from discord.ext import commands

class DefaultCmds(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        
        # Default
        default_embed = discord.Embed(
            title = "Default Commands",
            colour = discord.Colour.light_gray()
        )
        default_embed.add_field(name = "help", value = "Returns a list of commands. (defaultcmds)", inline = False)
        default_embed.add_field(name = "load [COG]", value = "Loads a cog. (none)", inline = False)
        default_embed.add_field(name = "unload [COG]", value = "Unloads a cog. (none)", inline = False)
        default_embed.add_field(name = "reload [COG]", value = "Unloads and loads a cog. (none)", inline = False)
        default_embed.add_field(name = "checkforupdates", value = "Unloads and loads all cogs.  (none)", inline = False)
        default_embed.add_field(name = "ping", value = "Returns the user's ping. (fun)", inline = False)
        default_embed.add_field(name = "info", value = "Returns the bot start time, bot up time, connected servers, and latency. (background)", inline = False)
        await ctx.send(embed = default_embed)

        # Fun
        fun_embed = discord.Embed(
            title = "Fun Commands",
            colour = discord.Colour.blue()
        )
        fun_embed.add_field(name = "8ball [QUESTION]", value = "Returns a random answer to the question. (fun)", inline = False)
        fun_embed.add_field(name = "senddudes [AMOUNT = 1]", value = "Returns [AMOUNT] images of dudes. (fun)", inline = False)
        fun_embed.add_field(name = "adddudes [LINK]", value = "Adds a new photo link to the `senddudes` cmd (fun)", inline = False)
        fun_embed.add_field(name = "yt [AMOUNT]", value = "Returns a random youtube video. (fun)", inline = False)
        fun_embed.add_field(name = "ytadd", value = "Adds a new link to the `ty` cmd (fun)", inline = False)
        fun_embed.add_field(name = "bordem [AMOUNT = 1]", value = "Returns [AMOUNT] random videogames. (fun)", inline = False)
        fun_embed.add_field(name = "votemf [AMOUNT = 1]", value = "Returns a random Among Us player. (fun)", inline = False)
        await ctx.send(embed = fun_embed)

        # Moderation
        moderation_embed = discord.Embed(
            title = "Moderation Commands",
            colour = discord.Colour.red()
        )
        moderation_embed.add_field(name = "clear [AMOUNT = 1]", value = "Clears [AMOUNT] messages in the executed channel. (moderation)", inline = False)
        moderation_embed.add_field(name = "kick [USER] [REASON = NONE]", value = "Kicks the user from the server with an optional reason. User executing command must have kick permissions (moderation)", inline = False)
        moderation_embed.add_field(name = "ban [USER] [REASON = NONE]", value = "Bans a user from that server with an optional reason. User executing the command must have ban permissions. (moderation)", inline = False)
        moderation_embed.add_field(name = "unban [USER]", value = "Unbans a user from the server. User executing the command must have ban permissions. (moderation)", inline = False)
        moderation_embed.add_field(name = "changeprefix [NEW_PREFIX = .]", value = "Changes the bot's prefix. user executing the command must have administrator permissions. (defaultcmds)", inline = False)
        await ctx.send(embed = moderation_embed)
            
    @commands.command()
    @commands.check_any(commands.is_owner())
    @commands.check_any(commands.is_owner(), commands.has_permissions(administrator = True))
    async def changeprefix(self, ctx, prefix = "."):
        with open("settings.json", "r") as f:
            settings = json.load(f)
            settings["server_data"][str(ctx.guild.id)]["prefix"] = prefix

            with open("settings.json", "w") as f:
                json.dump(settings, f, indent = 4)

        await ctx.send(f"Prefix changed to `{prefix}``")

def setup(client):
    client.add_cog(DefaultCmds(client))