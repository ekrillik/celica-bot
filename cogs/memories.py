import json
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


async def setup(bot: commands.Bot):
    await bot.add_cog(Memories(bot))
