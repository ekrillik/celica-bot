import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from utility.embedconfig import EmbedClass

class Help(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Help loaded.')

    @commands.command()
    async def help(self, ctx: commands.Context):
        commands = ["**?build**", "**?weapon/wep/weap/sig**", "**?skill, ?basic, ?red, ?yellow, ?blue, ?core, ?signature/ult, ?leader, ?qte, ?class, ?ss, ?sss, ?s+, ?leap**", "**?cub/pet**", "**?time/ppc**", "**?weaponlist**", "**?cublist**", "**?help**", "**?about**", "**?credits**"]
        # content="List of commands"
        embed = discord.Embed(
            title=f"Celica Bot Command List",
            description=f""
        )
        for i in commands:
            embed.add_field(
                name="",
                value=f"{i}",
                inline=False
            )

        await ctx.send(embed=embed)

    @commands.command()
    async def links(self, ctx: commands.Context):
        embed = discord.Embed(
            title=f"Useful Links",
            description=f""
        )
        embed.add_field(name="Officials", value=f"[Website](https://pgr.kurogame.net/)\n[Youtube](https://www.youtube.com/@PunishingGrayRaven)\n[BiliBili](https://space.bilibili.com/382651856)")
        embed.add_field(name="Wikis", value=f"[Gray Ravens](https://grayravens.com/wiki/GRAY_RAVENS)\n[Bili Wiki](https://wiki.biligame.com/zspms/%E9%A6%96%E9%A1%B5)")
        embed.add_field(name="Competitive Info", value=f"[Huaxu](https://huaxu.app/)")

        embed.add_field(name="Planning", value=f"[BC Planner](https://docs.google.com/spreadsheets/d/1nNauBXGcHv_7AepLWBLo4ykl3V_EhxpK)")

        embed.add_field(name="General Guides", value=f"[Zexous' Meta Spreadsheet](https://docs.google.com/spreadsheets/d/1SusxJ3tYwsBqY3dPwJ9BG2tDW0ox5GqVJgGZHYnAqa8)\n[Rexlent Beginner YT Playlist](https://www.youtube.com/watch?v=EHaKrXj643A&list=PLT669jfZO0z9OFd4fnfJxGc3Z71e-1FCg)")
        
        embed.add_field(name="Phantom Pain Cage", value=f"[SS Ultimate](https://docs.google.com/spreadsheets/d/16z8o9xw3NUhSAymJIRtsWyQsxqEndpgYS4OCb1GYyAQ)\n[SSS Ultimate](https://docs.google.com/spreadsheets/d/1p3-_Bqp4NEpqEVEFUqthxeVlvwu5uXzJSoHa8ZoN5yk)\n[S+ Ultimate](https://docs.google.com/spreadsheets/d/1YzOGbhTKaGTzfGbQJDdI6PSw8lXxcDpEQeeVLF4u2Dw)")

        embed.add_field(name="Warzone", value=f"[Advanced Warzone Tips](https://docs.google.com/document/d/1nJeLR5qIrq7SvueCGPDFz5KsMmYGVxUgqmxoRHZJ0GM)\n", inline=False)

        embed.add_field(name="Outdated Resources", value=f"[Story Reader](https://tf6ksijarp.github.io/)\n[Character 'Tier List by Doomy'](https://docs.google.com/spreadsheets/d/1nCmBq7NstZovPWs9cymAXNyakVXJ4lKvNGbVmtPbcUc)\n[Outdated Advanced PPC Spreadsheet](https://discord.com/channels/595893569609269251/663286717985456157/1283247685255696425)\n[Comprehensive Character Builds](https://docs.google.com/spreadsheets/d/1_NAHdVouSp2T6AwStpz9ZMLZ_ca5EzcuHde5obIlero)\n[Resource Calculator](https://docs.google.com/spreadsheets/d/1rfS6P1UOcZFj_ru2dqLzRkTE39Z0Phjbi5XDsOoNYRs)\n[Coatings Acquisition](https://docs.google.com/spreadsheets/d/1uIWrtp3mZEZgQseY788WHGp7_0mZBE8zSkpVOVCWtP8)")
        await ctx.send(embed=embed)

    @commands.command(aliases=["contentcreators"])
    async def cc(self, ctx: commands.Context):
        embed = discord.Embed(
            title=f"Content Creators",
            description=f""
        )
        embed.add_field(name="General Content", value=f"[Rexlent](https://www.youtube.com/@Rexlent)\n[Narushio](https://www.youtube.com/@narushio)\n[Moteyaba](https://www.youtube.com/@Moteyaba)\n[Spider2B](https://www.youtube.com/@Spider2B)")
        embed.add_field(name="PPC", value=f"[Windbell](https://www.youtube.com/@10thwindbell)\n[Fel](https://www.youtube.com/@FelPGR)\n[Acaxi](https://www.youtube.com/@notacaxi)\n[GlobalGlory](https://m.youtube.com/@GlobalGlorypgr)\n[Yor Forger](https://m.youtube.com/@yorforgerpgr)")
        embed.add_field(name="Warzone", value=f"[sNazz](https://www.youtube.com/@sNazzkun)\n[Empress](https://www.youtube.com/@Oksohee)\n[Setsu](https://www.youtube.com/@Setsugekwa)")
        embed.add_field(name="MMD", value="[KGEzre](https://www.youtube.com/channel/UCsv1LorzuEEqFoL08cEn61A)")
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot))

async def teardown(bot):
    print("Extension unloaded!")