import logging
from .reddit import stream
from .scan import is_match
from .notify import notify

log_format = "%(asctime)s::%(levelname)s::%(name)s::%(filename)s::%(lineno)d::%(message)s"
logging.basicConfig(level='INFO', format=log_format)

submission_stream = stream()


def watch():
    for submission in submission_stream:
        handle_submission(submission)


def handle_submission(submission):
    logging.info('Scanning submission... {' + submission.title + '}')

    if is_match(submission.selftext, "owl/scan/keywords.txt"):
        logging.warning("Match found")
        notify(submission, "owl/notify/message.txt")
