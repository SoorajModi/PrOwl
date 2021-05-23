from prowl.utility.file import read_file_by_line


def test_read_file_by_line_returns_string():
    expected: list = ["This", "is", "a", "test!"]
    received: list = read_file_by_line('test/utility/test_read_file.txt')

    assert expected == received
