"""Generate a message based on a template given a Reddit submission
"""

from string import Template

from prowl.utility.file import read_file


def generate_message(submission, template: Template) -> str:
    """Generate an email message

    :param submission: Reddit submission
    :param template: path to message template
    :return: message
    """

    url: str = validate_url(submission)

    return template.substitute(title=submission.title,
                               link=url,
                               post=submission.selftext)


def validate_url(submission) -> str:
    if hasattr(submission, 'url'):
        return submission.url
    else:
        return 'https://www.reddit.com/r/mechmarket/new/'


def get_template(template: str) -> Template:
    """Read template from file

    :param template: path to template
    :return: Template
    """

    template_file_content: str = read_file(template)
    return Template(template_file_content)
