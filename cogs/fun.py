import discord
import os
import json
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from utility.embedconfig import EmbedClass
from utility.pagination import PaginationView

class About(commands.Cog): 

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()
        self.disallowed_server_ids = [1285561465537040384, 595893569609269251, 361043659107467264]

    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun loaded.')

    @commands.command()
    async def fun(self, ctx: commands.Context) -> None:
        if ctx.guild.id not in self.disallowed_server_ids:
            embed = discord.Embed(title="This is a fun command.", description="This is a fun command description")
            await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(About(bot))

async def teardown(bot):
    print("Extension unloaded!")