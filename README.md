<!-- SPDX-License-Identifier: MIT -->

niles
=======
A modern, easy to use, feature-rich, and async-ready API wrapper for Discord written in Python.

Key Features
------------

- Proper rate limit handling.
- Type-safety measures.
- [FastAPI](https://fastapi.tiangolo.com/)-like slash command syntax.

<sup>The syntax and structure of `discord.py 2.0` is preserved.</sup>

Installing
----------

**Python 3.8 or higher is required.**

To install the library without full voice support, you can just run the
following command:

``` sh
# Linux/macOS
python3 -m pip install -U niles

# Windows
py -3 -m pip install -U niles
```

Installing `niles` with full voice support requires you to replace `niles` here, with `niles[voice]`. To learn more about voice support (or installing the development version), please visit [this section of our guide](https://guide.niles.dev/prerequisites/installing-niles/).

(You can optionally install [PyNaCl](https://pypi.org/project/PyNaCl/) for voice support.)

Note that voice support on Linux requires installation of `libffi-dev` and `python-dev` packages, via your preferred package manager (e.g. `apt`, `dnf`, etc.) before running the following commands.

Quick Example
-------------

### Slash Commands Example

``` py
import niles
from niles.ext import commands

bot = commands.InteractionBot(test_guilds=[12345])

@bot.slash_command()
async def ping(inter):
    await inter.response.send_message("Pong!")

bot.run("BOT_TOKEN")
```

### Context Menus Example

``` py
import niles
from niles.ext import commands

bot = commands.InteractionBot(test_guilds=[12345])

@bot.user_command()
async def avatar(inter, user):
    embed = niles.Embed(title=str(user))
    embed.set_image(url=user.display_avatar.url)
    await inter.response.send_message(embed=embed)

bot.run("BOT_TOKEN")
```

### Prefix Commands Example

``` py
import niles
from niles.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run("BOT_TOKEN")
```

You can find more examples in the [examples directory](./examples).
