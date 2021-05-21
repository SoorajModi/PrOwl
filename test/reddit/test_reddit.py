from prowl.reddit.reddit import get_subreddit


def test_return_one_subreddit():
    expected: str = "test"
    received: str = get_subreddit('test/reddit/one_subreddit.txt')

    assert expected == received


def test_return_two_subreddits():
    expected: str = "test1+test2"
    received: str = get_subreddit('test/reddit/two_subreddit.txt')

    assert expected == received


def test_return_three_subreddits():
    expected: str = 'test1+test2+test3'
    received: str = get_subreddit('test/reddit/three_subreddit.txt')

    assert expected == received


def test_return_four_subreddits():
    expected: str = 'test1+test2+test3+test4'
    received: str = get_subreddit('test/reddit/four_subreddits.txt')

    assert expected == received
