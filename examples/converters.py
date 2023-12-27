# SPDX-License-Identifier: MIT

"""An example showcasing different builtin converter types."""

# A list of all available converter types can be found at
# https://docs.niles.dev/en/stable/ext/commands/commands.html#discord-converters.

import os
import typing

import niles
from niles.ext import commands

intents = niles.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(commands.when_mentioned_or("!"), intents=intents)


@bot.command()
async def userinfo(ctx: commands.Context, user: niles.User):
    # In the command signature above, you can see that the `user`
    # parameter is typehinted to `niles.User`. This means that
    # during command invocation, we will attempt to convert
    # the value passed as `user` to a `niles.User` instance.

    # The documentation notes what can be converted, in the case of `niles.User`
    # you pass an ID, mention or username (discrim optional)
    # e.g. 941192261427920937, @Snakebot or Snakebot#5949

    # If the conversion is successful, we will have a full `niles.User` instance
    # and can do the following:
    await ctx.send(f"User found: {user.id} -- {user.name}\n{user.display_avatar.url}")


@userinfo.error
async def userinfo_error(ctx: commands.Context, error: commands.CommandError):
    # If the conversion above fails for any reason, it will raise `commands.UserNotFound`
    # so we handle this in this error handler:
    if isinstance(error, commands.UserNotFound):
        return await ctx.send("Couldn't find that user.")


@bot.command()
async def ignore(ctx: commands.Context, target: typing.Union[niles.Member, niles.TextChannel]):
    # This command signature utilises the `typing.Union` typehint.
    # The `commands` framework attempts a conversion of each type in this Union *in order*.
    # So, it will attempt to convert whatever is passed to `target` to a `niles.Member` instance.
    # If that fails, it will attempt to convert it to a `niles.TextChannel` instance.
    # See: https://docs.niles.dev/en/stable/ext/commands/commands.html#typing-union

    # NOTE: If a Union typehint converter fails it will raise `commands.BadUnionArgument`
    # instead of `commands.BadArgument`.

    # To check the resulting type, `isinstance` is used
    if isinstance(target, niles.Member):
        await ctx.send(f"Member found: {target.mention}, adding them to the ignore list.")
    else:
        await ctx.send(f"Channel found: {target.mention}, adding it to the ignore list.")


# Built-in type converters.
@bot.command()
async def multiply(ctx: commands.Context, number: int, maybe: bool):
    # We want an `int` and a `bool` parameter here.
    # `bool` is a slightly special case, as shown here:
    # See: https://docs.niles.dev/en/stable/ext/commands/commands.html#bool

    if maybe is True:
        return await ctx.send(str(number * 2))

    await ctx.send(str(number * 5))


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})\n------")


if __name__ == "__main__":
    bot.run(os.getenv("BOT_TOKEN"))
