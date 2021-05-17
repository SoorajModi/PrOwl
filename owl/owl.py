from .reddit import stream
from .scan import is_match
from .notify import notify

submission_stream = stream()


def watch():
    for submission in submission_stream:
        handle_submission(submission, "owl/scan/keywords.txt", "owl/notify/message.txt")


def handle_submission(submission, keywords: str, message: str):
    if is_match(submission.selftext, keywords):
        notify(submission, message)
