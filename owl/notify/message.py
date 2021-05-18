"""Generate a message based on a template given a Reddit submission
"""

from string import Template


def generate_message(submission, template: str) -> str:
    """Generate an email message

    :param submission: Reddit submission
    :param template: path to message template
    :return: message
    """

    template = read_template(template)
    return template.substitute(title=submission.title,
                               link=submission.url,
                               post=submission.selftext)


def read_template(template: str) -> Template:
    """Read template

    :param template: path to template
    :return: Template
    """

    with open(template, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)
