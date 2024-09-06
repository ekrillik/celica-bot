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

    def __init__(self, user: discord.User | discord.Member, timeout: float = 60.0, data = [], build = {}) -> None:
        super().__init__(timeout=timeout)
        self.user = user
        self.data = data
        self.build = build
        self.menu = discord.ui.Select[DropdownView](
            custom_id="persistent_menu",
            placeholder="Select a build",
            min_values=1,
            max_values=1,
            options=[discord.SelectOption(label=f"{i}") for i in data],
        )
        self.clear_button = discord.ui.Button(label="Delete", style=discord.ButtonStyle.red)
        self.menu.callback = self.callback
        self.clear_button.callback = self.deleteView
        self.add_item(self.menu)
        self.add_item(self.clear_button)
        self.embedconf = EmbedClass()

    async def callback(self, interaction: discord.Interaction) -> None:
        embed = self.embedconf.create_build_embed(self.build, self.menu.values[0])
        await interaction.response.edit_message(embed=embed, view=self)

    
    def _disable_all(self) -> None:
        # disable all components
        # so components that can be disabled are buttons and select menus
        for item in self.children:
            if isinstance(item, discord.ui.Button):
                item.disabled = True

    # after disabling all components we need to edit the message with the new view
    # now when editing the message there are two scenarios:
    # 1. the view was never interacted with i.e in case of plain timeout here message attribute will come in handy
    # 2. the view was interacted with and the interaction was processed and we have the latest interaction stored in the interaction attribute
    async def _edit(self, **kwargs: typing.Any) -> None:
        if self.interaction is None:
            # if the view was never interacted with and the message attribute is not None, edit the message
            await self.message.edit(**kwargs)
        elif self.interaction is not None:
            try:
                # if not already responded to, respond to the interaction
                await self.interaction.response.edit_message(**kwargs)
            except discord.InteractionResponded:
                # if already responded to, edit the response
                await self.interaction.edit_original_response(**kwargs)

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
        self.clear_items()
        await interaction.response.edit_message(view=self)