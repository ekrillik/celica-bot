from __future__ import annotations

import json

from discord.ext import commands

from utility.embedconfig import EmbedClass
from utility.general_view import GeneralView
from utility.nickname_checker import check_nickname, character_theme
from utility.pagination import PaginationView
from utility.skills_menu import SkillsView
from utility.fuzzymatch import fuzzmatch

class Skills(commands.Cog):
    skills = {}

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()
        self.level_not_in_range = False

        with open('data/skills.json') as file:
            self.skills = json.load(file)

    async def grab_skill(self, ctx, character, skill_type, level = 18):
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

        if skill_type in ['Leap', 'Basic Attack', 'Red Orb', 'Yellow Orb', 'Blue Orb']and len(skill) > 1:
            view = PaginationView(ctx.author, data=skill, pagination_type="skills", skill_type=skill_type, theme=theme, level=level)
        elif skill_type in ['Core Passive', 'Signature/Ultimate'] and len(skill['skills']) > 1 :
            view = PaginationView(ctx.author, data=skill, pagination_type="skills", skill_type=skill_type, theme=theme, level=level)
        else:
            view = GeneralView(ctx.author)

        embed = self.embedconf.skillsEmbed(skill, skill_type, colour=theme[0], chibi_avatar=theme[1], user=theme[2], thumbnail=theme[3], level=level)
        if self.level_not_in_range == True:
            view.message = await ctx.send(content="Invalid skill level, value defaulted to 18.", embed=embed, view=view)
            self.level_not_in_range = False
        else:
            view.message = await ctx.send(embed=embed, view=view)

    @commands.Cog.listener()
    async def on_ready(self):
        print('Skills loaded.')

    @commands.hybrid_command(description="Displays a skill menu for a particular character.")
    async def skills(self, ctx: commands.Context, *, frame) -> None:
        level = 0
        nickname = ""
        str_array = frame.split(" ")
        if str_array[len(str_array) - 1].isdigit():
            if int(str_array[len(str_array) - 1]) > 0 and int(str_array[len(str_array) - 1]) < 26:
                level = int(str_array[len(str_array) - 1])
                str_array.pop()
            else:
                self.level_not_in_range = True
                level = 18
                str_array.pop()
        else:
            level = 18
        nickname = " ".join(str_array)
        
        name = fuzzmatch(nickname)
        if name == "":
            name = nickname
        character = check_nickname(name, "character")

        if character != "":
            theme = character_theme(character)

            skills = self.skills.get(character)
            embed = self.embedconf.skillsEmbed(skills['basic_attack'], "Basic Attack", colour=theme[0], chibi_avatar=theme[1], user=theme[2], thumbnail=theme[3], level=level)
            
            view = SkillsView(ctx.author, skills=skills, theme=theme, level=level)
            if self.level_not_in_range == True:
                view.message = await ctx.send(content="Invalid skill level, value defaulted to 18.", embed=embed, view=view)
            else:
                view.message = await ctx.send(embed=embed, view=view)
        else:
            await ctx.send(content=f"The name {frame} does not exist!")

    @commands.hybrid_command(aliases=['Basic'], description="Displays the basic attack skill for a particular character.")
    async def basic(self, ctx: commands.Context, *, frame) -> None:
        level = 0
        nickname = ""
        str_array = frame.split(" ")
        if str_array[len(str_array) - 1].isdigit():
            if int(str_array[len(str_array) - 1]) > 0 and int(str_array[len(str_array) - 1]) < 26:
                level = int(str_array[len(str_array) - 1])
                str_array.pop()
            else:
                self.level_not_in_range = True
                level = 18
                str_array.pop()
        else:
            level = 18
        nickname = " ".join(str_array)

        name = fuzzmatch(nickname)
        if name == "":
            name = nickname
        character = check_nickname(name, "character")
        await self.grab_skill(ctx, character, 'basic', level)

    @commands.hybrid_command(aliases=['Red'], description="Displays the red orb skill for a particular character.")
    async def red(self, ctx: commands.Context, *, frame) -> None:
        level = 0
        nickname = ""
        str_array = frame.split(" ")
        if str_array[len(str_array) - 1].isdigit():
            if int(str_array[len(str_array) - 1]) > 0 and int(str_array[len(str_array) - 1]) < 26:
                level = int(str_array[len(str_array) - 1])
                str_array.pop()
            else:
                self.level_not_in_range = True
                level = 18
                str_array.pop()
        else:
            level = 18
        nickname = " ".join(str_array)

        name = fuzzmatch(nickname)
        if name == "":
            name = nickname
        character = check_nickname(name, "character")
        await self.grab_skill(ctx, character, 'red', level)

    @commands.hybrid_command(aliases=['Yellow'], description="Displays the yellow orb skill for a particular character.")
    async def yellow(self, ctx: commands.Context, *, frame) -> None:
        level = 0
        nickname = ""
        str_array = frame.split(" ")
        if str_array[len(str_array) - 1].isdigit():
            if int(str_array[len(str_array) - 1]) > 0 and int(str_array[len(str_array) - 1]) < 26:
                level = int(str_array[len(str_array) - 1])
                str_array.pop()
            else:
                self.level_not_in_range = True
                level = 18
                str_array.pop()
        else:
            level = 18
        nickname = " ".join(str_array)

        name = fuzzmatch(nickname)
        if name == "":
            name = nickname
        character = check_nickname(name, "character")
        await self.grab_skill(ctx, character, 'yellow', level)

    @commands.hybrid_command(aliases=['Blue'], description="Displays the blue orb skill for a particular character.")
    async def blue(self, ctx: commands.Context, *, frame) -> None:
        level = 0
        nickname = ""
        str_array = frame.split(" ")
        if str_array[len(str_array) - 1].isdigit():
            if int(str_array[len(str_array) - 1]) > 0 and int(str_array[len(str_array) - 1]) < 26:
                level = int(str_array[len(str_array) - 1])
                str_array.pop()
            else:
                self.level_not_in_range = True
                level = 18
                str_array.pop()
        else:
            level = 18
        nickname = " ".join(str_array)

        name = fuzzmatch(nickname)
        if name == "":
            name = nickname
        character = check_nickname(name, "character")
        await self.grab_skill(ctx, character, 'blue', level)

    @commands.hybrid_command(aliases=['Core'], description="Displays the core passive skill for a particular character.")
    async def core(self, ctx: commands.Context, *, frame) -> None:
        level = 0
        nickname = ""
        str_array = frame.split(" ")
        if str_array[len(str_array) - 1].isdigit():
            if int(str_array[len(str_array) - 1]) > 0 and int(str_array[len(str_array) - 1]) < 26:
                level = int(str_array[len(str_array) - 1])
                str_array.pop()
            else:
                self.level_not_in_range = True
                level = 18
                str_array.pop()
        else:
            level = 18
        nickname = " ".join(str_array)

        name = fuzzmatch(nickname)
        if name == "":
            name = nickname
        character = check_nickname(name, "character")
        await self.grab_skill(ctx, character, 'core', level)

    @commands.hybrid_command(aliases=['Signature', 'ult', 'Ult', 'ultimate', 'Ultimate'], description="Displays the signature skill/ultimate for a particular character.")
    async def signature(self, ctx: commands.Context, *, frame) -> None:
        level = 0
        nickname = ""
        str_array = frame.split(" ")
        if str_array[len(str_array) - 1].isdigit():
            if int(str_array[len(str_array) - 1]) > 0 and int(str_array[len(str_array) - 1]) < 26:
                level = int(str_array[len(str_array) - 1])
                str_array.pop()
            else:
                self.level_not_in_range = True
                level = 18
                str_array.pop()
        else:
            level = 18   
        nickname = " ".join(str_array)

        name = fuzzmatch(nickname)
        if name == "":
            name = nickname
        character = check_nickname(name, "character")
        await self.grab_skill(ctx, character, 'signature', level)

    @commands.hybrid_command(aliases=['QTE', 'Qte'], description="Displays the QTE skill for a particular character.")
    async def qte(self, ctx: commands.Context, *, frame) -> None:
        level = 0
        nickname = ""
        str_array = frame.split(" ")
        if str_array[len(str_array) - 1].isdigit():
            if int(str_array[len(str_array) - 1]) > 0 and int(str_array[len(str_array) - 1]) < 26:
                level = int(str_array[len(str_array) - 1])
                str_array.pop()
            else:
                self.level_not_in_range = True
                level = 18
                str_array.pop()
        else:
            level = 18
        nickname = " ".join(str_array)

        name = fuzzmatch(nickname)
        if name == "":
            name = nickname
        character = check_nickname(name, "character")
        await self.grab_skill(ctx, character, 'qte', level)

    @commands.hybrid_command(aliases=['Leader'], description="Displays the leader passive skill for a particular character.")
    async def leader(self, ctx: commands.Context, *, frame) -> None:
        nickname = ""
        str_array = frame.split(" ")
        if str_array[len(str_array) - 1].isdigit():
            str_array.pop()
        nickname = " ".join(str_array)

        name = fuzzmatch(nickname)
        if name == "":
            name = nickname
        character = check_nickname(name, "character")
        await self.grab_skill(ctx, character, 'leader')

    @commands.hybrid_command(name="class", aliases=['Class'], description="Displays the class passive skill for a particular character.")
    async def class_passive(self, ctx: commands.Context, *, frame) -> None:
        level = 0
        nickname = ""
        str_array = frame.split(" ")
        if str_array[len(str_array) - 1].isdigit():
            if int(str_array[len(str_array) - 1]) > 0 and int(str_array[len(str_array) - 1]) < 26:
                level = int(str_array[len(str_array) - 1])
                str_array.pop()
            else:
                self.level_not_in_range = True
                level = 18
                str_array.pop()
        else:
            level = 18      
        nickname = " ".join(str_array)

        name = fuzzmatch(nickname)
        if name == "":
            name = nickname
        character = check_nickname(name, "character")
        await self.grab_skill(ctx, character, 'class', level)

    @commands.hybrid_command(aliases=['SS', '2S', '2s', 's5', 'S5'], description="Displays the SS rank skills for a particular character.")
    async def ss(self, ctx: commands.Context, *, frame) -> None:
        nickname = ""
        str_array = frame.split(" ")
        if str_array[len(str_array) - 1].isdigit():
            str_array.pop()
        nickname = " ".join(str_array)

        name = fuzzmatch(nickname)
        if name == "":
            name = nickname
        character = check_nickname(name, "character")
        await self.grab_skill(ctx, character, 'ss')

    @commands.hybrid_command(aliases=['SSS', '3S', '3s', 'SS3', 'ss3'], description="Displays the SSS rank skills for a particular character.")
    async def sss(self, ctx: commands.Context, *, frame) -> None:
        nickname = ""
        str_array = frame.split(" ")
        if str_array[len(str_array) - 1].isdigit():
            str_array.pop()     
        nickname = " ".join(str_array)

        name = fuzzmatch(nickname)
        if name == "":
            name = nickname
        character = check_nickname(name, "character")
        await self.grab_skill(ctx, character, 'sss')

    @commands.hybrid_command(name="splus", aliases=['s+', 'SSS+', 'S+', '3S+', '3s+', 'sss+', 'sss3', 'sss6', 'SSS3', 'SSS6'], description="Displays the S+ rank skills for a particular character.")
    async def splus(self, ctx: commands.Context, *, frame) -> None:
        nickname = ""
        str_array = frame.split(" ")
        if str_array[len(str_array) - 1].isdigit():
            str_array.pop()
        nickname = " ".join(str_array)

        name = fuzzmatch(nickname)
        if name == "":
            name = nickname
        character = check_nickname(name, "character")
        await self.grab_skill(ctx, character, 's+')

    @commands.hybrid_command(aliases=['Leap'], description="Displays the leap skills for a particular character.")
    async def leap(self, ctx: commands.Context, *, frame) -> None:
        nickname = ""
        str_array = frame.split(" ")
        if str_array[len(str_array) - 1].isdigit():
            str_array.pop()
        nickname = " ".join(str_array)

        name = fuzzmatch(nickname)
        if name == "":
            name = nickname
        character = check_nickname(name, "character")
        await self.grab_skill(ctx, character, 'leap')

    @commands.hybrid_command(aliases=['Leaplist', 'LeapList', 'll'], description="Displays a list of existing characters with leap skills.")
    async def leaplist(self, ctx: commands.Context) -> None:
        with open('data/leaplist.json') as file:
            parsed_json = json.load(file)
        embed = self.embedconf.create_list_embed("Leapable Units", "leaps", parsed_json['leaplist'], 1, 1)
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Skills(bot))
