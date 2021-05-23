from prowl.notify.message import validate_url


def test_validate_url():
    class MockSubmission(object):
        def __init__(self, title, url, selftext):
            self.title = title
            self.url = url
            self.selftext = selftext

    submission: MockSubmission = MockSubmission('title', 'url', 'selftext')
    expected: str = 'url'
    received: str = validate_url(submission)

    assert expected == received


def test_validate_url_missing_url():
    class MockSubmission(object):
        def __init__(self, title, selftext):
            self.title = title
            self.selftext = selftext

    submission: MockSubmission = MockSubmission('title', 'selftext')
    expected: str = 'https://www.reddit.com/r/mechmarket/new/'
    received: str = validate_url(submission)

    assert expected == received
