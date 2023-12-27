# SPDX-License-Identifier: MIT

"""An example that uses webhooks to "impersonate" a specified user."""

import os

import niles
from niles.ext import commands

intents = niles.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=intents)


@bot.command()
@commands.has_permissions(
    administrator=True  # To make sure that not everyone can use this command.
)
async def userecho(ctx: commands.Context, member: niles.Member, *, content: str):
    # We don't want users to see who initiated the command, to make it more realistic :P
    await ctx.message.delete()

    # Fetch the channel's webhooks.
    channel = ctx.channel
    if not isinstance(channel, niles.TextChannel):
        return
    channel_webhooks = await channel.webhooks()

    # Check if the bot's webhook already exists in the channel.
    for webhook in channel_webhooks:
        # Check if the creator of the webhook is the same as the bot, and if the name is the same.
        if webhook.user == bot.user and webhook.name == "Bot Webhook":
            break
    else:
        # If the webhook does not exist, it will be created.
        webhook = await channel.create_webhook(name="Bot Webhook")

    # Finally, send the message via the webhook, using the user's display name and avatar.
    await webhook.send(
        content=content,
        username=member.display_name,
        avatar_url=member.display_avatar.url,
        allowed_mentions=niles.AllowedMentions.none(),
    )

    # Note: This method cannot impersonate the member's roles, since it works using webhooks.


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})\n------")


if __name__ == "__main__":
    bot.run(os.getenv("BOT_TOKEN"))
