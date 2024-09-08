from __future__ import annotations

import logging
import discord
import typing
import traceback

class GeneralView(discord.ui.View):
    message: discord.Message | None = None
    current_page = 0

    def __init__(self, user: discord.User | discord.Member, timeout: float = 60.0) -> None:
        super().__init__(timeout=timeout)
        self.user = user
        self.clear_button = discord.ui.Button(label="Delete", style=discord.ButtonStyle.red)
        self.clear_button.callback = self.deleteView
        self.add_item(self.clear_button)

    # checks for the view's interactions
    async def interaction_check(self, interaction: discord.Interaction) -> bool:
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
        
    async def deleteView(self, interaction: discord.Interaction) -> None:
        await self.message.delete()

    # error handler for the view
    async def on_error(
        self, interaction: discord.Interaction[discord.Client], error: Exception, item: discord.ui.Item[typing.Any]
    ) -> None:
        tb = "".join(traceback.format_exception(type(error), error, error.__traceback__))
        message = f"An error occurred while processing the interaction for {str(item)}:\n```py\n{tb}\n```"
        await interaction.response.send_message(message)