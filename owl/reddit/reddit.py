import os
import praw
from dotenv import load_dotenv

load_dotenv()

USER_AGENT = os.getenv('USER_AGENT')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
SUBREDDIT = os.getenv('SUBREDDIT')

reddit = praw.Reddit(
    user_agent=USER_AGENT,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    username=USERNAME,
    password=PASSWORD
)

reddit.read_only = True
subreddit = SUBREDDIT


def stream():
    return reddit.subreddit(subreddit).stream.submissions(skip_existing=True)
