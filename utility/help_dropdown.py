from __future__ import annotations

import logging
import discord
import typing
import traceback
import json
from utility.embedconfig import EmbedClass

class HelpView(discord.ui.View):
    message: discord.Message | None = None
    interaction: discord.Interaction | None = None
    sep : int = 5
    current_page = 1

    def __init__(self, user: discord.User | discord.Member, timeout: float = 60.0, bot_related = [], informational_commands = []) -> None:
        super().__init__(timeout=timeout)
        self.user = user
        self.bot_related = bot_related
        self.informational_commands = informational_commands
        options = ["Main", "Bot Related", "Informational Commands"]
        self.menu = discord.ui.Select[HelpView](
            custom_id="persistent_menu",
            placeholder="Select a category",
            min_values=1,
            max_values=1,
            options=[discord.SelectOption(label=f"{i}") for i in options],
        )
        self.clear_button = discord.ui.Button(label="Delete", style=discord.ButtonStyle.red)
        self.menu.callback = self.callback
        self.clear_button.callback = self.deleteView
        self.add_item(self.menu)
        self.add_item(self.clear_button)
        self.embedconf = EmbedClass()

    async def callback(self, interaction: discord.Interaction) -> None:
        if(self.menu.values[0] == "Main"):
            embed = discord.Embed(title="Celica Help Menu", description="I'm an informational bot for the game **Punishing: Gray Raven**", color=discord.Color(0x2e6a80))
            embed.add_field(
                name="", 
                value=f"""
                    My prefix is: >
                    Use the dropdown to view a list of commands by category.
                    Use `>help [command]` for more information on a specific command.
                """
            )
            embed.add_field(
                name="**Changelog**",
                value="```This is a new PGR bot with updated information, taking aspects of the Cogs bot made by Doomy. Please stay tuned for more updates.```",
                inline=False
            )
        elif(self.menu.values[0] == "Bot Related"):
            embed = self.embedconf.helplist_embed(title="Celica Help", list=self.bot_related)
        elif(self.menu.values[0] == "Informational Commands"):
            embed = self.embedconf.helplist_embed(title="Informational Help", list=self.informational_commands)

        await interaction.response.edit_message(embed=embed, view=self)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user == self.user:
            return True
        await interaction.response.send_message(f"The command was initiated by {self.user.mention}", ephemeral=True)
        return False
    
    async def on_timeout(self) -> None:
        self.clear_items()
        await self.message.edit(view=self)

    async def deleteView(self, interaction: discord.Interaction) -> None:
        await self.message.delete()