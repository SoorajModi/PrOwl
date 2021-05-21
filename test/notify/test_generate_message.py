from string import Template
from prowl.notify.message import generate_message


class MockSubmission(object):
    def __init__(self, title, url, selftext):
        self.title = title
        self.url = url
        self.selftext = selftext


def test_generate_message():
    submission: MockSubmission = MockSubmission('title', 'url', 'selftext')
    template: Template = Template('Title: $title\nLink: $link\nPost: $post\n\nHoot hoot <3\n')

    expected: str = "Title: title\nLink: url\nPost: selftext\n\nHoot hoot <3\n"
    received: str = generate_message(submission, template)

    assert expected == received
