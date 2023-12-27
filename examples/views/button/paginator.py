# SPDX-License-Identifier: MIT

"""A simple paginator example using views and buttons."""

import os
from typing import List

import niles
from niles.ext import commands


# Defines a simple paginator of buttons for the embed.
class Menu(niles.ui.View):
    def __init__(self, embeds: List[niles.Embed]):
        super().__init__(timeout=None)
        self.embeds = embeds
        self.index = 0

        # Sets the footer of the embeds with their respective page numbers.
        for i, embed in enumerate(self.embeds):
            embed.set_footer(text=f"Page {i + 1} of {len(self.embeds)}")

        self._update_state()

    def _update_state(self) -> None:
        self.first_page.disabled = self.prev_page.disabled = self.index == 0
        self.last_page.disabled = self.next_page.disabled = self.index == len(self.embeds) - 1

    @niles.ui.button(emoji="⏪", style=niles.ButtonStyle.blurple)
    async def first_page(self, button: niles.ui.Button, inter: niles.MessageInteraction):
        self.index = 0
        self._update_state()

        await inter.response.edit_message(embed=self.embeds[self.index], view=self)

    @niles.ui.button(emoji="◀", style=niles.ButtonStyle.secondary)
    async def prev_page(self, button: niles.ui.Button, inter: niles.MessageInteraction):
        self.index -= 1
        self._update_state()

        await inter.response.edit_message(embed=self.embeds[self.index], view=self)

    @niles.ui.button(emoji="🗑️", style=niles.ButtonStyle.red)
    async def remove(self, button: niles.ui.Button, inter: niles.MessageInteraction):
        await inter.response.edit_message(view=None)

    @niles.ui.button(emoji="▶", style=niles.ButtonStyle.secondary)
    async def next_page(self, button: niles.ui.Button, inter: niles.MessageInteraction):
        self.index += 1
        self._update_state()

        await inter.response.edit_message(embed=self.embeds[self.index], view=self)

    @niles.ui.button(emoji="⏩", style=niles.ButtonStyle.blurple)
    async def last_page(self, button: niles.ui.Button, inter: niles.MessageInteraction):
        self.index = len(self.embeds) - 1
        self._update_state()

        await inter.response.edit_message(embed=self.embeds[self.index], view=self)


bot = commands.Bot(command_prefix=commands.when_mentioned)


@bot.command()
async def paginator(ctx: commands.Context):
    # Creates the embeds as a list.
    embeds = [
        niles.Embed(
            title="Paginator example",
            description="This is the first embed.",
            colour=niles.Colour.random(),
        ),
        niles.Embed(
            title="Paginator example",
            description="This is the second embed.",
            colour=niles.Color.random(),
        ),
        niles.Embed(
            title="Paginator example",
            description="This is the third embed.",
            colour=niles.Color.random(),
        ),
    ]

    # Sends first embed with the buttons, it also passes the embeds list into the View class.
    await ctx.send(embed=embeds[0], view=Menu(embeds))


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})\n------")


if __name__ == "__main__":
    bot.run(os.getenv("BOT_TOKEN"))
