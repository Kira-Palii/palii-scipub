import pytest

from scipub.domain.text import normalize_title, truncate_title


def test_normalize_title_strips_spaces_and_lowercases():
    assert normalize_title("  Deep   Learning  ") == "deep learning"


def test_normalize_title_empty_string():
    assert normalize_title("") == ""


def test_truncate_title_short_title_unchanged():
    assert truncate_title("abc", 10) == "abc"


def test_truncate_title_long_title_is_cut():
    assert truncate_title("abcdef", 4) == "abc…"


def test_truncate_title_rejects_invalid_limit():
    with pytest.raises(ValueError):
        truncate_title("abc", 0)
