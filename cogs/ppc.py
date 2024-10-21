import discord
import json
from discord.ext import commands
from utility.embedconfig import EmbedClass
from utility.boss_dropdown import BossDropdownView

class Ppc(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

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

        embed = discord.Embed(
            title=f"{self.boss['name']}",
            description=f"",
            color=discord.Color(0xcd0000)
        )
        embed.set_thumbnail(url=self.boss['thumbnail'])
        embed.add_field(name=f"Weakness: {self.boss['weakness_name']}", value="", inline=False)
        embed.add_field(name=f"Zone Type: Ultimate/EXPPC", value="", inline=False)
        difficulty_stats = self.boss['exppc']['hell']
        embed.add_field(
            name=f"Difficulty: Hell", 
            value=f"HP: {difficulty_stats['hp']}\nSuper Armor: {difficulty_stats['super_armor']}\nExtra Damage Reduction: {difficulty_stats['edr']/100}%\nDefence: {difficulty_stats['def']}\nPhys Resist: {difficulty_stats['phys_res']/100}%\nFire Resist: {difficulty_stats['fire_res']/100}%\nLight Resist: {difficulty_stats['light_res']/100}%\nIce Resist: {difficulty_stats['ice_res']/100}%\nDark Resist: {difficulty_stats['dark_res']/100}%\n",
            inline=False
        )
        
        await ctx.send(embed=embed)

    @commands.hybrid_command(pass_context=True, description="Provides info on a particular boss")
    async def exppc(self, ctx: commands.Context, boss_name):
        self.boss = self.bossdata[boss_name]

        embed = discord.Embed(
            title=f"{self.boss['name']}",
            description=f"",
            color=discord.Color(0xcd0000)
        )
        embed.set_thumbnail(url=self.boss['thumbnail'])
        embed.add_field(name=f"Weakness: {self.boss['weakness_name']}", value="", inline=False)
        embed.add_field(name=f"Zone Type: Ultimate/EXPPC", value="", inline=False)
        difficulty_stats = self.boss['exppc']['hell']
        embed.add_field(
            name=f"Difficulty: Hell", 
            value=f"HP: {difficulty_stats['hp']}\nSuper Armor: {difficulty_stats['super_armor']}\nExtra Damage Reduction: {difficulty_stats['edr']/100}%\nDefence: {difficulty_stats['def']}\nPhys Resist: {difficulty_stats['phys_res']/100}%\nFire Resist: {difficulty_stats['fire_res']/100}%\nLight Resist: {difficulty_stats['light_res']/100}%\nIce Resist: {difficulty_stats['ice_res']/100}%\nDark Resist: {difficulty_stats['dark_res']/100}%\n",
            inline=False
        )
        
        await ctx.send(embed=embed)


    @commands.hybrid_command(pass_context=True, description="Provides info on a particular boss")
    async def onslaught(self, ctx: commands.Context, boss_name):
        self.boss = self.bossdata[boss_name]

        embed = discord.Embed(
            title=f"{self.boss['name']}",
            description=f"",
            color=discord.Color(0xcd0000)
        )
        embed.set_thumbnail(url=self.boss['thumbnail'])
        embed.add_field(name=f"Weakness: {self.boss['weakness_name']}", value="", inline=False)
        embed.add_field(name=f"Zone Type: Ultimate/EXPPC", value="", inline=False)
        difficulty_stats = self.boss['exppc']['hell']
        embed.add_field(
            name=f"Difficulty: Hell", 
            value=f"HP: {difficulty_stats['hp']}\nSuper Armor: {difficulty_stats['super_armor']}\nExtra Damage Reduction: {difficulty_stats['edr']/100}%\nDefence: {difficulty_stats['def']}\nPhys Resist: {difficulty_stats['phys_res']/100}%\nFire Resist: {difficulty_stats['fire_res']/100}%\nLight Resist: {difficulty_stats['light_res']/100}%\nIce Resist: {difficulty_stats['ice_res']/100}%\nDark Resist: {difficulty_stats['dark_res']/100}%\n",
            inline=False
        )
        
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Ppc(bot))
