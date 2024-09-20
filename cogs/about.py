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

    @commands.Cog.listener()
    async def on_ready(self):
        print('About loaded.')

    # @commands.hybrid_group()
    # async def about(self, ctx: commands.Context[commands.Bot]) -> None:
    #     pass

    @commands.command()
    @commands.is_owner()
    async def sync(ctx: commands.Context) -> None:
        """Sync commands"""
        synced = await ctx.bot.tree.sync()
        await ctx.send(f"Synced {len(synced)} commands globally")

    @commands.hybrid_command()
    async def about(self, ctx: commands.Context[commands.Bot]):
        embed = self.embedconf.create_about_embed()
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def credits(self, ctx: commands.Context[commands.Bot]):
        with open('data/credits.json') as file:
            parsed_json = json.load(file)
        credits = parsed_json['credits']

        embed = self.embedconf.credits_embed(credits=credits[0], cur_page=0, max_len=len(credits))
        view = PaginationView(ctx.author, data=credits, pagination_type="credits")
        view.message = await ctx.send(embed=embed, view=view)

async def setup(bot: commands.Bot):
    await bot.add_cog(About(bot))

async def teardown(bot):
    print("Extension unloaded!")