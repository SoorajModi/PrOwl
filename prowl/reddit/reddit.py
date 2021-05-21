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

REDDIT = Reddit(
    user_agent=USER_AGENT,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    username=USERNAME,
    password=PASSWORD,
)

REDDIT.read_only = True


def stream(subreddits: str) -> Reddit.submission:
    """Stream reddit submissions in real time

    :return: Reddit submission
    """

    return REDDIT.subreddit(subreddits).stream.submissions(skip_existing=True)
