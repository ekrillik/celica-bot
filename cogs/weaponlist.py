from __future__ import annotations

import json
from discord.ext import commands
from utility.embedconfig import EmbedClass
from utility.weplist_pagination import WeaponListPaginationView

class WeaponList(commands.Cog):
    categories = []

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

        with open('data/weaponlist.json') as file:
            self.categories = json.load(file)['weaponlist_categorised']

    @commands.Cog.listener()
    async def on_ready(self):
        print('WeaponList loaded.')

    @commands.hybrid_command(aliases=['WeaponList', 'Weaponlist', 'wl'], description="Displays all lists of weapons based on a particular type.")
    async def weaponlist(self, ctx: commands.Context) -> None:
        weplistview = WeaponListPaginationView(ctx.author, data=self.categories)

        embed = self.embedconf.create_list_embed(name=self.categories[0]['name'], type="weapons", items=self.categories[0]['list'], curpage=1, maxlistcount=len(self.categories))
        weplistview.message = await ctx.send(embed=embed, view=weplistview)

async def setup(bot: commands.Bot):
    await bot.add_cog(WeaponList(bot))
