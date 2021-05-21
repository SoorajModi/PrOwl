from prowl.scan.scan import get_keywords


def get_subreddits(filename: str) -> str:
    """Will collect list of subreddits from a file into a string

    :param filename: the path to the file with a list of
    :return: a + separated string with all subreddits
    """

    subreddit: list = get_keywords(filename)
    return '+'.join(subreddit)
