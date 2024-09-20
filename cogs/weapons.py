import json

from discord import app_commands
from discord.ext import commands
from utility.embedconfig import EmbedClass
from utility.nickname_checker import check_nickname, character_theme
from utility.wep_pagination import WeaponPageView

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

    @commands.Cog.listener()
    async def on_ready(self):
        print('Weapons loaded.')

    @commands.hybrid_command(aliases=["sig", "wep", "weap"])
    @app_commands.rename(weapon_name='name')
    async def weapon(self, ctx: commands.Context, *, weapon_name) -> None:
        weapon_name = weapon_name.lower()

        if (weapon := self.weapons.get(weapon_name)) is not None:
            embed = self.embedconf.create_weapon_embed(weapon)
            await ctx.send(embed=embed)
            return

        character_name = check_nickname(weapon_name, "character")
        theme = character_theme(character_name)
        weapon_name = check_nickname(weapon_name, "weapon")
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


async def setup(bot: commands.Bot):
    await bot.add_cog(Weapons(bot))
