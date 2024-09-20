import json

import discord
from discord.ext import commands
from utility.embedconfig import EmbedClass
from utility.nickname_checker import check_nickname, abbreviation_checker

class Memories(commands.Cog):
    memories = {}

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

        with open('data/mems.json') as file:
            self.memories = json.load(file)

    @commands.Cog.listener()
    async def on_ready(self):
        print('Memory loaded.')

    def resolve_memory(self, memory_name):
        if memory_name in self.memories:
            return self.memories[memory_name]

        # Check if it was an abbreviated memory
        if (name := abbreviation_checker(memory_name)) in self.memories:
            return self.memories[name]

        # Check if it was a nickname
        if (name := check_nickname(memory_name, "memory")) in self.memories:
            return self.memories[name]

        # No memory exists with this name
        return None

    @commands.command(aliases=["mem", "memo"])
    async def memory(self, ctx: commands.Context, *args) -> None:
        memory_name = " ".join(args)

        memory = self.resolve_memory(memory_name)
        if memory is None:
            await ctx.send(content="This memory does not exist. Please try again.")
            return

        embed = self.embedconf.create_memory_embed(memory)
        await ctx.send(embed=embed)

    @commands.command(aliases=['mm', 'min'])
    async def minmax(self, ctx: commands.Context, *args):
        names = " ".join(args).split(",")
        memories = [self.resolve_memory(s.strip()) for s in names]
        if len(memories) != 2 or None in memories:
            await ctx.send(content="Either one of these memories are not valid! Please enter 2 valid memories to be compared.")
            return

        top_mem, bot_mem = sorted(memories, key=lambda x: x['atk'])

        embed = discord.Embed(
            title="Minmax",
            description="",
            color=discord.Color(value=0xc3d8fa)
        )

        embed.add_field(
            name=f"{top_mem['name']} goes Top",
            value=f"""
                `ATK  : {top_mem['atk']}   `
                `DEF  : {top_mem['def']}   `
                `CRIT : {top_mem['crit']}    `
                `HP   : {top_mem['hp']}  `
                """)

        embed.add_field(
            name=f"{bot_mem['name']} goes Bottom",
            value=f"""
                `ATK : {bot_mem['atk']}   `
                `DEF : {bot_mem['def']}   `
                `CRIT: {bot_mem['crit']}    `
                `HP  : {bot_mem['hp']}  `
                """)

        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Memories(bot))
