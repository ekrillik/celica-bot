from __future__ import annotations

import json

from discord.ext import commands

from utility.embedconfig import EmbedClass
from utility.general_view import GeneralView
from utility.nickname_checker import check_nickname, character_theme
from utility.pagination import PaginationView
from utility.skills_menu import SkillsView


class Skills(commands.Cog):
    skills = {}

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

        with open('data/skills.json') as file:
            self.skills = json.load(file)

    async def grab_skill(self, ctx, character, skill_type):
        skillset = self.skills.get(character)
        if skillset is None:
            content = "This character does not exist. Please try again."
            await ctx.send(content=content)
            return

        match skill_type:
            case 'basic':
                skill = skillset['basic_attack']
                skill_type = 'Basic Attack'
            case 'red':
                skill = skillset['red_orb']
                skill_type = 'Red Orb'
            case 'yellow':
                skill = skillset['yellow_orb']
                skill_type = 'Yellow Orb'
            case 'blue':
                skill = skillset['blue_orb']
                skill_type = 'Blue Orb'
            case 'core':
                skill = skillset['core_passive']
                skill_type = 'Core Passive'
            case 'signature':
                skill = skillset['signature']
                skill_type = 'Signature/Ultimate'
            case 'qte':
                skill = skillset['qte']
                skill_type = 'QTE'
            case 'leader':
                skill = skillset['leader']
                skill_type = 'Leader Passive'
            case 'class':
                skill = skillset['class']
                skill_type = 'Class Passive'
            case 'ss':
                skill = skillset['ss_rank']
                skill_type = 'SS'
            case 'sss':
                skill = skillset['sss_rank']
                skill_type = 'SSS'
            case 's+':
                skill = skillset['s+_rank']
                skill_type = 'S+'
            case 'leap':
                if 'leap' not in skillset:
                    await ctx.send("This character does not have Leap skills.")
                    return
                skill = skillset['leap']
                skill_type = 'Leap'
            case _:
                await ctx.send("This skill type does not exist.")
                return

        theme = character_theme(character)

        if len(skill) > 1 and skill_type in ['Leap', 'Core Passive', 'Basic Attack', 'Red Orb', 'Yellow Orb', 'Blue Orb', 'Signature/Ultimate']:
            view = PaginationView(ctx.author, data=skill, pagination_type="skills", skill_type=skill_type, theme=theme)
        else:
            view = GeneralView(ctx.author)

        embed = self.embedconf.skillsEmbed(skill, skill_type, colour=theme[0], chibi_avatar=theme[1], user=theme[2], thumbnail=theme[3])
        view.message = await ctx.send(embed=embed, view=view)

    @commands.Cog.listener()
    async def on_ready(self):
        print('Skills loaded.')

    @commands.hybrid_command(aliases=["skills"])
    async def skill(self, ctx: commands.Context, *, character) -> None:
        character = check_nickname(character, "character")

        theme = character_theme(character)

        skills = self.retrieve_skills(character)
        embed = self.embedconf.skillsEmbed(skills['basic_attack'], "Basic Attack", colour=theme[0], chibi_avatar=theme[1], user=theme[2], thumbnail=theme[3])
        view = SkillsView(ctx.author, skills=skills, theme=theme)
        view.message = await ctx.send(embed=embed, view=view)

    @commands.hybrid_command()
    async def basic(self, ctx: commands.Context, *, character) -> None:
        character = check_nickname(character, "character")
        await self.grab_skill(ctx, character, 'basic')

    @commands.hybrid_command()
    async def red(self, ctx: commands.Context, *, character) -> None:
        character = check_nickname(character, "character")
        await self.grab_skill(ctx, character, 'red')

    @commands.hybrid_command()
    async def yellow(self, ctx: commands.Context, *, character) -> None:
        character = check_nickname(character, "character")
        await self.grab_skill(ctx, character, 'yellow')

    @commands.hybrid_command()
    async def blue(self, ctx: commands.Context, *, character) -> None:
        character = check_nickname(character, "character")
        await self.grab_skill(ctx, character, 'blue')

    @commands.hybrid_command()
    async def core(self, ctx: commands.Context, *, character) -> None:
        character = check_nickname(character, "character")
        await self.grab_skill(ctx, character, 'core')

    @commands.hybrid_command(aliases=['ult', 'ultimate'])
    async def signature(self, ctx: commands.Context, *, character) -> None:
        character = check_nickname(character, "character")
        await self.grab_skill(ctx, character, 'signature')

    @commands.hybrid_command()
    async def qte(self, ctx: commands.Context, *, character) -> None:
        character = check_nickname(character, "character")
        await self.grab_skill(ctx, character, 'qte')

    @commands.hybrid_command()
    async def leader(self, ctx: commands.Context, *, character) -> None:
        character = check_nickname(character, "character")
        await self.grab_skill(ctx, character, 'leader')

    @commands.hybrid_command(name="class")
    async def class_passive(self, ctx: commands.Context, *, character) -> None:
        character = check_nickname(character, "character")
        await self.grab_skill(ctx, character, 'class')

    @commands.command(aliases=["SS", "2S", "2s", "s5", "S5"])
    async def ss(self, ctx: commands.Context, *, character) -> None:
        character = check_nickname(character, "character")
        await self.grab_skill(ctx, character, 'ss')

    @commands.command(aliases=["SSS", "3S", "3s", "SS3", "ss3"])
    async def sss(self, ctx: commands.Context, *, character) -> None:
        character = check_nickname(character, "character")
        await self.grab_skill(ctx, character, 'sss')

    @commands.command(name="s+", aliases=["s+", "SSS+", "S+", "3S+", "3s+"])
    async def splus(self, ctx: commands.Context, *, character) -> None:
        character = check_nickname(character, "character")
        await self.grab_skill(ctx, character, 's+')

    @commands.hybrid_command(aliases=["Leap"])
    async def leap(self, ctx: commands.Context, *, character) -> None:
        character = check_nickname(character, "character")
        await self.grab_skill(ctx, character, 'leap')

    @commands.hybrid_command(aliases=['ll'])
    async def leaplist(self, ctx: commands.Context) -> None:
        with open('data/leaplist.json') as file:
            parsed_json = json.load(file)
        embed = self.embedconf.create_list_embed("Leapable Units", "leaps", parsed_json['leaplist'], 1, 1)
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Skills(bot))
