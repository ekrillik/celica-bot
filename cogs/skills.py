
from __future__ import annotations

import typing
import traceback
import discord
import os
import json
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from utility.embedconfig import EmbedClass
from utility.build_dropdown import DropdownView
from utility.nickname_checker import check_nickname, character_theme
from utility.skills_menu import SkillsView
from utility.pagination import PaginationView
from utility.general_view import GeneralView

from discord.ui.select import BaseSelect

class Skills(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

    def retrieve_skills(self, character):
        with open('data/skills.json') as file:
            parsed_json = json.load(file)
        return parsed_json[character]

    def does_character_exist(self, character):
        with open('data/characterlist.json') as file:
            parsed_json = json.load(file)
        framelist = parsed_json['characterlist']
        exists = False

        for i in framelist:
            if character == i:
                exists = True
                break
            else:
                exists = False

        return exists

    async def grab_skill(self, ctx, character, skill_type):
        if(self.does_character_exist(character)):
            skillset = self.retrieve_skills(character)
            match skill_type:
                case 'basic':
                    skill = skillset['basic_attack']
                    skill_type = 'Basic Attack'
                    skill_len = len(skill)
                case 'red':
                    skill = skillset['red_orb']
                    skill_type = 'Red Orb'
                    skill_len = len(skill)
                case 'yellow':
                    skill = skillset['yellow_orb']
                    skill_type = 'Yellow Orb'
                    skill_len = len(skill)
                case 'blue':
                    skill = skillset['blue_orb']
                    skill_type = 'Blue Orb'
                    skill_len = len(skill)
                case 'core':
                    skill = skillset['core_passive']
                    skill_type = 'Core Passive'
                    skill_len = len(skill['skills'])
                case 'signature':
                    skill = skillset['signature']
                    skill_type = 'Signature/Ultimate'
                    skill_len = len(skill['skills'])
                case 'qte':
                    skill = skillset['qte']
                    skill_type = 'QTE'
                    skill_len = 0
                case 'leader':
                    skill = skillset['leader']
                    skill_type = 'Leader Passive'
                    skill_len = 0
                case 'class':
                    skill = skillset['class']
                    skill_type = 'Class Passive'
                    skill_len = 0
                case 'ss':
                    skill = skillset['ss_rank']
                    skill_type = 'SS'
                    skill_len = 0
                case 'sss':
                    skill = skillset['sss_rank']
                    skill_type = 'SSS'
                    skill_len = 0
                case 's+':
                    skill = skillset['s+_rank']
                    skill_type = 'S+'
                    skill_len = 0
                case 'leap':
                    if 'leap' in skillset:
                        skill = skillset['leap']
                        skill_type = 'Leap'
                        skill_len = len(skillset['leap'])
                    else:
                        await ctx.send("This character does not have Leap skills.")

            theme = character_theme(character)

            if skill_type == 'Leap' or skill_type == 'Core Passive' or skill_type == 'Basic Attack' or skill_type == 'Red Orb' or skill_type == 'Yellow Orb' or skill_type == 'Blue Orb' or skill_type == 'Signature/Ultimate':
                if len(skill) > 1:
                    print(skill_len)
                    embed = self.embedconf.skillsEmbed(skill, skill_type, colour=theme[0], chibi_avatar=theme[1], user=theme[2], thumbnail=theme[3])
                    view = PaginationView(ctx.author, data=skill, pagination_type="skills", skill_type=skill_type, theme=theme)
                    view.message = await ctx.send(embed=embed, view=view)
                else:
                    embed = self.embedconf.skillsEmbed(skill, skill_type, colour=theme[0], chibi_avatar=theme[1], user=theme[2], thumbnail=theme[3])
                    view = GeneralView(ctx.author)
                    view.message = await ctx.send(embed=embed, view=view)
            else:
                embed = self.embedconf.skillsEmbed(skill, skill_type, colour=theme[0], chibi_avatar=theme[1], user=theme[2], thumbnail=theme[3])
                view = GeneralView(ctx.author)
                view.message = await ctx.send(embed=embed, view=view)
        else:
            content = "This character does not exist. Please try again."
            await ctx.send(content=content)


    @commands.Cog.listener()
    async def on_ready(self):
        print('Skills loaded.')

    @commands.command(aliases=["skills"])
    async def skill(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        character = check_nickname(character, "character")

        theme = character_theme(character)

        skills = self.retrieve_skills(character)
        embed = self.embedconf.skillsEmbed(skills['basic_attack'], "Basic Attack", colour=theme[0], chibi_avatar=theme[1], user=theme[2], thumbnail=theme[3])
        view = SkillsView(ctx.author, skills=skills, theme=theme)
        view.message = await ctx.send(embed=embed, view=view)

    @commands.command()
    async def basic(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]
        
        print(character)

        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 'basic')
    
    @commands.command()
    async def red(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        
        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 'red')
    
    @commands.command()
    async def yellow(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        
        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 'yellow')

    @commands.command()
    async def blue(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        
        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 'blue')

    @commands.command()
    async def core(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        
        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 'core')
        
    @commands.command(aliases=['ult', 'ultimate'])
    async def signature(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        
        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 'signature')

    @commands.command()
    async def qte(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        
        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 'qte')

    @commands.command()
    async def leader(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        
        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 'leader')

    @commands.command(name="class")
    async def class_passive(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        
        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 'class')

    @commands.command(aliases=["SS", "2S", "2s", "s5", "S5"])
    async def ss(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        
        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 'ss')

    @commands.command(aliases=["SSS", "3S", "3s", "SS3", "ss3"])
    async def sss(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        
        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 'sss')

    @commands.command(name="sss+", aliases=["s+", "SSS+", "S+", "3S+", "3s+"])
    async def splus(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        
        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 's+')
    
    @commands.command(aliases=["Leap"])
    async def leap(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        
        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 'leap')

    @commands.command()
    async def leaplist(self, ctx: commands.Context) -> None:

        
        await ctx.send(content="Leap List")

async def setup(bot: commands.Bot):
    await bot.add_cog(Skills(bot))

async def teardown(bot):
    print("Extension unloaded!")