"""Notify the user

Will send an email to a preset recipient with details about the match.

    Usage example:

    from .notify import notify
    notify(submission, "prowl/notify/message.txt")

"""

from .notify import notify
