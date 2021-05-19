import discord
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mimic(self, ctx, member: discord.Member, *, message=None):

        webhook = await ctx.channel.create_webhook(name=member.name)
        await webhook.send(
            str(message), username=member.name, avatar_url=member.avatar_url)

        webhooks = await ctx.channel.webhooks()
        for webhook in webhooks:
                await webhook.delete()

    

def setup(bot):
	bot.add_cog(Fun(bot))
