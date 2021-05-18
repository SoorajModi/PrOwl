"""Stream Reddit posts from a specified subreddit
"""

import os
from praw import Reddit
from dotenv import load_dotenv

load_dotenv()

USER_AGENT = os.getenv('USER_AGENT')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
SUBREDDIT = os.getenv('SUBREDDIT')


def stream() -> Reddit.submission:
    """Stream reddit submissions in real time

    :return: Reddit submission
    """

    reddit = Reddit(
        user_agent=USER_AGENT,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        username=USERNAME,
        password=PASSWORD
    )
    reddit.read_only = True

    return reddit.subreddit(SUBREDDIT).stream.submissions(skip_existing=True)
