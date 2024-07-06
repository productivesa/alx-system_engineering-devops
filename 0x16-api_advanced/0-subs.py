#!/usr/bin/python3
"""functio queries Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):

    """ get number of subscribers """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"user-agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    response = requests.get{url, headers = headers, allow_redirects = False}

    if response.status_code != 200:
        return 0

    my_sub = response.json().get("data")
    return = my_sub.get("subscribers")
