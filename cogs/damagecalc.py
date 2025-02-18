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

    @commands.Cog.listener()
    async def on_ready(self):
        print('DamageCalc loaded.')
    
    @app_commands.command(name="eledamagecalculator", description="Performs a calculation on the estimated elemental damage for a particular skill.")
    @app_commands.describe(skillpc="Skill scaling percentage", baseatk="Base ATK of unit. This number is shown in the character stats screen and includes character base ATK stat, weapon ATK stat and total memory ATK stat.", atkpcup="Total ATK percentage increase", finalatk="Final ATK Stat. Obtained from CUB passive skill 2 and Incandescence/Glorious Afterglow weapon resonances", eledmg="Total elemental DMG % increase.", basedmg="Total Base DMG increase.", extradmg="Total Extra DMG Boost(EDB)/Increase", shred="Total Elemental Resist Down %", edrdownpc="Extra DMG Reduction Down %")
    async def eledamagecalculator(self, inter: discord.Interaction, skillpc: int, baseatk: int, atkpcup: int, finalatk: int, eledmg: int, basedmg: int, extradmg: int, shred: int, edrdownpc: int) -> None:

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

        finaldmgestimate = round(finaldmg,2)
        finaldmglower = round(finaldmg*0.9,2)
        finaldmgupper = round(finaldmg*1.1,2)

        embed = discord.Embed(
            title="Elemental DMG Calculator",
            description=f""
        )
        embed.add_field(name="", value=f"Skill Scaling: {skillpc}%", inline=False)
        embed.add_field(name="", value=f"Base ATK: {baseatk}", inline=False)
        embed.add_field(name="", value=f"Total ATK Percent Boost: {atkpcup}%", inline=False)
        embed.add_field(name="", value=f"Final ATK: {finalatk}", inline=False)
        embed.add_field(name="", value=f"Total Elemental DMG Boost: {eledmg}%", inline=False)
        embed.add_field(name="", value=f"Total Base DMG Boost: {basedmg}%", inline=False)
        embed.add_field(name="", value=f"Total Extra DMG Boost (EDB): {extradmg}%", inline=False)
        embed.add_field(name="", value=f"Total Shred (Elemental Resist Down): {shred}%", inline=False)
        embed.add_field(name="", value=f"Total EDR Down %: {edrdownpc}%", inline=False)

        embed.add_field(name=f"Total Elemental DMG Estimate:", value=f"**{finaldmgestimate}**", inline=False)
        embed.add_field(name=f"Estimated Range:", value=f"**{finaldmglower} - {finaldmgupper}**", inline=False)

        embed.add_field(name=f"**Assumptions taken into account:**", value=f"**- Base EDR is 0%\n- Base Elemental Resist is 20%**", inline=False)

        embed.add_field(name=f"Disclaimer", value=f"Do note that this number does not take into account the context in which this damage is being dealt. It just calculates an estimate of a skill being used in **one instance** based on all the buffs applied to the unit dealing the damage as well as the debuffs applied to the enemy.", inline=False)
        
        
        await inter.response.send_message(embed=embed)

    #Skill Scaling Percentage x (Base ATK x (1 + ATK Increase) + Final ATK) x (1 + Elemental DMG Increase) x (1 + Base DMG Increase) x (1 + Extra DMG Increase) x (1 - Elemental Resistance) x (1 - Extra DMG Reduction) = Final DMG Output

    @app_commands.command(name="physdamagecalculator", description="Performs a calculation on the estimated physical damage for a particular skill.")
    @app_commands.describe(skillpc="Skill scaling percentage", baseatk="Base ATK of unit. This number is shown in the character stats screen and includes character base ATK stat, weapon ATK stat and total memory ATK stat.", atkpcup="Total ATK percentage increase", finalatk="Final ATK Stat. Obtained from CUB passive skill 2 and Incandescence/Glorious Afterglow weapon resonances", critdmg="Total Crit DMG % increase", physdmg="Total physical DMG % increase.", basedmg="Total Base DMG increase.", extradmg="Total Extra DMG Boost(EDB)/Increase", physresshred="Total Physical Resist Down %", edrdownpc="Extra DMG Reduction Down %")
    async def physdamagecalculator(self, inter: discord.Interaction, skillpc: int, baseatk: int, atkpcup: int, finalatk: int, critdmg: int, physdmg: int, basedmg: int, extradmg: int, physresshred: int, edrdownpc: int) -> None:

        skillscaling = float(skillpc)/100
        critdmgpercentup = float(critdmg)/100
        attackpercentup = float(atkpcup)/100
        physboost = float(physdmg)/100
        basedmgboost = float(basedmg)/100
        extradmgboost = float(extradmg)/100
        finalphysresist = float(physresshred)/100-0.2
        # finaldef = float(defshred)/100
        finaledr = float(edrdownpc)/100-0.2

        print(f"Skill Scaling: {skillscaling}")
        print(f"Total ATK Percent Boost: {attackpercentup}")
        print(f"Total Crit DMG Boost: {critdmgpercentup}")
        print(f"Total Phys DMG Boost: {physboost}")
        print(f"Total Base DMG Boost: {basedmgboost}")
        print(f"Total Extra Damage Boost (EDB): {extradmgboost}")
        # print(f"Total DEF %: {finaleleresist}")
        print(f"Total Phys Resistance: {finalphysresist}")
        print(f"Total Extra DMG Reduction: {finaledr}")

        # finaldmgnocrit = skillscaling*(baseatk*(1+attackpercentup)+finalatk)*(1+physboost)*(1+basedmgboost)*(1+extradmgboost)*(1-finalphysresist)*(1-newdef)*(1-finaledr)
        finaldmgnocrit = skillscaling*(baseatk*(1+attackpercentup)+finalatk)*(1+physboost)*(1+basedmgboost)*(1+extradmgboost)*(1-finalphysresist)*(1-finaledr)

        finaldmgnocrit_lowfloat = finaldmgnocrit*0.95
        finaldmgnocrit_highfloat = finaldmgnocrit*1.05

        finaldmgcrit = (2 + critdmg)*skillscaling*(baseatk*(1+attackpercentup)+finalatk)*(1+physboost)*(1+basedmgboost)*(1+extradmgboost)*(1-finalphysresist)*(1-finaledr)

        finaldmgcrit_lowfloat = finaldmgcrit*0.95
        finaldmgcrit_highfloat = finaldmgcrit*1.05

        # Skill Scaling Percentage x (Base ATK x (1 + ATK Increase) + Final ATK) x (1 + Phys DMG Increase) x (1 + Base DMG Increase) x (1 + Extra DMG Increase) x (1 - New DEF Stat) x (1 - Physical Resistance) x (1 - Extra DMG Reduction) x Float = Final DMG Output

        # (2 + Crit DMG Increase) x Skill Scaling Percentage x (Base ATK x (1 + ATK Increase) + Final ATK) x (1 + Phys DMG Increase) x (1 + Base DMG Increase) x (1 + Extra DMG Increase) x (1 - New DEF Stat) x (1 - Physical Resistance) x (1 - Extra DMG Reduction) x Float = Final DMG Output

        finaldmg_nocrit_estimate_lowfloat = round(finaldmgnocrit_lowfloat,2)
        finaldmg_nocrit_lower_lowfloat = round(finaldmgnocrit_lowfloat*0.9,2)
        finaldmg_nocrit_upper_lowfloat = round(finaldmgnocrit_lowfloat*1.1,2)

        finaldmg_nocrit_estimate_highfloat = round(finaldmgnocrit_highfloat,2)
        finaldmg_nocrit_lower_highfloat = round(finaldmgnocrit_highfloat*0.9,2)
        finaldmg_nocrit_upper_highfloat = round(finaldmgnocrit_highfloat*1.1,2)

        finaldmg_crit_estimate_lowfloat = round(finaldmgcrit_lowfloat,2)
        finaldmg_crit_lower_lowfloat = round(finaldmgcrit_lowfloat*0.9,2)
        finaldmg_crit_upper_lowfloat = round(finaldmgcrit_lowfloat*1.1,2)

        finaldmg_crit_estimate_highfloat = round(finaldmgcrit_highfloat,2)
        finaldmg_crit_lower_highfloat = round(finaldmgcrit_highfloat*0.9,2)
        finaldmg_crit_upper_highfloat = round(finaldmgcrit_highfloat*1.1,2)

        embed = discord.Embed(
            title="Physical DMG Calculator",
            description=f""
        )
        embed.add_field(name="", value=f"Skill Scaling: {skillpc}%", inline=False)
        embed.add_field(name="", value=f"Base ATK: {baseatk}", inline=False)
        embed.add_field(name="", value=f"Total ATK % Boost: {atkpcup}%", inline=False)
        embed.add_field(name="", value=f"Final ATK: {finalatk}", inline=False)
        embed.add_field(name="", value=f"Total Crit DMG % Boost: {critdmg}%", inline=False)
        embed.add_field(name="", value=f"Total Phys DMG % Boost: {physdmg}%", inline=False)
        embed.add_field(name="", value=f"Total Base DMG Boost: {basedmg}%", inline=False)
        embed.add_field(name="", value=f"Total Extra DMG Boost (EDB): {extradmg}%", inline=False)
        embed.add_field(name="", value=f"Total Phys Shred (Phys Resist Down): {physresshred}%", inline=False)
        embed.add_field(name="", value=f"Total EDR Down %: {edrdownpc}%", inline=False)

        embed.add_field(name=f"Total Phys DMG Estimate - Low Float(No Crit):", value=f"**{finaldmg_nocrit_estimate_lowfloat}**", inline=False)
        embed.add_field(name=f"Estimated Range - Low Float(No Crit):", value=f"**{finaldmg_nocrit_lower_lowfloat} - {finaldmg_nocrit_upper_lowfloat}**", inline=False)

        embed.add_field(name=f"Total Phys DMG Estimate - High Float(No Crit):", value=f"**{finaldmg_nocrit_estimate_highfloat}**", inline=False)
        embed.add_field(name=f"Estimated Range - High Float(No Crit):", value=f"**{finaldmg_nocrit_lower_highfloat} - {finaldmg_nocrit_upper_highfloat}**", inline=False)

        embed.add_field(name=f"Total Phys DMG Estimate - Low Float(Crit):", value=f"**{finaldmg_crit_estimate_lowfloat}**", inline=False)
        embed.add_field(name=f"Estimated Range - Low Float(Crit):", value=f"**{finaldmg_crit_lower_lowfloat} - {finaldmg_crit_upper_lowfloat}**", inline=False)

        embed.add_field(name=f"Total Phys DMG Estimate - High Float(Crit):", value=f"**{finaldmg_crit_estimate_highfloat}**", inline=False)
        embed.add_field(name=f"Estimated Range - High Float(Crit):", value=f"**{finaldmg_crit_lower_highfloat} - {finaldmg_crit_upper_highfloat}**", inline=False)

        embed.add_field(name=f"Disclaimer", value=f"Do note that this number does not take into account the context in which this damage is being dealt. It just calculates an estimate of a skill being used in **one instance** based on all the buffs applied to the unit dealing the damage as well as the debuffs applied to the enemy.",
         inline=False)
        
        embed.add_field(name=f"Assumptions taken into account:", value=f"- DEF has been reduced by 100%\n- Base EDR is 0%\n- Base Phys Resist is 0%", inline=False)

        await inter.response.send_message(embed=embed)

        

async def setup(bot: commands.Bot):
    await bot.add_cog(DamageCalc(bot))
