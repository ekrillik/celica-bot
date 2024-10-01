from __future__ import annotations
import json
from discord.ext import commands
from utility.embedconfig import EmbedClass
from utility.pagination import PaginationView


class CharacterList(commands.Cog):
    construct_list = {}
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

        with open('data/characterlist.json') as file:
            self.construct_list = json.load(file)['formatted']

    @commands.Cog.listener()
    async def on_ready(self):
        print('CharacterList loaded.')

    @commands.hybrid_command(aliases=['CharacterList', 'Characterlist', 'charlist', 'chl'], description="Displays a comprehensive list of all existing characters and their frames.")
    async def characterlist(self, ctx: commands.Context) -> None:
        view = PaginationView(ctx.author, data=self.construct_list, pagination_type="characters")

        embed = self.embedconf.create_characterlist_embed(self.construct_list[0])
        view.message = await ctx.send(embed=embed, view=view)


async def setup(bot: commands.Bot):
    await bot.add_cog(CharacterList(bot))

