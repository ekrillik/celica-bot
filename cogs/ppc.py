import discord
import json
from discord.ext import commands
from utility.embedconfig import EmbedClass
from utility.boss_dropdown import BossDropdownView
from utility.fuzzymatch import fuzzmatch

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
        difficulties = ["knight", "chaos", "hell"]
        if difficulty not in difficulties:
            await ctx.send(content=f"{difficulty} is not a valid difficulty!")
            return

        power = difficulties.index(difficulty) + 2
        if difficulty == 'knight':
            hp_score_multiplier = difficulties.index(difficulty) + 1
        else:
            hp_score_multiplier = difficulties.index(difficulty)*2
        try:
            time_sec = min(abs(int(time_str)), max_seconds)
        except ValueError:
            content = f"The provided time needs to be a valid number of seconds!"
            await ctx.send(content=content)
            return

        minutes, seconds = divmod(time_sec, 60)

        score = self.calculate_score_v2(power, time_sec, hp_score_multiplier)

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

    @staticmethod
    def calculate_score_v2(power, time, multiplier):
        factor = 2**power
        time = time+1
        hp_score = 9000 * multiplier
        score = (21000 * factor - round((74.875 * float(factor) * float(time)) - (0.25 * float(factor) * float(time) * (float(time)-1.0) / 2.0), 0)) + hp_score
        return int(score)

    @commands.hybrid_command(pass_context=True, description="Provides info on a particular boss")
    async def advanced(self, ctx: commands.Context, *, boss_name):
        if boss_name.lower() in self.bossdata:
            self.boss = self.bossdata[boss_name.lower()]
        else:
            try:
                nickname = fuzzmatch(boss_name.lower(), "boss")
                self.boss = self.bossdata[nickname]
            except:
                await ctx.send(content="This boss does not exist. Please try again.")
        # elif fuzzmatch(boss_name.lower(), "boss") in self.bossdata:
        #     self.boss = self.bossdata[fuzzmatch(boss_name.lower(), "boss")]
        # else:
        #     await ctx.send(content="This boss does not exist. Please try again.")
        #     return

        if 'advanced' in self.boss:
            view = BossDropdownView(ctx.author, boss=self.boss, ppc_mode='advanced', post_luna=False)
            embed = self.embedconf.create_boss_embed(self.boss['name'], self.boss['thumbnail'], self.boss['weakness_name'], 'Advanced', 'Test', self.boss['start_time'], self.boss['advanced']['test'])
            view.message = await ctx.send(embed=embed, view=view)
        else:
            await ctx.send(content="This boss does not have a valid advanced PPC variant!")
        

    @commands.hybrid_command(pass_context=True, description="Provides info on a particular boss")
    async def exppc(self, ctx: commands.Context, *, boss_name):
        if boss_name.lower() in self.bossdata:
            self.boss = self.bossdata[boss_name.lower()]
        else:
            try:
                nickname = fuzzmatch(boss_name.lower(), "boss")
                print(nickname)
                self.boss = self.bossdata[nickname]
            except:
                await ctx.send(content="This boss does not exist. Please try again.")

        if 'exppc' in self.boss:
            if 'outlier' in self.boss:
                outlier = self.boss['outlier']
            else:
                outlier = False
            
            if 'post-oblivion' in self.boss and self.boss['post-oblivion'] is True:
                view = BossDropdownView(ctx.author, boss=self.boss, ppc_mode='exppc', post_luna=True)
                embed = self.embedconf.create_boss_embed(self.boss['name'], self.boss['thumbnail'], self.boss['weakness_name'], 'EXPPC', 'Knight', self.boss['start_time'], self.boss['exppc']['knight'], outlier)
            else:
                view = BossDropdownView(ctx.author, boss=self.boss, ppc_mode='exppc', post_luna=False)
                embed = self.embedconf.create_boss_embed(self.boss['name'], self.boss['thumbnail'], self.boss['weakness_name'], 'EXPPC', 'Test', self.boss['start_time'], self.boss['exppc']['test'], outlier)
            view.message = await ctx.send(embed=embed, view=view)
        else:
            await ctx.send(content="This boss does not have a valid EXPPC variant!")


    @commands.hybrid_command(pass_context=True, description="Provides info on a particular boss")
    async def onslaught(self, ctx: commands.Context, *, boss_name):
        if boss_name.lower() in self.bossdata:
            self.boss = self.bossdata[boss_name.lower()]
        elif fuzzmatch(boss_name.lower(), "boss") in self.bossdata:
            self.boss = self.bossdata[fuzzmatch(boss_name.lower(), "boss")]
        else:
            await ctx.send(content="This boss does not exist. Please try again.")
            return

        if 'onslaught' in self.boss:
            view = BossDropdownView(ctx.author, boss=self.boss, ppc_mode='onslaught', post_luna=True)
            embed = self.embedconf.create_boss_embed(self.boss['name'], self.boss['thumbnail'], 'Dependent on weekly rotation', 'Onslaught', 'Onslaught', self.boss['start_time'], self.boss['onslaught'])
            view.message = await ctx.send(embed=embed, view=view)
        else:
            await ctx.send(content="This boss does not have a valid Onslaught PPC variant!")

    @commands.hybrid_command(name="580k", aliases=['580', '58w'], pass_context=True, description="Provides the approximate times required to hit 580K in EXPPC.")
    async def achieveminscore(self, ctx: commands.Context):
        embed = discord.Embed(title="580K", description="Approximate time and score for each difficulty to reach 580k total score for an Ultimate Phantom Pain Cage boss.")
        embed.set_image(url="https://pgr-discord-bot.s3.ap-southeast-2.amazonaws.com/Infographics/580k.png")
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Ppc(bot))
