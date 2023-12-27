# SPDX-License-Identifier: MIT

import niles
from niles.enums import TextInputStyle
from niles.ext import commands


class MyModal(niles.ui.Modal):
    def __init__(self) -> None:
        components = [
            niles.ui.TextInput(
                label="Name",
                placeholder="The name of the tag",
                custom_id="name",
                style=TextInputStyle.short,
                max_length=50,
            ),
            niles.ui.TextInput(
                label="Description",
                placeholder="The description of the tag",
                custom_id="description",
                style=TextInputStyle.paragraph,
            ),
        ]
        super().__init__(title="Create Tag", custom_id="create_tag", components=components)

    async def callback(self, inter: niles.ModalInteraction[commands.Bot]) -> None:
        embed = niles.Embed(title="Tag Creation")
        for key, value in inter.text_values.items():
            embed.add_field(name=key.capitalize(), value=value, inline=False)
        await inter.response.send_message(embed=embed)


class Modals(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.slash_command()
    async def create_tag(self, inter: niles.AppCmdInter[commands.Bot]) -> None:
        """Sends a Modal to create a tag."""
        await inter.response.send_modal(modal=MyModal())

    @commands.slash_command()
    async def create_tag_low(self, inter: niles.AppCmdInter[commands.Bot]) -> None:
        """Sends a Modal to create a tag but with a low-level implementation."""
        await inter.response.send_modal(
            title="Create Tag",
            custom_id="create_tag2",
            components=[
                niles.ui.TextInput(
                    label="Name",
                    placeholder="The name of the tag",
                    custom_id="name",
                    style=TextInputStyle.short,
                    max_length=50,
                ),
                niles.ui.TextInput(
                    label="Description",
                    placeholder="The description of the tag",
                    custom_id="description",
                    style=TextInputStyle.paragraph,
                ),
            ],
        )

        modal_inter: niles.ModalInteraction = await self.bot.wait_for(
            "modal_submit",
            check=lambda i: i.custom_id == "create_tag2" and i.author.id == inter.author.id,  # type: ignore  # unknown parameter type
        )

        embed = niles.Embed(title="Tag Creation")
        for key, value in modal_inter.text_values.items():
            embed.add_field(name=key.capitalize(), value=value, inline=False)
        await modal_inter.response.send_message(embed=embed)


def setup(bot: commands.Bot) -> None:
    bot.add_cog(Modals(bot))
