# SPDX-License-Identifier: MIT

import io
from base64 import b64decode

import niles
from niles.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot: commands.Bot = bot

    def _get_file(self, description: str) -> niles.File:
        # just a white 100x100 png
        data = b64decode(
            "iVBORw0KGgoAAAANSUhEUgAAAGQAAABkBAMAAACCzIhnAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAADUExURf///6fEG8gAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAcSURBVFjD7cEBDQAAAMKg909tDwcEAAAAAByoARPsAAFwJuooAAAAAElFTkSuQmCC"
        )
        return niles.File(io.BytesIO(data), "image.png", description=description)

    @commands.slash_command()
    async def attachment_desc(
        self, inter: niles.AppCmdInter[commands.Bot], desc: str = "test"
    ) -> None:
        """Send an attachment with the given description (or the default)

        Parameters
        ----------
        desc: The attachment description
        """
        await inter.response.send_message(file=self._get_file(desc))

    @commands.slash_command()
    async def attachment_desc_edit(
        self, inter: niles.AppCmdInter[commands.Bot], desc: str = "test"
    ) -> None:
        """Send a message with a button, which sends an attachment with the given description (or the default)

        Parameters
        ----------
        desc: The attachment description
        """
        button = niles.ui.Button(label="edit")
        button.callback = lambda interaction: interaction.response.edit_message(
            file=self._get_file(desc)
        )

        view = niles.ui.View()
        view.add_item(button)
        await inter.response.send_message(".", view=view)


def setup(bot) -> None:
    bot.add_cog(Misc(bot))
