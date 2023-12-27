# SPDX-License-Identifier: MIT

import re

from setuptools import setup

packages = [
    "niles",
    "niles.bin",
    "niles.types",
    "niles.ui",
    "niles.ui.select",
    "niles.webhook",
    "niles.interactions",
    "niles.ext.commands",
    "niles.ext.tasks",
    "niles.ext.mypy_plugin",
]

setup(
    version=0.0.1,
    packages=packages,
    include_package_data=True,
)
