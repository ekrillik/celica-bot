from __future__ import annotations

import logging
import discord
import typing
import traceback
from utility.embedconfig import EmbedClass

class SkillsView(discord.ui.View):
    message: discord.Message | None = None
    current_page = 0

    def __init__(self, user: discord.User | discord.Member, timeout: float = 60.0, skills = {}) -> None:
        super().__init__(timeout=timeout)
        if 'leap' in skills:
            options = ["Basic Attack", "Red Orb", "Blue Orb", "Yellow Orb", "Core Passive", "Signature/Ultimate", "QTE", "Leader Passive", "Class Passive", "SS", "SSS", "S+", "Leap"]
        else:
            options = ["Basic Attack", "Red Orb", "Blue Orb", "Yellow Orb", "Core Passive", "Signature/Ultimate", "QTE", "Leader Passive", "Class Passive", "SS", "SSS", "S+"]
        
        self.user = user
        self.skills = skills
        self.embedconf = EmbedClass()

        self.menu = discord.ui.Select[SkillsView](
            custom_id="menu",
            placeholder="Select a skill",
            min_values=1,
            max_values=1,
            options=[discord.SelectOption(label=f"{skill}") for skill in options],
        )
        self.first = discord.ui.Button(label="|<", style=discord.ButtonStyle.green)
        self.prev = discord.ui.Button(label="<", style=discord.ButtonStyle.blurple)
        self.next = discord.ui.Button(label=">", style=discord.ButtonStyle.blurple)
        self.last = discord.ui.Button(label=">|", style=discord.ButtonStyle.green)
        self.clear_button = discord.ui.Button(label="Delete", style=discord.ButtonStyle.red)
        self.menu.callback = self.callback
        self.first.callback = self.first_callback
        self.prev.callback = self.prev_callback
        self.next.callback = self.next_callback
        self.last.callback = self.last_callback
        self.clear_button.callback = self.deleteView

        self.skill_type = "Basic Attack"
        self.skill = self.skills['basic_attack']
        self.skill_len = len(self.skills['basic_attack'])
        self.add_item(self.menu)
        
        print(self.current_page)
        if(self.skill_len > 1):
            self.add_item(self.first)
            self.add_item(self.prev)
            self.add_item(self.next)
            self.add_item(self.last)
            self.update_buttons()
        self.add_item(self.clear_button)
        
    def spawn_items(self):
        self.clear_items()   
        self.add_item(self.menu)
        
        if(self.skill_len > 1):
            self.add_item(self.first)
            self.add_item(self.prev)
            self.add_item(self.next)
            self.add_item(self.last)
            self.update_buttons()

        self.add_item(self.clear_button)
        embed = self.embedconf.skillsEmbed(self.skill, self.skill_type, self.current_page)
        return embed
        
    async def callback(self, interaction: discord.Interaction) -> None:
        self.current_page = 0
        match self.menu.values[0]:
            # Done
            case "Basic Attack":
                self.skill_type = "Basic Attack"
                self.skill = self.skills['basic_attack']
                self.skill_len = len(self.skills['basic_attack'])
                embed = self.spawn_items()
            # Done         
            case "Red Orb":
                self.skill_type = "Red Orb"
                self.skill = self.skills['red_orb']
                self.skill_len = len(self.skills['red_orb'])
                embed = self.spawn_items()              
            # Done
            case "Blue Orb":
                self.skill_type = "Blue Orb"
                self.skill = self.skills['blue_orb']
                self.skill_len = len(self.skills['blue_orb'])
                embed = self.spawn_items()
            # Done
            case "Yellow Orb":
                self.skill_type = "Yellow Orb"
                self.skill = self.skills['yellow_orb']
                self.skill_len = len(self.skills['yellow_orb'])
                embed = self.spawn_items()
            case "Core Passive":
                self.skill_type = "Core Passive"
                self.skill = self.skills['core_passive']
                self.skill_len = len(self.skill['skills'])
                embed = self.spawn_items()
            # Done
            case "Signature/Ultimate":
                self.skill_type = "Signature/Ultimate"
                self.skill = self.skills['signature']
                self.skill_len = len(self.skill['skills'])
                embed = self.spawn_items()
            # Done
            case "QTE":
                print(self.current_page)
                self.skill_type = "QTE"
                self.skill = self.skills['qte']
                self.skill_len = 0
                print(self.skill_len)
                embed = self.spawn_items()
            # Done
            case "Leader Passive":
                print(self.current_page)
                self.skill_type = "Leader Passive"
                self.skill = self.skills['leader']
                self.skill_len = 0
                embed = self.spawn_items()
            # Done
            case "Class Passive":
                print(self.current_page)
                self.skill_type = "Class Passive"
                self.skill = self.skills['class']
                self.skill_len = 0
                embed = self.spawn_items()
            # Done
            case "SS":
                print(self.current_page)
                self.skill_type = "SS"
                self.skill = self.skills['ss_rank']
                self.skill_len = 0
                embed = self.spawn_items()
            # Done
            case "SSS":
                print(self.current_page)
                self.skill_type = "SSS"
                self.skill = self.skills['sss_rank']
                self.skill_len = 0
                embed = self.spawn_items()
            # Done
            case "S+":
                print(self.current_page)
                self.skill_type = "S+"
                self.skill = self.skills['s+_rank']
                self.skill_len = 0
                embed = self.spawn_items()
            case "Leap":
                print(self.current_page)
                self.skill_type = "Leap"
                self.skill = self.skills['leap']
                self.skill_len = len(self.skill)
                embed = self.spawn_items()
        
        # embed = self.embedconf.create_build_embed(self.build, self.menu.values[0])
        await interaction.response.edit_message(embed=embed, view=self)

    # checks for the view's interactions
    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        
        # view: PaginationView = self.view

        # print(interaction)
        if interaction.user == self.user:
            content = "Test"
            # await self.update_message(self.data[:self.sep])
            # await interaction.response.edit_message(content=content, view=view)
            return True
        # else send a message and return False
        await interaction.response.send_message(f"The command was initiated by {self.user.mention}", ephemeral=True)
        return False
    
    # do stuff on timeout
    async def on_timeout(self) -> None:
        self.clear_items()
        await self.message.edit(view=self)

    async def first_callback(self, interaction: discord.Interaction) -> None:
        self.current_page=0
        print(self.current_page)
        # print(self.skill)
        self.embed = self.embedconf.skillsEmbed(self.skill, self.skill_type, cur_page=self.current_page)
        self.update_buttons()
        await interaction.response.edit_message(embed=self.embed, view=self)

    async def prev_callback(self, interaction: discord.Interaction) -> None:
        self.current_page-=1
        print(self.current_page)
        # print(self.skill)
        self.embed = self.embedconf.skillsEmbed(self.skill, self.skill_type, cur_page=self.current_page)
        self.update_buttons()
        await interaction.response.edit_message(embed=self.embed, view=self)
        
    async def next_callback(self, interaction: discord.Interaction) -> None:
        self.current_page+=1
        print(self.current_page)
        # print(self.skill)
        self.embed = self.embedconf.skillsEmbed(self.skill, self.skill_type, cur_page=self.current_page)
        self.update_buttons()
        await interaction.response.edit_message(embed=self.embed, view=self)
        
    async def last_callback(self, interaction: discord.Interaction) -> None:
        self.current_page = int(self.skill_len) + 1
        print(self.current_page)
        # print(self.skill)
        self.embed = self.embedconf.skillsEmbed(self.skill, self.skill_type, cur_page=self.current_page)
        self.update_buttons()
        await interaction.response.edit_message(embed=self.embed, view=self)
        
    async def deleteView(self, interaction: discord.Interaction) -> None:
        await self.message.delete()

    def update_buttons(self):
        if self.current_page == 0:
            self.first.disabled = True
            self.prev.disabled = True
            self.first.style = discord.ButtonStyle.gray
            self.prev.style = discord.ButtonStyle.gray
        else:
            self.first.disabled = False
            self.prev.disabled = False
            self.first.style = discord.ButtonStyle.green
            self.prev.style = discord.ButtonStyle.primary

        if self.current_page == int(self.skill_len) - 1:
            self.next.disabled = True
            self.last.disabled = True
            self.last.style = discord.ButtonStyle.gray
            self.next.style = discord.ButtonStyle.gray
        else:
            self.next.disabled = False
            self.last.disabled = False
            self.last.style = discord.ButtonStyle.green
            self.next.style = discord.ButtonStyle.primary

    # error handler for the view
    async def on_error(
        self, interaction: discord.Interaction[discord.Client], error: Exception, item: discord.ui.Item[typing.Any]
    ) -> None:
        tb = "".join(traceback.format_exception(type(error), error, error.__traceback__))
        message = f"An error occurred while processing the interaction for {str(item)}:\n```py\n{tb}\n```"
        await interaction.response.send_message(message)