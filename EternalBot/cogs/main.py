import discord
from discord.ext import commands
import datetime
import random
from random import randint

class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, *,  avamember : discord.Member=None):
        """Gets a user's avatar."""
        avamsg = await ctx.send('Fetching Avatar...')
        await avamsg.edit(content=f'{avamember.avatar_url}')

    @commands.command()
    async def info(self, ctx, *, member: discord.Member):
        ip = f'{random.randint(100, 200)}.{random.randint(10, 50)}.{random.randint(40, 100)}.{random.randint(200, 500)}'
        embed=discord.Embed(color=0xFFFFF0, title=f"{ctx.author.name}'s Info", description="Displays user information.")
        embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
        embed.add_field(name="User ID:", value=f"{ctx.author.id}", inline=True)
        embed.add_field(name="Color:", value=f"{ctx.author.top_role.mention}\n[{ctx.author.top_role.colour}]")
        embed.add_field(name="IP Address:", value=ip, inline=False) # i also stole this from naxxbot
        embed.add_field(name="Join Date:", value=f"{ctx.author.joined_at}")
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Main(bot))
