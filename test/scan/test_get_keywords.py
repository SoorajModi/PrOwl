from prowl.scan import get_keywords


def test_should_get_list_of_keywords():
    expected: list = ["1", "2", "3", "4", "5"]
    received: list = get_keywords('test/scan/test_scan.txt')

    assert expected == received


def test_should_get_empty_list():
    expected: list = []
    received: list = get_keywords('test/scan/test_empty.txt')

    assert expected == received
