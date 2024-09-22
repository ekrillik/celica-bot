import discord
from discord.ext import commands


class Test(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('TestCog loaded.')

    @commands.hybrid_command(description="Test command to check if bot is alive.")
    async def test(self, ctx: commands.Context):
        message = "I'm alive"
        title = "Test Message"
        embed = discord.Embed(title=title, description=message)
        await ctx.send(embed=embed)

    @commands.hybrid_command(description="Displays latency between the bot server and the Discord server.")
    async def ping(self, ctx: commands.Context):
        message = f'⏱|** {round(self.bot.latency * 1000)} ms** Latency!'
        title = "Ping"
        embed = discord.Embed(title=title, description=message)
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Test(bot))
