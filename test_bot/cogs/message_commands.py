# SPDX-License-Identifier: MIT

import niles
from niles.ext import commands


class MessageCommands(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot: commands.Bot = bot

    @commands.message_command(name="Reverse")
    async def reverse(self, inter: niles.MessageCommandInteraction[commands.Bot]) -> None:
        await inter.response.send_message(inter.target.content[::-1])


def setup(bot) -> None:
    bot.add_cog(MessageCommands(bot))
