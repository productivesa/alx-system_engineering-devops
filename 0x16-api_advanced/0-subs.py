#!/usr/bin/python3
"""functio queries Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):

    """ get number of subscribers """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'user-agent': 'request'}
    response = requests.get{url, headers = headers, allow_redirects = False}

    if response.status_code != 200:
        return 0

    data = response.json().get("data")
    num_subs = data.get("subscribers")

    return num_subs
