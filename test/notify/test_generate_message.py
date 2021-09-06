from string import Template
from prowl.notify.message import generate_message


class Object(object):
    pass


class MockSubmission(object):
    def __init__(self, title, time, author, url, selftext):
        self.title = title
        self.created_utc = time
        self.author = Object
        self.author.name = author
        self.url = url
        self.selftext = selftext


def test_generate_message():
    submission: MockSubmission = MockSubmission('title', 'time', 'author', 'url', 'selftext')
    template: Template = Template('Title: $title\nTime: $time\nAuthor: $author\nLink: $link\nPost: $post\n\nHoot hoot '
                                  '<3\n')

    expected: str = "Title: title\nTime: time\nAuthor: author\nLink: url\nPost: selftext\n\nHoot hoot <3\n"
    received: str = generate_message(submission, template)

    assert expected == received
