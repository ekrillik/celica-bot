from __future__ import annotations

import json
from discord.ext import commands
from utility.embedconfig import EmbedClass
from utility.pagination import PaginationView


class MemoryList(commands.Cog):
    memory_list = {}

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

        with open('data/memorylist.json') as file:
            parsed_json = json.load(file)
            self.memory_list = parsed_json['memories_categorised']

    @commands.Cog.listener()
    async def on_ready(self):
        print('MemoryList loaded.')

    @commands.command(aliases=['ml'])
    async def memorylist(self, ctx: commands.Context) -> None:
        view = PaginationView(ctx.author, data=self.memory_list, pagination_type="memories")
        embed = self.embedconf.create_list_embed(name="Memories", type="memories", items=self.memory_list[0])
        view.message = await ctx.send(embed=embed, view=view)


async def setup(bot: commands.Bot):
    await bot.add_cog(MemoryList(bot))
