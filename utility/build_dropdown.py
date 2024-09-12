from __future__ import annotations

import logging
import discord
import typing
import traceback
import json
from utility.embedconfig import EmbedClass

class DropdownView(discord.ui.View):
    message: discord.Message | None = None
    interaction: discord.Interaction | None = None
    sep : int = 5
    current_page = 1

    def __init__(self, user: discord.User | discord.Member, timeout: float = 60.0, data = [], build = {}, theme = []) -> None:
        super().__init__(timeout=timeout)
        self.user = user
        self.data = data
        self.build = build
        self.theme = theme
        self.menu = discord.ui.Select[DropdownView](
            custom_id="persistent_menu",
            placeholder="Select a build",
            min_values=1,
            max_values=1,
            options=[discord.SelectOption(label=f"{i}") for i in data],
        )
        self.clear_button = discord.ui.Button(label="Delete", style=discord.ButtonStyle.red)
        self.image_view = discord.ui.Button(label="Image View", style=discord.ButtonStyle.gray)
        self.text_view = discord.ui.Button(label="Text View", style=discord.ButtonStyle.gray)
        self.menu.callback = self.callback
        self.clear_button.callback = self.deleteView
        self.add_item(self.menu)
        self.add_item(self.clear_button)
        self.embedconf = EmbedClass()

    async def callback(self, interaction: discord.Interaction) -> None:
        embed = self.embedconf.create_build_embed(self.build, self.menu.values[0], colour=self.theme[0])
        await interaction.response.edit_message(embed=embed, view=self)

    # checks for the view's interactions
    async def interaction_check(self, interaction: discord.Interaction) -> bool:

        if interaction.user == self.user:
            content = "Test"
            return True
        # else send a message and return False
        await interaction.response.send_message(f"The command was initiated by {self.user.mention}", ephemeral=True)
        return False
    
    # do stuff on timeout
    async def on_timeout(self) -> None:
        self.clear_items()
        await self.message.edit(view=self)

    async def deleteView(self, interaction: discord.Interaction) -> None:
        await self.message.delete()