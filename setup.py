# SPDX-License-Identifier: MIT

import re

from setuptools import setup

version = ""
with open("niles/__init__.py", encoding="utf-8") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)  # type: ignore

if not version:
    raise RuntimeError("version is not set")

if version.endswith(("a", "b", "rc")):
    # append version identifier based on commit count
    try:
        import subprocess  # noqa: TID251

        p = subprocess.Popen(
            ["git", "rev-list", "--count", "HEAD"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = p.communicate()
        if out:
            version += out.decode("utf-8").strip()
        p = subprocess.Popen(
            ["git", "rev-parse", "--short", "HEAD"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = p.communicate()
        if out:
            version += "+g" + out.decode("utf-8").strip()
    except Exception:
        pass

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
    version=version,
    packages=packages,
    include_package_data=True,
)
