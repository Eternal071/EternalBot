import discord
from discord.ext import commands
import random
from random import randint
from discord import Spotify
import wikipedia
from discord.utils import get
import urllib.parse, urllib.request, re

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def spotify(self, ctx, member: discord.Member=None):
        """Shows what you are listening to"""
        member = member or ctx.message.author
        for activity in member.activities:
            if isinstance(activity, Spotify):
                em = discord.Embed(color=0x1DB954, title=f'{ctx.author} is listening to:', description=f"**{activity.title}** by **{activity.artist}**")
                await ctx.send(embed=em)
            if ctx.author == None:
                await ctx.send(embed=em)


    @commands.command()
    async def wiki(self, ctx, *, arg):
        """Searches something on wikipedia"""
        searchmsg = await ctx.send(f'Searching for {arg}...')
        em = discord.Embed(color=0x000000, description=f"{wikipedia.summary(arg, sentences=2)}")
        await ctx.send(embed=em)
        await searchmsg.delete()

    @commands.command()
    async def yt(self, ctx, *, search):
        """youtube"""
        qs = urllib.parse.urlencode({'search_query': search})
        hc = urllib.request.urlopen(
            'http://www.youtube.com/results?' + qs)
        sr = re.findall(r'/watch\?v=(.{11})',
                                    hc.read().decode())
        await ctx.send('http://www.youtube.com/watch?v=' + sr[0])

def setup(bot):
	bot.add_cog(Misc(bot))
