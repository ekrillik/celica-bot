from __future__ import annotations

import logging
import discord
import typing
import traceback
import json
from utility.embedconfig import EmbedClass

class BossDropdownView(discord.ui.View):
    message: discord.Message | None = None
    interaction: discord.Interaction | None = None
    sep : int = 5
    current_page = 1

    def __init__(self, user: discord.User | discord.Member, timeout: float = 60.0, boss = {}, post_luna = False) -> None:
        super().__init__(timeout=timeout)
        self.user = user
        self.boss = boss
        if post_luna:
            options = ["Knight", "Chaos", "Hell"]
        else:
            options = ["Test", "Elite", "Knight", "Chaos", "Hell"]
        self.menu = discord.ui.Select[HelpView](
            custom_id="persistent_menu",
            placeholder="Select a difficulty",
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
        if(self.menu.values[0] == "Test"):
            ""
        elif(self.menu.values[0] == "Elite"):
            embed = self.embedconf.helplist_embed(title="Celica Help", list=self.bot_related)
        elif(self.menu.values[0] == "Knight"):
            embed = self.embedconf.helplist_embed(title="Informational Help", list=self.informational_commands)
        elif(self.menu.values[0] == "Chaos"):
            ""
        elif(self.menu.values[0] == "Hell"):
            ""

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