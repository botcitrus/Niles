.. SPDX-License-Identifier: MIT

.. currentmodule:: niles

Emoji
=====

This section documents everything related to Discord
:ddocs:`emoji <resources/emoji>`.

Discord Models
---------------

Emoji
~~~~~

.. attributetable:: Emoji

.. autoclass:: Emoji()
    :members:
    :inherited-members:

Data Classes
-------------

PartialEmoji
~~~~~~~~~~~~

.. attributetable:: PartialEmoji

.. autoclass:: PartialEmoji
    :members:
    :inherited-members:

Events
------

- :func:`on_guild_emojis_update(guild, before, after) <niles.on_guild_emojis_update>`
