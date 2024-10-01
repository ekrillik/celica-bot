from __future__ import annotations

import json

import discord
from discord.ext import commands

from utility.build_dropdown import DropdownView
from utility.embedconfig import EmbedClass
from utility.nickname_checker import check_nickname, character_theme
from utility.fuzzymatch import fuzzmatch


class Builds(commands.Cog):
    builds = {}
    character_list = []

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

        with open('data/builds.json') as file:
            self.builds = json.load(file)
        with open('data/characterlist.json') as file:
            self.character_list = json.load(file)['characterlist']

    @commands.Cog.listener()
    async def on_ready(self):
        print('Builds loaded.')

    @commands.hybrid_command(aliases=['BuildNotation', 'Buildnotation', 'bn', 'BN'], description="Displays the build notation diagram to explain the community used build notation.")
    async def buildnotation(self, ctx: commands.Context):
        embed = discord.Embed(title="", description="")
        embed.set_image(url='https://pgr-discord-bot.s3.ap-southeast-2.amazonaws.com/cnnotationguide4.png')
        await ctx.send(embed=embed)

    @commands.hybrid_command(aliases=['AffixGuide', 'Affixguide',  'affix', 'ag'], description="Displays the affix diagram created by Ko used to explain PGR affixes.")
    async def affixguide(self, ctx: commands.Context):
        embed = discord.Embed(title="", description="")
        embed.set_image(url='https://pgr-discord-bot.s3.ap-southeast-2.amazonaws.com/Infographics/affix-guide.png')
        await ctx.send(embed=embed)

    @commands.hybrid_command(aliases=['AffixTeams', 'Affixteams', 'at'], description="Displays the affix teams infographic by Aethervoid used to explain affix teams.")
    async def affixteams(self, ctx: commands.Context):
        embed = discord.Embed(title="", description="")
        embed.set_image(url='https://pgr-discord-bot.s3.ap-southeast-2.amazonaws.com/Infographics/Affix_Teams.png')
        await ctx.send(embed=embed)

    @commands.hybrid_command(aliases=['Build', 'b'], description="Displays a set of builds for any particular character.")
    async def build(self, ctx: commands.Context, *, frame) -> None:
        name = fuzzmatch(frame)
        if name == "":
            name = frame
        character = check_nickname(name, "character")

        build = self.builds.get(character, None)
        if build is None:
            content = ('This character does not exist. Please try again.\nYou may be searching for a character with '
                       'multiple frames as well.')
            await ctx.send(content=content)
            return

        theme = character_theme(character)
        data = build['set_list']
        embed = self.embedconf.create_build_embed(build, data[0]['name'], colour=theme[0], thumbnail_url=theme[3])
        if len(data) == 1:
            view = DropdownView(ctx.author, data=data, build=build, theme=theme)
            view.message = await ctx.send(view=view, embed=embed)
        else:
            view = DropdownView(ctx.author, data=data, build=build, theme=theme, multibuild=True)
            view.message = await ctx.send(view=view, embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Builds(bot))
