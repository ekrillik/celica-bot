from __future__ import annotations

import typing
import traceback
import discord
import os
import json
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from utility.embedconfig import EmbedClass
from utility.pagination import PaginationView

from discord.ui.select import BaseSelect

class CharacterList(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

    def retrieve_characterlist(self):
        with open('data/characterlist.json') as file:
            parsed_json = json.load(file)
        return parsed_json['formatted']

    @commands.Cog.listener()
    async def on_ready(self):
        print('CharacterList loaded.')

    @commands.command(aliases=['chl'])
    async def characterlist(self, ctx: commands.Context) -> None:
        constructs = self.retrieve_characterlist()
        self.view = PaginationView(ctx.author, data=constructs, pagination_type="characters")

        embed = self.embedconf.create_characterlist_embed(constructs[0])
        self.view.message = await ctx.send(embed=embed, view=self.view)

async def setup(bot: commands.Bot):
    await bot.add_cog(CharacterList(bot))

async def teardown(bot):
    print("Extension unloaded!")