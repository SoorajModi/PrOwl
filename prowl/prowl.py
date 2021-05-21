"""This module will stream Reddit posts and notify the recipient if a match is found
"""

import logging

from prowl.reddit.subreddit import get_subreddits
from .reddit.reddit import stream
from .scan.scan import contains_keywords
from .notify.notify import notify

LOG_FORMAT = "%(asctime)s::%(levelname)s::%(name)s::%(filename)s::%(lineno)d::%(message)s"
logging.basicConfig(level='INFO', format=LOG_FORMAT)

SUBREDDITS: str = get_subreddits('prowl/reddit/subreddits.txt')


def watch() -> None:
    """Stream reddit posts from a specified subreddit
    :return: None
    """

    logging.info('PyOwl starting up...')
    for submission in stream(SUBREDDITS):
        handle_submission(submission)


def handle_submission(submission) -> None:
    """Scan a submission and notify recipient if match is found
    :param submission: A Reddit submission
    :return: None
    """

    logging.info('Scanning submission...%s', submission.title)

    if contains_keywords(submission.selftext, "prowl/scan/keywords.txt"):
        logging.warning('Match found...{{\n'
                        '\title: %s,\n'
                        '\tlink: %s,\n'
                        '\tcontent: %s\n}}',
                        submission.title, submission.link, submission.selftext)
        notify(submission, "prowl/notify/message.txt")
