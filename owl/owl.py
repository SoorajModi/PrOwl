from .reddit import stream
from .scan import is_match
from .notify import notify

submission_stream = stream()


def watch():
    for submission in submission_stream:
        handle_submission(submission)


def handle_submission(submission):
    if is_match(submission.selftext):
        notify(submission)
    else:
        print('Match not found')
