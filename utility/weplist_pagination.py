from __future__ import annotations

import logging
import discord
import typing
import traceback
from utility.embedconfig import EmbedClass

class WeaponListPaginationView(discord.ui.View):
    message: discord.Message | None = None
    current_page = 0

    def __init__(self, user: discord.User | discord.Member, timeout: float = 60.0, data = []) -> None:
        super().__init__(timeout=timeout)
        self.user = user
        self.data = data
        self.weaponlistcount = len(self.data)
        self.embedconf = EmbedClass()
        self.update_buttons()

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user == self.user:
            return True
        await interaction.response.send_message(f"The command was initiated by {self.user.mention}", ephemeral=True)
        return False
    
    async def on_timeout(self) -> None:
        self.clear_items()
        await self.message.edit(view=self)

    def create_embed(self):
        embed = {} 
        embed = self.embedconf.create_list_embed(name=self.data[self.current_page]['name'], type="weapons", items=self.data[self.current_page]['list'], curpage=self.current_page + 1, maxlistcount=len(self.data))
        return embed

    @discord.ui.button(label="|<", style=discord.ButtonStyle.green)
    async def first_page_button(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.current_page=0
        embed = self.create_embed()
        self.update_buttons()
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="<", style=discord.ButtonStyle.blurple)
    async def prev_button(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.current_page-=1
        embed = self.create_embed()
        self.update_buttons()
        await interaction.response.edit_message(embed=embed, view=self)
        
    @discord.ui.button(label=">", style=discord.ButtonStyle.blurple)
    async def next_button(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.current_page+=1
        embed = self.create_embed()
        self.update_buttons()
        await interaction.response.edit_message(embed=embed, view=self)
        
    @discord.ui.button(label=">|", style=discord.ButtonStyle.green)
    async def last_page_button(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.current_page = int(len(self.data)) - 1
        embed = self.create_embed()
        self.update_buttons()
        await interaction.response.edit_message(embed=embed, view=self)
        
    @discord.ui.button(label="Delete", style=discord.ButtonStyle.red)
    async def deleteView(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self.message.delete()

    def update_buttons(self):
        if self.current_page == 0:
            self.first_page_button.disabled = True
            self.prev_button.disabled = True
            self.first_page_button.style = discord.ButtonStyle.gray
            self.prev_button.style = discord.ButtonStyle.gray
        else:
            self.first_page_button.disabled = False
            self.prev_button.disabled = False
            self.first_page_button.style = discord.ButtonStyle.green
            self.prev_button.style = discord.ButtonStyle.primary

        if self.current_page == len(self.data) - 1:
            self.next_button.disabled = True
            self.last_page_button.disabled = True
            self.last_page_button.style = discord.ButtonStyle.gray
            self.next_button.style = discord.ButtonStyle.gray
        else:
            self.next_button.disabled = False
            self.last_page_button.disabled = False
            self.last_page_button.style = discord.ButtonStyle.green
            self.next_button.style = discord.ButtonStyle.primary

    async def on_error(
        self, interaction: discord.Interaction[discord.Client], error: Exception, item: discord.ui.Item[typing.Any]
    ) -> None:
        tb = "".join(traceback.format_exception(type(error), error, error.__traceback__))
        message = f"An error occurred while processing the interaction for {str(item)}:\n```py\n{tb}\n```"
        await interaction.response.send_message(message)