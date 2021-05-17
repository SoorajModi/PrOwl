def is_match(text: str, keywords: str) -> bool:
    return any(map(text.__contains__, get_keywords(keywords)))


def get_keywords(filename: str) -> list:
    with open(filename, 'r', encoding='utf-8') as file_content:
        return file_content.read().splitlines()
