import discord
import os
import json
import time
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
        self.pasta_command_ran = False
        self.bubblewrap_command_ran = False
        self.last_pasta_command_ran = 0.00
        self.last_bubblewrap_command_ran = 0.00

    # The following commands are restricted to specific servers/not usable within PGR:O
    # Disallowed Servers: Dud bot testing server, PGR:O, Personal Discord Server 
    # Allowed Servers: Celica's Office, Nnin's Corner 

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
            start = time.time()
            if(self.pasta_command_ran == True):
                if((start - self.last_pasta_command_ran) > 5 ):
                    self.pasta_command_ran = False

            if(self.pasta_command_ran == False):
                self.pasta_command_ran = True
                self.last_pasta_command_ran = start
                embed = discord.Embed(title="This is a pasta.", description="This is a pasta")
                await ctx.send(embed=embed)
            else:
                await ctx.send(content="A pasta has been spawned recently. Please wait.")
            
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
            start = time.time()
            if(self.bubblewrap_command_ran == True):
                if((start - self.last_bubblewrap_command_ran) > 30 ):
                    self.bubblewrap_command_ran = False

            if(self.bubblewrap_command_ran == False):
                self.bubblewrap_command_ran = True
                self.last_bubblewrap_command_ran = start
                embed = discord.Embed(title="Free Bubble Wrap", description="")
                embed.add_field(name="", value=f"||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop||\n||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop||\n||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop||\n||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop||\n||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop||\n||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop||\n||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop||\n||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop||\n||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop||\n||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop||\n||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop||")
                await ctx.send(embed=embed)
            else:
                await ctx.send(content="We have apparently ran out of bubble wraps! Please kindly wait for a moment until we get another one.")

async def setup(bot: commands.Bot):
    await bot.add_cog(Fun(bot))

async def teardown(bot):
    print("Extension unloaded!")