import discord
import os
import json
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from utility.embedconfig import EmbedClass
from utility.pagination import PaginationView

class Fun(commands.Cog): 

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()
        self.disallowed_server_ids = [1285561465537040384, 595893569609269251, 361043659107467264]
        self.allowed_server_ids = [1280331315115327488, 1272185726699573358]

    # The following commands are restricted to specific servers/not usable within PGR:O

    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun loaded.')

    @commands.command()
    async def fun(self, ctx: commands.Context) -> None:
        if ctx.guild.id not in self.disallowed_server_ids:
            embed = discord.Embed(title="This is a fun command.", description="This is a fun command description")
            await ctx.send(embed=embed)

    @commands.command()
    async def pasta(self, ctx: commands.Context) -> None:
        if ctx.guild.id in self.allowed_server_ids:
            embed = discord.Embed(title="This is a pasta.", description="This is a pasta")
            await ctx.send(embed=embed)

    @commands.command()
    async def dalaos(self, ctx: commands.Context) -> None:
        if ctx.guild.id not in self.disallowed_server_ids:
            embed = discord.Embed(
                title=f"Dalaos",
                description=f""
            )
            embed.add_field(name="PPC", value=f"[Windbell](https://www.youtube.com/@10thwindbell)\n[Fel](https://www.youtube.com/@FelPGR)\n[Acaxi](https://www.youtube.com/@notacaxi)\n[GlobalGlory](https://m.youtube.com/@GlobalGlorypgr)\n[Yor Forger](https://m.youtube.com/@yorforgerpgr)")
            embed.add_field(name="Warzone", value=f"[sNazz](https://www.youtube.com/@sNazzkun)\n[Empress](https://www.youtube.com/@Oksohee)\n[Setsu](https://www.youtube.com/@Setsugekwa)")
            await ctx.send(embed=embed)

    @commands.command()
    async def bubblewrap(self, ctx: commands.Context) -> None:
        if ctx.guild.id in self.allowed_server_ids:
            embed = discord.Embed(title="Free Bubble Wrap", description="")
            embed.add_field(name="", value=f"||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop||")
            await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Fun(bot))

async def teardown(bot):
    print("Extension unloaded!")