"""Read text files
"""


def read_file(filename) -> str:
    """Read the contents of the file into a string

    :param filename: path to the file to be read
    :return: string will contents of the file
    """

    with open(filename, 'r', encoding='utf-8') as file_content:
        return file_content.read()


def read_file_by_line(filename) -> list:
    """Read the contents of the file by line

    :param filename: path to the file to be read
    :return: list with each line of the file in a different node
    """

    return read_file(filename).splitlines()
