from .stream import stream
from .scan import scan

submission_stream = stream()


def watch():
    while True:
        for submission in submission_stream:
            text = submission.selftext
            res = scan(text)
            print(submission.title)
            if res != -1:
                print("Found")
            else:
                print("Not Found")
