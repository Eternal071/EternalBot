import discord
from discord.ext import commands
from discord.ext import tasks

prefixes = ['e!', 'e?', 'e.']

activity = discord.Game(name="cmd")

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=prefixes, activity=activity, status=discord.Status.do_not_disturb, intents=intents)

initial_extensions = ['cogs.fun', 'cogs.main', 'cogs.owner', 'cogs.misc', 'cogs.errors']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print('Online')

@bot.command()
@commands.is_owner()
async def reload(ctx):
    """Reload all cogs. (Owner)"""
    reloading = await ctx.send("Reloading...")
    bot.unload_extension("cogs.main")
    bot.load_extension("cogs.main")
    bot.unload_extension("cogs.fun")
    bot.load_extension("cogs.fun")
    bot.unload_extension("cogs.owner")
    bot.load_extension("cogs.owner")
    bot.unload_extension("cogs.misc")
    bot.load_extension("cogs.misc")
    bot.unload_extension("cogs.errors")
    bot.load_extension("cogs.errors")
    await reloading.edit(content='Reloaded.')

bot.run("TOKEN")
