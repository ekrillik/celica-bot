import json

from discord import app_commands
from discord.ext import commands
from utility.embedconfig import EmbedClass
from utility.nickname_checker import check_nickname, character_theme
from utility.wep_pagination import WeaponPageView
from utility.general_view import GeneralView
from utility.fuzzymatch import fuzzmatch

class Weapons(commands.Cog):
    weapons = {}
    weapon_types = {}

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

        with open('data/weapons.json') as file:
            self.weapons = json.load(file)
        with open('data/weapontypes.json') as file:
            self.weapon_types = json.load(file)
        with open('data/resos.json') as file:
            self.resos = json.load(file)

    @commands.Cog.listener()
    async def on_ready(self):
        print('Weapons loaded.')

    @commands.hybrid_command(aliases=['Sig', 'sig', 'Wep', 'wep', 'Weap', 'weap'], description="Displays info on an existing weapon.")
    @app_commands.rename(weapon_name='name')
    async def weapon(self, ctx: commands.Context, *, weapon_name) -> None:
        weapon_name = weapon_name.lower()

        if (weapon := self.weapons.get(weapon_name)) is not None:
            embed = self.embedconf.create_weapon_embed(weapon)
            await ctx.send(embed=embed)
            return

        name = fuzzmatch(weapon_name)
        if name == "":
            name = weapon_name
        character_name = check_nickname(name, "character")
        theme = character_theme(character_name)
        weapon_name = check_nickname(name, "weapon")
        weapon = self.weapons.get(weapon_name)
        if weapon is None:
            await ctx.send(content=f"{weapon_name} is not a valid weapon name. Please try again.")
            return

        same_type_weapons_list = self.weapon_types[weapon['weapon_type'].lower()]

        weapon_box = [
            self.weapons[name] for name in same_type_weapons_list if self.weapons[name]['rarity'] < 6
        ] + [weapon]

        embed = self.embedconf.create_weapon_embed(weapon, user=theme[2], chibi_avatar=theme[1])
        view = WeaponPageView(ctx.author, weapon_box=weapon_box, theme=theme)
        view.current_page = "6★"
        view.update_buttons()
        view.message = await ctx.send(view=view, embed=embed)

    @commands.hybrid_command(aliases=['reso'], description="Displays recommended resonances for each unit.")
    async def resonance(self, ctx: commands.Context, *, frame_name) -> None:
        name = fuzzmatch(frame_name)
        if name == "":
            name = frame_name
        character = check_nickname(name, "character")

        reso = self.resos.get(character, None)
        if reso is None:
            content = ('This character does not exist. Please try again.\nYou may be searching for a character with '
                       'multiple frames as well.')
            await ctx.send(content=content)
            return
        
        data = reso

        theme = character_theme(character)
        if 'alternate' in data:
            embed = self.embedconf.create_reso_embed(name=theme[2], main_list=data['main'], alt_list=data['alternate'], colour=theme[0], thumbnail_url=theme[3])
        else:
            embed = self.embedconf.create_reso_embed(name=theme[2], main_list=data['main'], colour=theme[0], thumbnail_url=theme[3])
        view = GeneralView(ctx.author)
        view.message = await ctx.send(view=view, embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Weapons(bot))
