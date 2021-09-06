from string import Template
from prowl.notify.message import generate_message


class MockAuthor(object):
    def __init__(self, name):
        self.name = name


class MockSubmission(object):
    def __init__(self, title, author, url, selftext):
        self.title = title
        self.author = MockAuthor(author)
        self.url = url
        self.selftext = selftext


def test_generate_message():
    submission: MockSubmission = MockSubmission('title', 'author', 'url', 'selftext')
    template: Template = Template('Title: $title\nAuthor: $author\nLink: $link\nPost: $post\n\nHoot hoot '
                                  '<3\n')

    expected: str = "Title: title\nAuthor: author\nLink: url\nPost: selftext\n\nHoot hoot <3\n"
    received: str = generate_message(submission, template)

    assert expected == received
