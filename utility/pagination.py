from __future__ import annotations

import logging
import discord
import typing
import traceback
from utility.embedconfig import EmbedClass

class PaginationView(discord.ui.View):
    message: discord.Message | None = None
    current_page = 0

    def __init__(self, user: discord.User | discord.Member, timeout: float = 60.0, data = [], pagination_type = "", skill_type = "", theme = []) -> None:
        super().__init__(timeout=timeout)
        self.user = user
        self.data = data
        self.skill_type = skill_type
        # [colour, chibi_portrait, name]
        self.theme = theme
        if(self.skill_type == 'Core Passive' or self.skill_type == 'Signature/Ultimate'):
            self.max_len = len(self.data['skills'])
        else:
            self.max_len = len(self.data)
        self.embedconf = EmbedClass()
        self.pagination_type = pagination_type

        self.update_buttons()

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user == self.user:
            return True
        await interaction.response.send_message(f"The command was initiated by {self.user.mention}", ephemeral=True)
        return False


    async def on_timeout(self) -> None:
        try:
            self.clear_items()
            await self.message.edit(view=self)
        except discord.NotFound:
            # Message was deleted, nothing to do here
            pass


    @discord.ui.button(label="|<", style=discord.ButtonStyle.green)
    async def first_page_button(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.current_page=0
        if (self.pagination_type == "skills"):
            embed = self.embedconf.skillsEmbed(self.data, self.skill_type, cur_page=self.current_page, colour=self.theme[0], chibi_avatar=self.theme[1], user=self.theme[2], thumbnail=self.theme[3])
        elif(self.pagination_type == "credits"):
            embed = self.embedconf.credits_embed(self.data[0], cur_page=self.current_page, max_len=len(self.data))
        elif(self.pagination_type == "characters"):
            embed = self.embedconf.create_characterlist_embed(self.data[self.current_page])
        elif(self.pagination_type == "memories"):
            embed = self.embedconf.create_list_embed(name="Memories", type="memories", items = self.data[0], curpage=self.current_page+1, maxlistcount=len(self.data))
        elif(self.pagination_type == "nicknames"):
            embed = self.embedconf.create_list_embed(name="Nicknames", type="nicknames", character=self.data[0]['name'], items = self.data[0]['nicknames'], curpage=self.current_page+1, maxlistcount=len(self.data))
        self.update_buttons()
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="<", style=discord.ButtonStyle.blurple)
    async def prev_button(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.current_page-=1
        if (self.pagination_type == "skills"):
            embed = self.embedconf.skillsEmbed(self.data, self.skill_type, cur_page=self.current_page, colour=self.theme[0], chibi_avatar=self.theme[1], user=self.theme[2], thumbnail=self.theme[3])
        elif(self.pagination_type == "credits"):
            embed = self.embedconf.credits_embed(self.data[self.current_page], cur_page=self.current_page, max_len=len(self.data))
        elif(self.pagination_type == "characters"):
            embed = self.embedconf.create_characterlist_embed(self.data[self.current_page])
        elif(self.pagination_type == "memories"):
            embed = self.embedconf.create_list_embed(name="Memories", type="memories", items = self.data[self.current_page], curpage=self.current_page+1, maxlistcount=len(self.data))
        elif(self.pagination_type == "nicknames"):
            embed = self.embedconf.create_list_embed(name="Nicknames", type="nicknames", character=self.data[self.current_page]['name'], items = self.data[self.current_page]['nicknames'], curpage=self.current_page+1, maxlistcount=len(self.data))
        self.update_buttons()
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label=">", style=discord.ButtonStyle.blurple)
    async def next_button(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.current_page+=1
        if (self.pagination_type == "skills"):
            embed = self.embedconf.skillsEmbed(self.data, self.skill_type, cur_page=self.current_page, colour=self.theme[0], chibi_avatar=self.theme[1], user=self.theme[2], thumbnail=self.theme[3])
        elif(self.pagination_type == "credits"):
            embed = self.embedconf.credits_embed(self.data[self.current_page], cur_page=self.current_page, max_len=len(self.data))
        elif(self.pagination_type == "characters"):
            embed = self.embedconf.create_characterlist_embed(self.data[self.current_page])
        elif(self.pagination_type == "memories"):
            embed = self.embedconf.create_list_embed(name="Memories", type="memories", items = self.data[self.current_page], curpage=self.current_page+1, maxlistcount=len(self.data))
        elif(self.pagination_type == "nicknames"):
            embed = self.embedconf.create_list_embed(name="Nicknames", type="nicknames", character=self.data[self.current_page]['name'], items = self.data[self.current_page]['nicknames'], curpage=self.current_page+1, maxlistcount=len(self.data))
        self.update_buttons()
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label=">|", style=discord.ButtonStyle.green)
    async def last_page_button(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.current_page = self.max_len - 1
        if (self.pagination_type == "skills"):
            embed = self.embedconf.skillsEmbed(self.data, self.skill_type, cur_page=self.current_page, colour=self.theme[0], chibi_avatar=self.theme[1], user=self.theme[2], thumbnail=self.theme[3])
        elif(self.pagination_type == "credits"):
            embed = self.embedconf.credits_embed(self.data[self.current_page], cur_page=self.current_page, max_len=len(self.data))
        elif(self.pagination_type == "characters"):
            embed = self.embedconf.create_characterlist_embed(self.data[self.current_page])
        elif(self.pagination_type == "memories"):
            embed = self.embedconf.create_list_embed(name="Memories", type="memories", items = self.data[self.current_page], curpage=self.current_page+1, maxlistcount=len(self.data))
        elif(self.pagination_type == "nicknames"):
            embed = self.embedconf.create_list_embed(name="Nicknames for", type="nicknames", character=self.data[self.current_page]['name'], items = self.data[self.current_page]['nicknames'], curpage=self.current_page+1, maxlistcount=len(self.data))
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

        if self.current_page == self.max_len - 1:
            self.next_button.disabled = True
            self.last_page_button.disabled = True
            self.last_page_button.style = discord.ButtonStyle.gray
            self.next_button.style = discord.ButtonStyle.gray
        else:
            self.next_button.disabled = False
            self.last_page_button.disabled = False
            self.last_page_button.style = discord.ButtonStyle.green
            self.next_button.style = discord.ButtonStyle.primary

    # error handler for the view
    async def on_error(
        self, interaction: discord.Interaction[discord.Client], error: Exception, item: discord.ui.Item[typing.Any]
    ) -> None:
        tb = "".join(traceback.format_exception(type(error), error, error.__traceback__))
        message = f"An error occurred while processing the interaction for {str(item)}:\n```py\n{tb}\n```"
        await interaction.response.send_message(message)
