#!/usr/bin/python3
"""    
A script that queries the subscribers on a given subreddit
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Returns the total  number of subscribers from  a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'xica369'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)

