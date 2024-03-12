MAX_HEADING_LEVEL = 6
HEADING_CHAR = "#"


class InvalidHeadingExeption(Exception):
    """Raised when string provided is not a valid heading"""


def is_heading(line: str) -> bool:
    """Determines if the given line is a heading"""
    heading = line.strip().split(" ", maxsplit=1)
    if len(heading) < 2:
        return False

    heading_level, heading_text = heading

    # make sure all characters in heading_level are hashtags
    if not all(char == HEADING_CHAR for char in heading_level):
        return False

    if len(heading_level) > MAX_HEADING_LEVEL:
        return False

    # make sure no hashtags exist elsewhere in the string
    if any(char == HEADING_CHAR for char in heading_text):
        return False

    return True


def get_heading_level(heading: str) -> int:
    """Gets the heading level of the given heading"""
    if not is_heading(heading):
        raise InvalidHeadingExeption(f"{heading} is not a valid heading")
    heading_level = heading.count(HEADING_CHAR)

    return heading_level
