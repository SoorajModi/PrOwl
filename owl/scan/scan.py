substring_list = ["Latrialum", "latrialum", "Lats", "lats"]


def is_match(text: str) -> bool:
    return any(map(text.__contains__, substring_list))
