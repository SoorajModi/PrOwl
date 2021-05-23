from prowl.utility.file import read_file


def test_read_file_returns_string():
    expected: str = "This\nis\na\ntest!\n"
    received: str = read_file('test/utility/test_read_file.txt')

    assert expected == received


def test_read_file_returns_empty_string():
    expected: str = ""
    received: str = read_file('test/utility/test_empty_file.txt')

    assert expected == received
