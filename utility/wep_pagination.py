from __future__ import annotations

import logging
import discord
import typing
import traceback
from utility.embedconfig import EmbedClass

class WeaponPageView(discord.ui.View):
    def __init__(self, user: discord.User | discord.Member, timeout: float = 60.0, weapon_box = [], theme = []) -> None:
        super().__init__(timeout=timeout)
        self.user = user
        self.embedconfig = EmbedClass()
        self.weapon_box = weapon_box
        self.theme = theme
        self.remove_item(self.two_star)
        self.remove_item(self.three_star)
        self.remove_item(self.four_star)
        self.remove_item(self.five_star)
        self.remove_item(self.six_star)

        for i in self.weapon_box:
            if(i['rarity'] == 2):
                self.add_item(self.two_star)
            elif(i['rarity'] == 3):
                self.add_item(self.three_star)
            elif(i['rarity'] == 4):
                self.add_item(self.four_star)
            elif(i['rarity'] == 5):
                self.add_item(self.five_star)
            else:
                self.add_item(self.six_star)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user == self.user:
            return True
        await interaction.response.send_message(f"The command was initiated by {self.user.mention}", ephemeral=True)
        return False

    async def on_timeout(self) -> None:
        self.clear_items()
        await self.message.edit(view=self)

    def create_embed(self, rarity):
        embed = {}

        for weapon in self.weapon_box:
            if weapon['rarity'] == rarity:
                embed = self.embedconfig.create_weapon_embed(weapon, user=self.theme[2], chibi_avatar=self.theme[1])
        return embed


    @discord.ui.button(label="2★", style=discord.ButtonStyle.gray)
    async def two_star(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.two_star.style = discord.ButtonStyle.blurple
        self.current_page="2★"
        self.update_buttons()
        embed = self.create_embed(2)
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="3★", style=discord.ButtonStyle.gray)
    async def three_star(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.three_star.style = discord.ButtonStyle.blurple
        self.current_page="3★"
        self.update_buttons()
        embed = self.create_embed(3)
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="4★", style=discord.ButtonStyle.gray)
    async def four_star(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.four_star.style = discord.ButtonStyle.blurple
        self.current_page="4★"
        self.update_buttons()
        embed = self.create_embed(4)
        await interaction.response.edit_message(embed=embed, view=self)
        
    @discord.ui.button(label="5★", style=discord.ButtonStyle.gray)
    async def five_star(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.five_star.style = discord.ButtonStyle.blurple
        self.current_page="5★"
        self.update_buttons()
        embed = self.create_embed(5)
        await interaction.response.edit_message(embed=embed, view=self)
        
    @discord.ui.button(label="6★", style=discord.ButtonStyle.gray)
    async def six_star(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.six_star.style = discord.ButtonStyle.blurple
        self.current_page="6★"
        self.update_buttons()
        embed = self.create_embed(6)
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="Delete", style=discord.ButtonStyle.red)
    async def deleteView(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self.message.delete()

    def update_buttons(self):
        match self.current_page:
            case "2★":
                self.two_star.style = discord.ButtonStyle.blurple
                self.three_star.style = discord.ButtonStyle.gray
                self.four_star.style = discord.ButtonStyle.gray
                self.five_star.style = discord.ButtonStyle.gray
                self.six_star.style = discord.ButtonStyle.gray
            case "3★":
                self.two_star.style = discord.ButtonStyle.gray
                self.three_star.style = discord.ButtonStyle.blurple
                self.four_star.style = discord.ButtonStyle.gray
                self.five_star.style = discord.ButtonStyle.gray
                self.six_star.style = discord.ButtonStyle.gray
            case "4★":
                self.two_star.style = discord.ButtonStyle.gray
                self.three_star.style = discord.ButtonStyle.gray
                self.four_star.style = discord.ButtonStyle.blurple
                self.five_star.style = discord.ButtonStyle.gray
                self.six_star.style = discord.ButtonStyle.gray
            case "5★":
                self.two_star.style = discord.ButtonStyle.gray
                self.three_star.style = discord.ButtonStyle.gray
                self.four_star.style = discord.ButtonStyle.gray
                self.five_star.style = discord.ButtonStyle.blurple
                self.six_star.style = discord.ButtonStyle.gray
            case "6★":
                self.two_star.style = discord.ButtonStyle.gray
                self.three_star.style = discord.ButtonStyle.gray
                self.four_star.style = discord.ButtonStyle.gray
                self.five_star.style = discord.ButtonStyle.gray
                self.six_star.style = discord.ButtonStyle.blurple

    async def on_error(
        self, interaction: discord.Interaction[discord.Client], error: Exception, item: discord.ui.Item[typing.Any]
    ) -> None:
        tb = "".join(traceback.format_exception(type(error), error, error.__traceback__))
        message = f"An error occurred while processing the interaction for {str(item)}:\n```py\n{tb}\n```"
        await interaction.response.send_message(message)