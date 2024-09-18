import discord
import os
import json
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from utility.embedconfig import EmbedClass
from utility.help_dropdown import HelpView
from utility.general_view import GeneralView

class Help(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

    @commands.Cog.listener()
    async def on_ready(self):
        print('Help loaded.')

    @commands.command()
    async def help(self, ctx: commands.Context, command = ""):
        if(command == ""):
            with open('data/help.json') as file:
                parsed_json = json.load(file)

            bot_related = parsed_json['bot_related']
            information = parsed_json['information']

            embed = discord.Embed(title="Celica's Help Menu", description="I'm an informational bot for the game **Punishing: Gray Raven**", color=discord.Color(0x2e6a80))
            embed.add_field(
                name="", 
                value=f"""
                    My prefix is: ?
                    Use the dropdown to view a list of commands by category.
                    Use `?help [command]` for more information on a specific command.
                """
            )
            embed.add_field(
                name="**Changelog**",
                value="```This is a new PGR bot with updated information, taking aspects of the Cogs bot made by Doomy. Please stay tuned for more updates.```",
                inline=False
            )
            view = HelpView(ctx.author, bot_related=bot_related, informational_commands=information)
            view.message = await ctx.send(embed=embed, view=view)
        else:
            with open('data/help.json') as file:
                parsed_json = json.load(file)

            view = GeneralView(ctx.author)

            command_help = parsed_json[command]
            if 'examples' not in command_help and 'aliases' not in command_help:
                embed = self.embedconf.help_commands_embed(title=command_help['syntax'], description=command_help['description'])
            elif 'examples' not in command_help:
                embed = self.embedconf.help_commands_embed(title=command_help['syntax'], aliases=command_help['aliases'], description=command_help['description'])
            elif 'aliases' not in command_help:
                embed = self.embedconf.help_commands_embed(title=command_help['syntax'], description=command_help['description'], examples=command_help['examples'])
            else:
                embed = self.embedconf.help_commands_embed(title=command_help['syntax'], aliases=command_help['aliases'], description=command_help['description'], examples=command_help['examples'])

            view.message = await ctx.send(embed=embed, view=view)


    @commands.command()
    async def links(self, ctx: commands.Context):
        embed = discord.Embed(
            title=f"Useful Links",
            description=f""
        )
        embed.add_field(name="Officials", value=f"[Website](https://pgr.kurogame.net/)\n[Youtube](https://www.youtube.com/@PunishingGrayRaven)\n[BiliBili](https://space.bilibili.com/382651856)")
        embed.add_field(name="Wikis", value=f"[Gray Ravens](https://grayravens.com/wiki/GRAY_RAVENS)\n[Bili Wiki](https://wiki.biligame.com/zspms/%E9%A6%96%E9%A1%B5)")
        embed.add_field(name="Competitive Info", value=f"[Huaxu](https://huaxu.app/)\n[Setsu's Harmo Spreadsheet](https://docs.google.com/spreadsheets/d/1t7TXDtfZdpHQy8SZAeIMpxcSi1pheSUVgDwkhicCw6s)")

        embed.add_field(name="Planning", value=f"[BC Planner](https://docs.google.com/spreadsheets/d/1nNauBXGcHv_7AepLWBLo4ykl3V_EhxpK)")

        embed.add_field(name="General Guides", value=f"[Zexous' Meta Spreadsheet](https://docs.google.com/spreadsheets/d/1SusxJ3tYwsBqY3dPwJ9BG2tDW0ox5GqVJgGZHYnAqa8)\n[Rexlent Beginner YT Playlist](https://www.youtube.com/watch?v=EHaKrXj643A&list=PLT669jfZO0z9OFd4fnfJxGc3Z71e-1FCg)")
        
        embed.add_field(name="Phantom Pain Cage", value=f"[SS Ultimate](https://docs.google.com/spreadsheets/d/16z8o9xw3NUhSAymJIRtsWyQsxqEndpgYS4OCb1GYyAQ)\n[SSS Ultimate](https://docs.google.com/spreadsheets/d/1p3-_Bqp4NEpqEVEFUqthxeVlvwu5uXzJSoHa8ZoN5yk)\n[S+ Ultimate](https://docs.google.com/spreadsheets/d/1YzOGbhTKaGTzfGbQJDdI6PSw8lXxcDpEQeeVLF4u2Dw)")

        embed.add_field(name="Warzone", value=f"[Advanced Warzone Tips](https://docs.google.com/document/d/1nJeLR5qIrq7SvueCGPDFz5KsMmYGVxUgqmxoRHZJ0GM)\n", inline=False)

        embed.add_field(name="Outdated Resources", value=f"[Story Reader](https://tf6ksijarp.github.io/)\n[Character 'Tier List by Doomy'](https://docs.google.com/spreadsheets/d/1nCmBq7NstZovPWs9cymAXNyakVXJ4lKvNGbVmtPbcUc)\n[Outdated Advanced PPC Spreadsheet](https://discord.com/channels/595893569609269251/663286717985456157/1283247685255696425)\n[Comprehensive Character Builds](https://docs.google.com/spreadsheets/d/1_NAHdVouSp2T6AwStpz9ZMLZ_ca5EzcuHde5obIlero)\n[Resource Calculator](https://docs.google.com/spreadsheets/d/1rfS6P1UOcZFj_ru2dqLzRkTE39Z0Phjbi5XDsOoNYRs)\n[Coatings Acquisition](https://docs.google.com/spreadsheets/d/1uIWrtp3mZEZgQseY788WHGp7_0mZBE8zSkpVOVCWtP8)")
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot))

async def teardown(bot):
    print("Extension unloaded!")