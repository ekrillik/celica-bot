import discord
from discord.ext import commands


class TestCog(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('TestCog loaded.')

    @commands.command()
    async def test(self, ctx):
        message = "I'm alive"
        title = "Test Message"
        embed = discord.Embed(title=title, description=message)
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        message = f'⏱|** {round(self.bot.latency * 1000)} ms** Latency!'
        title = "Ping"
        embed = discord.Embed(title=title, description=message)
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(TestCog(bot))
