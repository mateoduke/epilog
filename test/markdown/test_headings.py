import pytest
from src.markdown.headings import is_heading, get_heading_level, InvalidHeadingExeption

# Test is_heading()


def test_is_heading_valid():
    heading_str = "### Hello World"
    is_valid = is_heading(heading_str)
    assert is_valid is True


def test_is_heading_only_hashtags():
    heading_str = "###"
    is_valid = is_heading(heading_str)
    assert is_valid is False


def test_is_heading_invalid_no_spaces():
    heading_str = "###Hello World"
    is_valid = is_heading(heading_str)
    assert is_valid is False


def test_is_heading_invalid_no_hashtags():
    heading_str = "Hello World"
    is_valid = is_heading(heading_str)
    assert is_valid is False


def test_is_heading_invalid_hashtag_usage_at_end():
    heading_str = "### Hello World #"
    is_valid = is_heading(heading_str)
    assert is_valid is False


def test_is_heading_invalid_hashtag_usage_in_middle():
    heading_str = "### Hello # World "
    is_valid = is_heading(heading_str)
    assert is_valid is False


def test_is_heading_invalid_too_many_hashtags():
    heading_str = "####### Hell World "
    is_valid = is_heading(heading_str)
    assert is_valid is False


# get_heading_level()


def test_get_heading_level():
    heading_str = "### Hello World"
    heading_level = get_heading_level(heading_str)
    assert heading_level == 3


def test_get_heading_level_invalid_raises_error():
    heading_str = "####### Hello # World"
    with pytest.raises(InvalidHeadingExeption):
        get_heading_level(heading_str)
