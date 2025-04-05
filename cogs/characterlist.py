from __future__ import annotations
import json
import discord
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

    @commands.hybrid_command(description="Displays the current priority list for SS3 rank upgrades")
    async def ss3priority(self, ctx: commands.Context) -> None:

        ss3prioritylist = ["1. Lucia: Pyroath", "2. Selena: Pianissimo", "Ishmael: Parhelion", "Nanami: Startrail", "Hanying: Solacetune", "Vera: Geivaror"]

        names = "\n".join(f"{character}" for character in ss3prioritylist)

        embed =  discord.Embed(
            title=f"SS3 Priority List of gacha-only units",
            description=names
        )
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(CharacterList(bot))

