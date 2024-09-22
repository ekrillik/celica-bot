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

    def __init__(self, user: discord.User | discord.Member, timeout: float = 60.0, data = [], build = {}, theme = [], multibuild = False) -> None:
        super().__init__(timeout=timeout)
        self.user = user
        self.data = data
        self.build = build
        self.theme = theme
        self.multibuild = multibuild
        self.selection = data[0]
        self.menu = discord.ui.Select[DropdownView](
            custom_id="persistent_menu",
            placeholder="Select a build",
            min_values=1,
            max_values=1,
            options=[discord.SelectOption(label=f"{item['name']}", description=f"{item['memos']}") for item in data],
        )
        self.clear_button = discord.ui.Button(label="Delete", style=discord.ButtonStyle.red)
        self.image_view = discord.ui.Button(label="Image View", style=discord.ButtonStyle.gray)
        self.text_view = discord.ui.Button(label="Text View", style=discord.ButtonStyle.gray)
        self.menu.callback = self.callback
        self.clear_button.callback = self.deleteView
        self.image_view.callback = self.imageView
        self.text_view.callback = self.textView
        
        selection = self.choose_build(self.build['builds'], self.data[0]['name'])    
        if self.multibuild == True:
            self.add_item(self.menu)
        self.add_item(self.clear_button)
        if 'infographic' in selection:
            self.add_item(self.image_view)
        self.embedconf = EmbedClass()

    def choose_build(self, build_array, choice):
        for i in build_array:
            if choice == i['set_name']:
                build = i
        return build

    async def callback(self, interaction: discord.Interaction) -> None:
        if self.image_view in self.children:
            self.remove_item(self.image_view)
        if self.text_view in self.children:
            self.remove_item(self.text_view)
        self.selection = self.menu.values[0]
        selected_build = self.choose_build(self.build['builds'], self.selection)
        embed = self.embedconf.create_build_embed(self.build, self.menu.values[0], colour=self.theme[0], thumbnail_url=self.theme[3])
        if 'infographic' in selected_build:
            self.add_item(self.image_view)
        await interaction.response.edit_message(embed=embed, view=self)

    async def imageView(self, interaction: discord.Interaction) -> None:
        self.remove_item(self.image_view)
        self.add_item(self.text_view)
        embed = self.embedconf.create_build_embed(self.build, self.selection, imageView=True, colour=self.theme[0], thumbnail_url=self.theme[3])
        await interaction.response.edit_message(embed=embed, view=self)

    async def textView(self, interaction: discord.Interaction) -> None:
        self.remove_item(self.text_view)
        self.add_item(self.image_view)
        embed = self.embedconf.create_build_embed(self.build, self.selection, colour=self.theme[0], thumbnail_url=self.theme[3])
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