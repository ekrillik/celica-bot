import json
import discord
import datetime
from discord.ext import commands
from utility.embedconfig import EmbedClass
from utility.pagination import PaginationView


class Beginners(commands.Cog):
    credits = {}

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('About loaded.')

    @commands.hybrid_command(aliases=['bi', 'banners', 'banner'], description="Displays information about PGR banners.")
    async def bannerinfo(self, ctx: commands.Context[commands.Bot]):
        embed = discord.Embed(title=f"PGR Banner Info")
        embed.add_field(name=f"1. Banners in Punishing: Gray Raven are broadly divided into 3 types", value=f"a. Character Banner\nb. Weapon Banner\nc. C.U.B. Banner")
        embed.add_field(name=f"2. Depending on gacha rates and pity for guaranteed S rank drop, there are 2 types Omniframe banners -", value=f"a. Banner with 60 pity — has a 0.5% rate for S rank Omniframe\nb. Banner with 80~100 pity — has a 1.5% rate for S rank Omniframe", inline=False)
        embed.add_field(
            name=f"Standard Banners", 
            value=f"- **Standard Omniframe Banner** - You can choose A rank characters in this banner while the S rank is random if you hit pity. This banner has 40 pity if you are a newbie and once you hit that pity the pity changes to 60. This banner also has a S rank Omniframe selector tied to it which is only once per account.\nNote - If an A rank Omniframe is on debut, the specific A rank Omniframe will have 100% droprate on this banner. Otherwise every A rank Omniframe is on 80% droprate. The S rank pool of this banner gets updated every 2 patches.")
        embed.add_field(
            name=f"Weapon Banners", 
            value=f"- **Standard Weapon Banner** - Weapon banner with 30 pity. Cannot select which Signature Weapon you want, so the Signature weapon (6 star) will be random once you hit the pity.\n- **Target Weapon Banner** - Weapon Banner with 30 pity. Signature weapon can be selected in this banner according to your choice. The selected signature weapon will have 80% droprate while the other 20% droprate is split inbetween the other 2 Signature weapons in the banner.")
        embed.add_field(
            name=f"Event Banners", 
            value=f"- **Event Themed Banner** - appears every S rank Omniframe patch. This banner has the debut S rank Omniframe at 100% droprate (you have to hit the pity and it's guaranteed to drop the debut character).\n- **Event Fate Themed Banner** - same as above but with 80~100 pity and 1.5% rate (mentioned above in point #2)\n- **Event Arrival Banner** - this one is basically the rerun banner of PGR. It sometimes comes with 2 or more Omniframes on rerun at 70% droprate (hit pity then it's 70/30).\n- **Event Fate Arrival Banner** — same as above but with 80~100 pity and 1.5% rate (mentioned above in point #2)\n- **Anniversary Banner** - Comes out every Anniversary. Any S rank can be selected and they'll have 100% droprate just like Themed banner. This too has a Fate banner option.")
        embed.add_field(
            name=f"Uniframe Banner", 
            value=f"- **Target Uniframe Banner** -  Uniframes are niche characters in PGR. They don't have much use. Their banner has a lower pity which is 10 pulls. They usually have 80% droprate but if an Uniframe is on debut they'll have 100% droprate.")
        embed.add_field(
            name=f"C.U.B. Banners", 
            value=f"- **Target C.U.B. Banner** - the pity is 20 pulls. If a certain C.U.B. is tied with the debut S rank Omniframe, then they'll have 100% droprate during that patch, after the patch is over they'll have 80% droprate when selected.")
        embed.add_field(
            name=f"Useful Information", 
            value=f"- A rank Omniframes are always guaranteed on 10 pulls in any Omniframe banner.\n- Arrival and Fate banners are generally not recommended to be pulled on as Fate banners take more Black cards than normal banner and Arrival banners have 70% droprate.\n- Uniframes must be avoided at all cost as they have no purpose anymore.\n- C.U.B.s are more or less for whales. F2Ps can ignore.")
        await ctx.send(embed=embed)

    @commands.hybrid_command(description="Displays a roadmap diagram by llyodius")
    async def roadmap(self, ctx: commands.Context[commands.Bot]):
        date = datetime.date.today()
        embed = discord.Embed(title=f"Current Roadmap (as of {date.strftime("%b %dth %Y")})")
        embed.set_image(url="https://pgr-discord-bot.s3.ap-southeast-2.amazonaws.com/Infographics/NEW_PGR_ROADMAP-3.png")
        await ctx.send(embed=embed)
        
    @commands.hybrid_command(aliases=['maxlevel', 'mlm'], description="Displays the required number of resources to max out a single frame.")
    async def maxlevelmats(self, ctx: commands.Context[commands.Bot]):
        embed = discord.Embed(title="")
        embed.set_image(url="https://pgr-discord-bot.s3.ap-southeast-2.amazonaws.com/Infographics/Picsart_23-12-07_15-11-35-788-2.png")
        await ctx.send(embed=embed)

    @commands.hybrid_command(aliases=['hg'], description="Displays the harmo guide infographic.")
    async def harmoguide(self, ctx: commands.Context[commands.Bot]):
        embed = discord.Embed(title="")
        embed.set_image(url="https://pgr-discord-bot.s3.ap-southeast-2.amazonaws.com/Infographics/HarmoGuideBRS.png")
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Beginners(bot))
