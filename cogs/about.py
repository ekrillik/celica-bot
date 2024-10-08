import json
from discord.ext import commands
from utility.embedconfig import EmbedClass
from utility.pagination import PaginationView


class About(commands.Cog):
    credits = {}

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

        with open('data/credits.json') as file:
            self.credits = json.load(file)['credits']

    @commands.Cog.listener()
    async def on_ready(self):
        print('About loaded.')

    @commands.hybrid_command(description="Displays basic information about Celica.")
    async def about(self, ctx: commands.Context[commands.Bot]):
        embed = self.embedconf.create_about_embed()
        await ctx.send(embed=embed)

    @commands.hybrid_command(description="Displays the names of people who contributed to Celica's development.")
    async def credits(self, ctx: commands.Context[commands.Bot]):
        embed = self.embedconf.credits_embed(credits=self.credits[0], cur_page=0, max_len=len(self.credits))
        view = PaginationView(ctx.author, data=self.credits, pagination_type="credits")
        view.message = await ctx.send(embed=embed, view=view)


async def setup(bot: commands.Bot):
    await bot.add_cog(About(bot))
