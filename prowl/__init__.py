"""PrOwl a Reddit watch bot

This program will watch for submissions on a specified subreddit and notify a user if a post matches
a set of keywords.

    Usage example:

    import prowl
    prowl.watch()

"""

from .prowl import watch
