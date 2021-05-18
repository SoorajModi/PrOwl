"""This module will stream Reddit posts and notify the recipient if a match is found
"""

import logging
from .reddit import stream
from .scan import contains_keywords
from .notify import notify

LOG_FORMAT = "%(asctime)s::%(levelname)s::%(name)s::%(filename)s::%(lineno)d::%(message)s"
logging.basicConfig(level='INFO', format=LOG_FORMAT)


def watch() -> None:
    """Stream reddit posts from a specified subreddit
    :return: None
    """

    logging.info('PyOwl starting up...')
    for submission in stream():
        handle_submission(submission)


def handle_submission(submission) -> None:
    """Scan a submission and notify recipient if match is found
    :param submission: A Reddit submission
    :return: None
    """

    logging.info(f'Scanning submission...{submission.title}')

    if contains_keywords(submission.selftext, "owl/scan/keywords.txt"):
        logging.warning(f'Match found...{{\n'
                        f'\title: {submission.title},\n '
                        f'\tlink: {submission.link},\n '
                        f'\tcontent: {submission.selftext}\n}}')
        notify(submission, "owl/notify/message.txt")
