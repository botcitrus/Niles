.. SPDX-License-Identifier: MIT

.. currentmodule:: niles

Roles
=====

This section documents everything related to roles - a way of granting (or limiting) access to certain information/actions for a group of users.

Discord Models
---------------

Role
~~~~

.. attributetable:: Role

.. autoclass:: Role()
    :members:

RoleTags
~~~~~~~~

.. attributetable:: RoleTags

.. autoclass:: RoleTags()
    :members:

Data Classes
------------

RoleFlags
~~~~~~~~~

.. attributetable:: RoleFlags

.. autoclass:: RoleFlags()
    :members:

Events
------

- :func:`on_guild_role_create(role) <niles.on_guild_role_create>`
- :func:`on_guild_role_delete(role) <niles.on_guild_role_delete>`
- :func:`on_guild_role_update(before, after) <niles.on_guild_role_update>`
