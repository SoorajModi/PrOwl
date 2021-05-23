from string import Template

from prowl.notify.message import get_template


def test_get_template_returns_template():
    expected: Template = Template('Title: $title\nLink: $link\nPost: $post\n\nHoot hoot <3\n')
    received: Template = get_template('test/notify/test_template.txt')

    assert expected.__eq__(received)
