from prowl.utility.file import read_file_by_line


def get_subreddit(filename: str) -> str:
    """Will collect list of subreddits from a file into a string

    :param filename: the path to the file with a list of
    :return: a `+` separated string with all subreddits
    """

    subreddit: list = read_file_by_line(filename)
    return '+'.join(subreddit)