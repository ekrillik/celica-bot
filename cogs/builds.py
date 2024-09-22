from __future__ import annotations

import json

import discord
from discord.ext import commands

from utility.build_dropdown import DropdownView
from utility.embedconfig import EmbedClass
from utility.nickname_checker import check_nickname, character_theme


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

    @commands.hybrid_command(description="Displays the build notation diagram to explain the community used build notation.")
    async def buildnotation(self, ctx: commands.Context):
        embed = discord.Embed(title="", description="")
        embed.set_image(url='https://pgr-discord-bot.s3.ap-southeast-2.amazonaws.com/cnnotationguide4.png')
        await ctx.send(embed=embed)

    @commands.hybrid_command(aliases=["affix"], description="Displays the affix diagram created by Ko used to explain PGR affixes.")
    async def affixguide(self, ctx: commands.Context):
        embed = discord.Embed(title="", description="")
        embed.set_image(url='https://pgr-discord-bot.s3.ap-southeast-2.amazonaws.com/Affix+Infographic.jpg')
        await ctx.send(embed=embed)

    @commands.hybrid_command(description="Displays a set of builds for any particular character.")
    async def build(self, ctx: commands.Context, *, character) -> None:
        character = check_nickname(character, "character")

        build = self.builds.get(character, None)
        if build is None:
            content = ('This character does not exist. Please try again.\nYou may be searching for a character with '
                       'multiple frames as well. The bot is currently not able to return builds for multiple frames '
                       'based on a character search. Please use the specific frame name of the character instead.\n'
                       '(For example, search "?build oblivion" or "?build laurel" instead of "?build Luna/luna")')
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
