from string import Template


def generate_message(submission, template: str):
    template = read_template(template)
    return template.substitute(title=submission.title, link=submission.url, post=submission.selftext)


def read_template(template: str):
    with open(template, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)
