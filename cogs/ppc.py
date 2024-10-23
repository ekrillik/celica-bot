import discord
import json
from discord.ext import commands
from utility.embedconfig import EmbedClass
from utility.boss_dropdown import BossDropdownView

class Ppc(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

        with open('data/bosses.json') as file:
            self.bossdata = json.load(file)
            
    @commands.Cog.listener()
    async def on_ready(self):
        print('PPC loaded.')

    @commands.hybrid_command(pass_context=True, aliases=['PPC', 'ppc'], description="Accepts a difficulty and a time particular time in seconds to display a score for EX-PPC.")
    async def time(self, ctx: commands.Context, difficulty, time_str):
        max_seconds = 300
        difficulties = ["test", "elite", "knight", "chaos", "hell"]
        if difficulty not in difficulties:
            await ctx.send(content=f"{difficulty} is not a valid difficulty!")
            return

        power = difficulties.index(difficulty)
        try:
            time_sec = min(abs(int(time_str)), max_seconds)
        except ValueError:
            content = f"The provided time needs to be a valid number of seconds!"
            await ctx.send(content=content)
            return

        minutes, seconds = divmod(time_sec, 60)

        score = self.calculate_score(power, time_sec)

        embed = discord.Embed(
            title="",
            description=f"**{difficulty.title()} {minutes}:{seconds:02}**"
        )
        embed.add_field(name="", value=f"Final Score: {score}", inline=False)
        if time_sec == max_seconds:
            embed.add_field(name="", value=f"# You must have some skill issue if you even considered going over 5 minutes for EXPPC. :upside_down:", inline=False)
        await ctx.send(embed=embed)

    @staticmethod
    def calculate_score(power, time):
        factor = 2**power
        time = time+1
        score = 21000 * factor - round((74.875 * float(factor) * float(time)) - (0.25 * float(factor) * float(time) * (float(time)-1.0) / 2.0), 0)
        return int(score)

    @commands.hybrid_command(pass_context=True, description="Provides info on a particular boss")
    async def advanced(self, ctx: commands.Context, boss_name):
        self.boss = self.bossdata[boss_name]

        if 'advanced' in self.boss:
            view = BossDropdownView(ctx.author, boss=self.boss, ppc_mode='advanced', post_luna=False)
            embed = self.embedconf.create_boss_embed(self.boss['name'], self.boss['thumbnail'], self.boss['weakness_name'], 'Advanced', 'Test', self.boss['advanced']['test'])
            view.message = await ctx.send(embed=embed, view=view)
        else:
            await ctx.send(content="This boss does not exist or does not have a valid advanced PPC variant!")
        

    @commands.hybrid_command(pass_context=True, description="Provides info on a particular boss")
    async def exppc(self, ctx: commands.Context, boss_name):
        self.boss = self.bossdata[boss_name]

        if 'exppc' in self.boss:
            view = BossDropdownView(ctx.author, boss=self.boss, ppc_mode='exppc', post_luna=False)
            embed = self.embedconf.create_boss_embed(self.boss['name'], self.boss['thumbnail'], self.boss['weakness_name'], 'EXPPC', 'Test', self.boss['exppc']['test'])
            view.message = await ctx.send(embed=embed, view=view)
        else:
            await ctx.send(content="This boss does not exist or does not have a valid EXPPC variant!")


    @commands.hybrid_command(pass_context=True, description="Provides info on a particular boss")
    async def onslaught(self, ctx: commands.Context, boss_name):
        self.boss = self.bossdata[boss_name]

        if 'onslaught' in self.boss:
            view = BossDropdownView(ctx.author, boss=self.boss, ppc_mode='onslaught', post_luna=True)
            embed = self.embedconf.create_boss_embed(self.boss['name'], self.boss['thumbnail'], 'Dependent on weekly rotation', 'Onslaught', 'Onslaught', self.boss['onslaught'])
            view.message = await ctx.send(embed=embed, view=view)
        else:
            await ctx.send(content="This boss does not exist or does not have a valid Onslaught PPC variant!")

async def setup(bot: commands.Bot):
    await bot.add_cog(Ppc(bot))
