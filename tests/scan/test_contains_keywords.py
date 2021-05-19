from prowl.scan import contains_keywords


def test_contains_keywords_return_true():
    expected: bool = True
    received: bool = contains_keywords('1', 'tests/scan/test_scan.txt')

    assert expected == received


def test_contains_keywords_return_false():
    expected: bool = False
    received: bool = contains_keywords('0', 'tests/scan/test_scan.txt')

    assert expected == received
