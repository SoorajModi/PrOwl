![CI](https://github.com/SoorajModi/prowl/workflows/CI/badge.svg)
![License](https://img.shields.io/github/license/soorajmodi/prowl)


# PrOwl

Python Reddit Owl (PrOwl), a watch bot for Reddit. 
Built using the [Python Reddit API Wrapper (PRAW)](https://praw.readthedocs.io/en/latest/).

## How to run

Install requirements: `pip install .` or `pip install -r requirements.txt`

Run PyLint: `pylint **/*.py`

Run PyTest: `python -m pytest`

Run: `python -m prowl`

## How it works

PrOwl taps into the `new` feed for a given subreddit and analyzes the contents of each reddit submission to find a set of keywords.
Upon finding a match, PrOwl will send an email to a specified recipient using [Mailgun](https://app.mailgun.com). 

## License

MIT
