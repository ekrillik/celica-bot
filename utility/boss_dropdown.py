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

    def __init__(self, user: discord.User | discord.Member, timeout: float = 60.0, boss = {}, ppc_mode = "exppc", post_luna = False) -> None:
        super().__init__(timeout=timeout)
        self.user = user
        self.boss_name = boss['name']
        self.boss_thumbnail = boss['thumbnail']
        self.boss_weakness_name = boss['weakness_name']
        self.boss_start_time = boss['start_time']
        if 'outlier' in boss:
            self.outlier_mode = boss['outlier']
        else:
            self.outlier_mode = False

        if post_luna:
            options = ["Knight", "Chaos", "Hell"]
        else:
            options = ["Test", "Elite", "Knight", "Chaos", "Hell"]
        
        if ppc_mode == 'advanced' and 'advanced' in boss:
            self.ppc_mode = 'Advanced'
            self.boss_stats = boss['advanced']
        elif ppc_mode == 'onslaught' and 'onslaught' in boss:
            self.ppc_mode = 'Onslaught'
            self.boss_stats = boss['onslaught']
        else:
            self.ppc_mode = 'EXPPC'
            self.boss_stats = boss['exppc']
        
        self.menu = discord.ui.Select[BossDropdownView](
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
            embed = self.embedconf.create_boss_embed(self.boss_name, self.boss_thumbnail, self.boss_weakness_name, self.ppc_mode, 'Test', self.boss_start_time, self.boss_stats['test'], self.outlier_mode)
        elif(self.menu.values[0] == "Elite"):
            embed = self.embedconf.create_boss_embed(self.boss_name, self.boss_thumbnail, self.boss_weakness_name, self.ppc_mode, 'Elite', self.boss_start_time, self.boss_stats['elite'], self.outlier_mode)
        elif(self.menu.values[0] == "Knight"):
            embed = self.embedconf.create_boss_embed(self.boss_name, self.boss_thumbnail, self.boss_weakness_name, self.ppc_mode, 'Knight', self.boss_start_time, self.boss_stats['knight'], self.outlier_mode)
        elif(self.menu.values[0] == "Chaos"):
            embed = self.embedconf.create_boss_embed(self.boss_name, self.boss_thumbnail, self.boss_weakness_name, self.ppc_mode, 'Chaos', self.boss_start_time, self.boss_stats['chaos'], self.outlier_mode)
        elif(self.menu.values[0] == "Hell"):
            embed = self.embedconf.create_boss_embed(self.boss_name, self.boss_thumbnail, self.boss_weakness_name, self.ppc_mode, 'Hell', self.boss_start_time, self.boss_stats['hell'], self.outlier_mode)

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