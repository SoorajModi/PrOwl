"""This module will stream Reddit posts and notify the recipient if a match is found
"""

import logging
from string import Template

from prowl.notify.message import get_template
from prowl.reddit.subreddit import get_subreddit
from .reddit.reddit import stream
from .keyword.keyword import contains_keywords, get_keywords
from .notify.notify import notify

LOG_FORMAT = "%(asctime)s::%(levelname)s::%(name)s::%(filename)s::%(lineno)d::%(message)s"
logging.basicConfig(level='INFO', format=LOG_FORMAT)

SUBREDDIT: str = get_subreddit('prowl/reddit/subreddits.txt')
KEYWORD: list = get_keywords('prowl/keyword/keywords.txt')
TEMPLATE: Template = get_template('prowl/notify/template.txt')


def watch() -> None:
    """Stream reddit posts from a specified subreddit
    :return: None
    """

    logging.info('Starting PrOwl...')
    for submission in stream(SUBREDDIT):
        handle_submission(submission)


def handle_submission(submission) -> None:
    """Scan a submission and notify recipient if match is found
    :param submission: A Reddit submission
    :return: None
    """

    logging.info('Scanning submission...%s', submission.title)

    if contains_keywords(submission.selftext, KEYWORD):
        logging.warning('Match found...{{\n'
                        '\ttitle: %s,\n'
                        '\tposted: %s,\n'
                        '\tlink: %s,\n'
                        '\tcontent: %s\n}}',
                        submission.title, submission.created_utc,
                        submission.url, submission.selftext)
        notify(submission, TEMPLATE)
