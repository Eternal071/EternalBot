import discord
from discord.ext import commands
from difflib import SequenceMatcher

class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """Yes i stole this from naxxbot"""
        if isinstance(error, commands.CommandNotFound):
            cmds = []
            for cmd in ctx.bot.commands:
                cmds.append(cmd.name)
            ratio = [0]
            suggestion=[]
            tc = str(ctx.message.content).strip(ctx.prefix).split(' ')[0].lower()
            for command in cmds:
                matcher = SequenceMatcher(None, tc, command)
                matcherNr = matcher.ratio()
                if matcherNr > 0:
                    if max(ratio) > matcherNr:
                        pass
                    if max(ratio) < matcherNr:
                        ratio.clear(); suggestion.clear(); suggestion.append(command); ratio.append(matcherNr)
            return await ctx.send(f'Command not found. Were you looking for: `{suggestion[0]}`?')

	if isinstance(error, discord.ext.commands.NotOwner):
            await ctx.send("This command is owner only.")


def setup(bot):
	bot.add_cog(Errors(bot))
