import discord
import time
import json
import random
from discord.ext import commands
from utility.embedconfig import EmbedClass

class Fun(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()
        self.disallowed_server_ids = [
            1285561465537040384, # Dud bot testing server
            595893569609269251, # PGR:O
            361043659107467264, # Personal Discord Server
        ]
        self.allowed_server_ids = [
            1280331315115327488, # Celica's Office
            1272185726699573358, # Nnin's Corner
            140529276175777792, # Nova's personal discord
            949981074153435157, # Doggostruct
            854380499643138118, # Fel's Server
            712404390207815761, # Shahrivar's Server
            431234590372265994, # Ew's Server
            887647011904557068, # Exaltair
            1180200696474251355
        ]
        self.pasta_command_ran = False
        self.bubblewrap_command_ran = False
        self.last_pasta_command_ran = 0.00
        self.last_bubblewrap_command_ran = 0.00

        with open('data/bricks.json') as file:
            self.bricks = json.load(file)

        with open('data/pastas.json') as file:
            self.pastas = json.load(file)

    # The following commands are restricted to specific servers/not usable within PGR:O

    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun loaded.')

    @commands.hybrid_command(description="Test command for restricting commands to specific servers.")
    async def fun(self, ctx: commands.Context) -> None:
        if ctx.guild.id in self.disallowed_server_ids:
            return

        embed = discord.Embed(title="This is a fun command.", description="This is a fun command description")
        await ctx.send(embed=embed)

    @commands.hybrid_command(description="Displays a random pasta. Has a 5s cd. Shares the cd timer with >brick")
    async def pasta(self, ctx: commands.Context) -> None:
        if ctx.guild.id not in self.allowed_server_ids:
            return

        start = time.time()
        if self.pasta_command_ran:
            if (start - self.last_pasta_command_ran) > 2:
                self.pasta_command_ran = False

        if not self.pasta_command_ran:
            self.pasta_command_ran = True
            self.last_pasta_command_ran = start

            copypasta = random.choice(self.pastas['copypastas'])
            await ctx.send(content=f"{copypasta}")
        else:
            await ctx.send(content="A pasta or brick has been spawned recently. Please wait.")

    @commands.hybrid_command(description="Lists all currently playing dalaos in a comprehensive list.")
    async def dalaos(self, ctx: commands.Context) -> None:
        if ctx.guild.id in self.disallowed_server_ids:
            return

        embed = discord.Embed(
            title=f"Dalaos",
            description=f""
        )
        embed.add_field(name="PPC", value=f"[Windbell](https://www.youtube.com/@10thwindbell)\n[Fel](https://www.youtube.com/@FelPGR)\n[Acaxi](https://www.youtube.com/@notacaxi)\n[GlobalGlory](https://m.youtube.com/@GlobalGlorypgr)\n[Yor Forger](https://m.youtube.com/@yorforgerpgr)")
        embed.add_field(name="Warzone", value=f"[sNazz](https://www.youtube.com/@sNazzkun)\n[Empress](https://www.youtube.com/@Oksohee)\n[Setsu](https://www.youtube.com/@Setsugekwa)")
        await ctx.send(embed=embed)

    @commands.hybrid_command(aliases=['bubble'], description="Spawns some bubble wrap. Has a 30s cd upon each spawn.")
    async def bubblewrap(self, ctx: commands.Context) -> None:
        if ctx.guild.id not in self.allowed_server_ids:
            return

        start = time.time()
        if self.bubblewrap_command_ran:
            if (start - self.last_bubblewrap_command_ran) > 30:
                self.bubblewrap_command_ran = False

        if self.bubblewrap_command_ran:
            await ctx.send(content="We have apparently ran out of bubble wraps! Please kindly wait for a moment until we get another one.")
            return

        self.bubblewrap_command_ran = True
        self.last_bubblewrap_command_ran = start
        embed = discord.Embed(title="Free Bubble Wrap", description="")
        bubble_wrap = "\n".join(["||pop|| " * 8] * 11)
        embed.add_field(name="", value=bubble_wrap)
        await ctx.send(embed=embed)

    @commands.hybrid_command(aliases=['brick'], description="Spawns some bubble wrap. Has a 5s cd. Shares the cd timer with >pasta")
    async def brickistan(self, ctx: commands.Context) -> None:
        if ctx.guild.id not in self.allowed_server_ids:
            return

        start = time.time()
        if self.pasta_command_ran:
            if (start - self.last_pasta_command_ran) > 2:
                self.pasta_command_ran = False

        if not self.pasta_command_ran:
            self.pasta_command_ran = True
            self.last_pasta_command_ran = start

            brick_image = random.choice(self.bricks['bricks'])
            embed = discord.Embed(title="", description="")
            embed.set_image(url=brick_image)
            await ctx.send(embed=embed)
        else:
            await ctx.send(content="A pasta or brick has been spawned recently. Please wait.")

async def setup(bot: commands.Bot):
    await bot.add_cog(Fun(bot))
