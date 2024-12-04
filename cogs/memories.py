import json
from typing import List

import discord
from discord import app_commands
from discord.ext import commands
from utility.embedconfig import EmbedClass
from utility.nickname_checker import check_nickname, abbreviation_checker
from utility.fuzzymatch import fuzzmatch
from utility.mem_pagination import MemorPageView

def minmax(first, second) -> discord.Embed:
    top_mem, bot_mem = sorted([first, second], key=lambda x: x['atk'])

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

    return embed


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
        name = fuzzmatch(memory_name)
        if name == "":
            name = memory_name
        if (name := check_nickname(name, "memory")) in self.memories:
            return self.memories[name]

        # No memory exists with this name
        return None

    async def memory_autocomplete(self, interaction: discord.Interaction, current: str) -> List[app_commands.Choice[str]]:
        return [
            app_commands.Choice(name=memory_name, value=memory_name)
            for memory_name in self.memories.keys()
            if current.lower() in memory_name.lower()
        ][:25]

    @commands.hybrid_command(aliases=['Memory', 'Mem', 'MEM', 'mem', 'memo'], description="Displays stats and effects of a memory")
    @app_commands.autocomplete(name=memory_autocomplete)
    @app_commands.describe(name="Memory Name")
    async def memory(self, ctx: commands.Context, *, name) -> None:
        memory = self.resolve_memory(name.lower())
        if memory is None:
            await ctx.send(content="This memory does not exist. Please try again.")
            return
        
        view = MemorPageView(ctx.author, memory=memory)
        embed = self.embedconf.create_memory_embed(memory)
        await ctx.send(embed=embed)
        # if '4pc_alt' in memory:
        #     view.message = await ctx.send(view=view, embed=embed)
        # else:
        #     await ctx.send(embed=embed)

    @app_commands.command(name="minmax", description="Compares two memories and displays where they should be placed")
    @app_commands.autocomplete(first=memory_autocomplete, second=memory_autocomplete)
    async def minmax_slash(self, interaction: discord.Interaction, first: str, second: str):
        memory1 = self.resolve_memory(first)
        memory2 = self.resolve_memory(second)

        if memory1 is None or memory2 is None:
            await interaction.response.send_message(content="Either one of these memories are not valid! Please enter 2 valid memories to be compared.", ephemeral=True)
            return

        embed = minmax(memory1, memory2)
        await interaction.response.send_message(embed=embed)

    @commands.command(name="minmax", aliases=['MinMax', 'Minmax', 'mm', 'min'])
    async def minmax_chat(self, ctx: commands.Context, *args):
        names = " ".join(args).split(",")
        memories = [self.resolve_memory(s.strip().lower()) for s in names]
        if len(memories) != 2 or None in memories:
            await ctx.send(content="Either one of these memories are not valid! Please enter 2 valid memories to be compared.")
            return

        await ctx.send(embed=minmax(memories[0], memories[1]))


async def setup(bot: commands.Bot):
    await bot.add_cog(Memories(bot))
