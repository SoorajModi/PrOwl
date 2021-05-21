"""Stream Reddit posts from a specified subreddit
"""

import os
from praw import Reddit
from dotenv import load_dotenv

from prowl.utility.read_file import read_file_by_line

load_dotenv()

USER_AGENT = os.getenv('USER_AGENT')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

REDDIT = Reddit(
    user_agent=USER_AGENT,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    username=USERNAME,
    password=PASSWORD,
)

REDDIT.read_only = True


def stream(subreddit: str) -> Reddit.submission:
    """Stream reddit submissions in real time

    :return: Reddit submission
    """

    return REDDIT.subreddit(subreddit).stream.submissions(skip_existing=True)


def get_subreddit(filename: str) -> str:
    """Will collect list of subreddits from a file into a string

    :param filename: the path to the file with a list of
    :return: a `+` separated string with all subreddits
    """

    subreddit: list = read_file_by_line(filename)
    return '+'.join(subreddit)
