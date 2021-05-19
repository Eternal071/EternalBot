import discord
from discord.ext import commands
import ast

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def exec(self, ctx, *, arg):
        """runs code (owner)"""
        exv = arg.replace("```", "")
        if arg.startswith("await"):
            await eval(arg.replace("await ", ""))
        else:
            exec(exv)

def setup(bot):
	bot.add_cog(Owner(bot))
