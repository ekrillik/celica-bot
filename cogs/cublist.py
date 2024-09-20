from __future__ import annotations
import json
from discord.ext import commands
from utility.embedconfig import EmbedClass


class CUBList(commands.Cog):
    cubs = []

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

        with open('data/cublist.json') as file:
            self.cubs = json.load(file)['cublist_categorized']

    @commands.Cog.listener()
    async def on_ready(self):
        print('CUBList loaded.')

    @commands.hybrid_command(aliases=['cbl'])
    async def cublist(self, ctx: commands.Context) -> None:
        embed = self.embedconf.create_cublist_embed(cubs=self.cubs)
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(CUBList(bot))
