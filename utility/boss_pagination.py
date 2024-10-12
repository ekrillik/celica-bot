from __future__ import annotations

import logging
import discord
import typing
import traceback
from utility.embedconfig import EmbedClass

class MemorPageView(discord.ui.View):
    def __init__(self, user: discord.User | discord.Member, timeout: float = 60.0, boss = {}) -> None:
        super().__init__(timeout=timeout)
        self.user = user
        self.embedconfig = EmbedClass()
        self.boss = boss
        self.preshukra.disabled = True

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user == self.user:
            return True
        await interaction.response.send_message(f"The command was initiated by {self.user.mention}", ephemeral=True)
        return False

    async def on_timeout(self) -> None:
        self.clear_items()
        await self.message.edit(view=self)

    def create_embed(self, isAfter = False):
        embed = {}
        
        if isAfter:
            embed = self.embedconfig.create_memory_embed(self.memory, isRework=isAfter)
        else:
            embed = self.embedconfig.create_memory_embed(self.memory)
        return embed


    @discord.ui.button(label="Before Polaris Bond", style=discord.ButtonStyle.gray)
    async def preshukra(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.current_page="preshukra"
        self.update_buttons()
        embed = self.create_embed(isAfter=False)
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="After Polaris Bond", style=discord.ButtonStyle.blurple)
    async def postshukra(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.current_page="postshukra"
        self.update_buttons()
        embed = self.create_embed(isAfter=True)
        await interaction.response.edit_message(embed=embed, view=self)


    @discord.ui.button(label="Delete", style=discord.ButtonStyle.red)
    async def deleteView(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self.message.delete()

    def update_buttons(self):
        match self.current_page:
            case "preshukra":
                self.preshukra.style = discord.ButtonStyle.gray
                self.preshukra.disabled = True
                self.postshukra.style = discord.ButtonStyle.blurple
                self.postshukra.disabled = False
            case "postshukra":
                self.preshukra.style = discord.ButtonStyle.blurple
                self.preshukra.disabled = False
                self.postshukra.style = discord.ButtonStyle.gray
                self.postshukra.disabled = True


    async def on_error(
        self, interaction: discord.Interaction[discord.Client], error: Exception, item: discord.ui.Item[typing.Any]
    ) -> None:
        tb = "".join(traceback.format_exception(type(error), error, error.__traceback__))
        message = f"An error occurred while processing the interaction for {str(item)}:\n```py\n{tb}\n```"
        await interaction.response.send_message(message)