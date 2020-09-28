import discord, math
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount = 1):
        deleted_msgs = await ctx.channel.purge(limit = amount + 1)
        num_of_msgs = len(deleted_msgs) - 1
        message = await ctx.send(content = str(num_of_msgs) + " messages were deleted", delete_after = 2)

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member, *, reason = None):
        await member.kick(reason = reason)
        await ctx.send(str(member) + " was kicked")

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member, *, reason = None):
        await member.ban(reason = reason)
        await ctx.send(str(member) + " was banned")

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member):
        bannedUsers = await ctx.guild.bans()
        memberName, memberDiscriminator = member.split("#")

        for banEntry in bannedUsers:
            user = banEntry.user

            if (user.name, user.discriminator) == (memberName, memberDiscriminator):
                await ctx.guild.unban(user)
                await ctx.send(str(user) + " was unbanned")
                return

def setup(client):
    client.add_cog(Moderation(client))