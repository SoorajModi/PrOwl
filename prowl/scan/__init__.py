"""Scan and analyze text

Scan text and return if it matches a set of keywords

    Usage example:

    from .scan import is_match
    contains_keywords(submission.selftext, "prowl/scan/keywords.txt")

    from .scan import get_keywords
    get_keywords("prowl/scan/keywords.txt")

"""

from .scan import contains_keywords
from .scan import get_keywords
