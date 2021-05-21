from prowl.keywords.scan import contains_keywords


def test_contains_keywords_return_true():
    expected: bool = True
    received: bool = contains_keywords('1', 'test/keywords/test_scan.txt')

    assert expected == received


def test_contains_keywords_return_false():
    expected: bool = False
    received: bool = contains_keywords('0', 'test/keywords/test_scan.txt')

    assert expected == received
