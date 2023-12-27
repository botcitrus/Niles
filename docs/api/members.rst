.. SPDX-License-Identifier: MIT

.. currentmodule:: niles

Members
=======

This sections documents everything related to guild members.

Discord Models
---------------

Member
~~~~~~

.. attributetable:: Member

.. autoclass:: Member()
    :members:
    :inherited-members:
    :exclude-members: history, typing

    .. automethod:: history
        :async-for:

    .. automethod:: typing
        :async-with:

RawGuildMemberRemoveEvent
~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: RawGuildMemberRemoveEvent

.. autoclass:: RawGuildMemberRemoveEvent()
    :members:

Events
------

- :func:`on_member_join(member) <niles.on_member_join>`
- :func:`on_member_remove(member) <niles.on_member_remove>`
- :func:`on_member_update(before, after) <niles.on_member_update>`
- :func:`on_raw_member_remove(member) <niles.on_raw_member_remove>`
- :func:`on_raw_member_update(member) <niles.on_raw_member_update>`
- :func:`on_member_ban(guild, user) <niles.on_member_ban>`
- :func:`on_member_unban(guild, user) <niles.on_member_unban>`
- :func:`on_presence_update(before, after) <niles.on_presence_update>`
- :func:`on_user_update(before, after) <niles.on_user_update>`
