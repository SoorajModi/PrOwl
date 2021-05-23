"""Scan text and check if it contains a keyword
"""
from prowl.utility.file import read_file_by_line


def contains_keywords(text: str, keywords: list) -> bool:
    """Check if text contains a keyword from a list of keyword

    :param text: text to analyze
    :param keywords: list of keywords to match
    :return: true if match is found, false if no match
    """

    return any(map(text.__contains__, keywords))


def get_keywords(filename: str) -> list:
    """Read keyword from file and return as list of strings

    :param filename: path to file to read from
    :return: list of keyword
    """

    return read_file_by_line(filename)
