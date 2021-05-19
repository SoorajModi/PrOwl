# PyOwl

A Reddit watch bot.

## How to run

Install requirements: `pip install -r requirements.txt`

Run PyLint: `pylint **/*.py`

Run PyTest: `python -m pytest`

Run: `python index.py`

## How it works

PyOwl taps into the `new` feed for a given subreddit and analyzes the contents of each reddit submission to find a set of keywords.
Upon finding a match, PyOwl will send an email to a specified recipient using [Mailgun](https://app.mailgun.com). 

## License

MIT
