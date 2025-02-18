import json
import discord
from discord.ext import commands
from discord import app_commands
from utility.embedconfig import EmbedClass
from utility.pagination import PaginationView


class DamageCalc(commands.Cog):
    credits = {}

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

        # with open('data/credits.json') as file:
        #     self.credits = json.load(file)['credits']

    @commands.Cog.listener()
    async def on_ready(self):
        print('DamageCalc loaded.')

    
    # @app_commands.describe(skillpc="Skill scaling percentage", baseatk="Base ATK of unit. This number is shown in the character stats screen and includes character base ATK stat, weapon ATK stat and total memory ATK stat.", atkpcup="Total ATK percentage increase", finalatk="Final ATK Stat. Obtained from CUB passive skill 2 and Incandescence/Glorious Afterglow weapon resonances", eledmg="Total elemental DMG % increase.", basedmg="Total Base DMG increase.", extradmg="Total Extra DMG Boost(EDB)/Increase", shred="Total Elemental Resist Down %", edrdownpc="Extra DMG Reduction Down %")
    @app_commands.command(name="damagecalculator", description="Performs a calculation on the estimated damage for a particular skill.")
    async def damagecalculator(self, ctx: commands.Context, skillpc: int, baseatk: int, atkpcup: int, finalatk: int, eledmg: int, basedmg: int, extradmg: int, shred: int, edrdownpc: int) -> None:

        skillscaling = float(skillpc)/100
        attackpercentup = float(atkpcup)/100
        elementalboost = float(eledmg)/100
        basedmgboost = float(basedmg)/100
        extradmgboost = float(extradmg)/100
        finaleleresist = float(shred)/100-0.2
        finaledr = float(edrdownpc)/100-0.2

        print(f"Skill Scaling: {skillscaling}")
        print(f"Total ATK Percent Boost: {attackpercentup}")
        print(f"Total Elemental DMG Boost: {elementalboost}")
        print(f"Total Base DMG Boost: {basedmgboost}")
        print(f"Total Extra Damage Boost (EDB): {extradmgboost}")
        print(f"Total Elemental Resistance: {finaleleresist}")
        print(f"Total Extra DMG Reduction: {finaledr}")

        finaldmg = skillscaling*(baseatk*(1+attackpercentup)+finalatk)*(1+elementalboost)*(1+basedmgboost)*(1+extradmgboost)*(1-finaleleresist)*(1-finaledr)

        embed = discord.Embed(
            title="Elemental DMG Calculator",
            description=f""
        )
        embed.add_field(name="", value=f"Skill Scaling: {skillpc}", inline=False)
        embed.add_field(name="", value=f"Total ATK Percent Boost: {atkpcup}", inline=False)
        embed.add_field(name="", value=f"Total Elemental DMG Boost: {elementalboost}", inline=False)
        embed.add_field(name="", value=f"Total Base DMG Boost: {elementalboost}", inline=False)
        embed.add_field(name="", value=f"Total Extra DMG Boost (EDB): {elementalboost}", inline=False)
        embed.add_field(name="", value=f"Total Shred (Elemental Resist Down): {elementalboost}", inline=False)
        embed.add_field(name="", value=f"Total EDR Down %: {elementalboost}", inline=False)

        embed.add_field(name="Total DMG:", value=f"{finaldmg}", inline=False)
        
        await ctx.send(embed=embed)

#Skill Scaling Percentage x (Base ATK x (1 + ATK Increase) + Final ATK) x (1 + Elemental DMG Increase) x (1 + Base DMG Increase) x (1 + Extra DMG Increase) x (1 - Elemental Resistance) x (1 - Extra DMG Reduction) = Final DMG Output

async def setup(bot: commands.Bot):
    await bot.add_cog(DamageCalc(bot))
