# SPDX-License-Identifier: MIT

"""An example showing how to edit view components, use timeouts, and disable views."""

import os

import niles
from niles.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned)


class MyView(niles.ui.View):
    message: niles.Message

    def __init__(self):
        # Set a timeout of 30 seconds, after which `on_timeout` will be called
        super().__init__(timeout=30.0)

    async def on_timeout(self):
        # Once the view times out, we disable the first button and remove the second button
        self.disable_button.disabled = True
        self.remove_item(self.remove_button)

        # make sure to update the message with the new buttons
        await self.message.edit(view=self)

    @niles.ui.button(label="Disable the view", style=niles.ButtonStyle.grey)
    async def disable_button(self, button: niles.ui.Button, inter: niles.MessageInteraction):
        # We disable every single component in this view
        for child in self.children:
            if isinstance(child, niles.ui.Button):
                child.disabled = True
        # make sure to update the message with the new buttons
        await inter.response.edit_message(view=self)

        # Prevents on_timeout from being triggered after the buttons are disabled
        self.stop()

    @niles.ui.button(label="Remove the view", style=niles.ButtonStyle.red)
    async def remove_button(self, button: niles.ui.Button, inter: niles.MessageInteraction):
        # view=None removes the view
        await inter.response.edit_message(view=None)

        # Prevents on_timeout from being triggered after the view is removed
        self.stop()


@bot.command()
async def view(ctx: commands.Context):
    # Create our view
    view = MyView()

    # Send a message with the view
    message = await ctx.send("These buttons will be disabled or removed!", view=view)

    # Assign the message to the view, so that we can use it in on_timeout to edit it
    view.message = message


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})\n------")


if __name__ == "__main__":
    bot.run(os.getenv("BOT_TOKEN"))
