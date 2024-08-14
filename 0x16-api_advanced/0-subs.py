#!/usr/bin/bash
"""
    A script that queries the subscribers on a given subreddit
"""

import requests

def number_of_subscribers(subreddit):
    """
        Returns the total  number of subscribers from  a given subreddit
    """
    url = "https://www.reddit.com/{}/about.json".format(subreddit)
    headers = {'User-Agent' : 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code==200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0

