# SPDX-License-Identifier: MIT

"""niles.webhook
~~~~~~~~~~~~~~

Webhook support

:copyright: (c) 2015-2021 Rapptz, 2021-present Niles Development
:license: MIT, see LICENSE for more details.

"""
from . import async_, sync
from .async_ import *
from .sync import *

__all__ = []
__all__.extend(async_.__all__)
__all__.extend(sync.__all__)
