# SPDX-License-Identifier: MIT

import pytest

import niles
from niles import message
from niles.utils import MISSING


@pytest.mark.parametrize(
    "emoji",
    [
        # single char
        "💯",
        "🔥",
        # with combining characters
        "👩‍👩‍👧‍👦",
    ],
)
def test_convert_emoji_reaction__standard(emoji) -> None:
    assert message.convert_emoji_reaction(emoji) == emoji


@pytest.mark.parametrize(
    "emoji",
    [
        "test:1234",
        ":test:1234",
        "<:test:1234>",
        "a:test:1234",
        "<a:test:1234>",
    ],
)
def test_convert_emoji_reaction__custom(emoji) -> None:
    assert message.convert_emoji_reaction(emoji) == "test:1234"


def _create_emoji(animated: bool) -> niles.Emoji:
    return niles.Emoji(
        guild=niles.Object(1),  # type: ignore
        state=MISSING,
        data={"name": "test", "id": 1234, "animated": animated},
    )


@pytest.mark.parametrize(
    ("emoji", "expected"),
    [
        (niles.PartialEmoji(name="🔥"), "🔥"),
        (_create_emoji(False), "test:1234"),
        (_create_emoji(True), "test:1234"),
        (_create_emoji(False)._to_partial(), "test:1234"),
        (_create_emoji(True)._to_partial(), "test:1234"),
    ],
)
def test_convert_emoji_reaction__object(emoji, expected) -> None:
    assert message.convert_emoji_reaction(emoji) == expected
