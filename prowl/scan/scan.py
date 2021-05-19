"""Scan text and check if it contains a keyword
"""


def contains_keywords(text: str, filename: str) -> bool:
    """Check if text contains a keyword from a list of keywords

    :param text: text to scan
    :param filename: file to read from
    :return: true if match is found, false if no match
    """

    return any(map(text.__contains__, get_keywords(filename)))


def get_keywords(filename: str) -> list:
    """Read keywords from file and return as list of strings

    :param filename: file to read from
    :return: list of keywords
    """

    with open(filename, 'r', encoding='utf-8') as file_content:
        return file_content.read().splitlines()
