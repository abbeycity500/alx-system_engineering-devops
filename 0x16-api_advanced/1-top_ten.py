#!/usr/bin/python3
"""
    this module contain the function top_ten
"""

import requests
from sys import argv

def top_ten(subreddit):
    """
        Returns top ten posts for a given subreddit
    """
    user = {'User-Agent' : 'Elizabeth'}
    url = requests.get('https://www.reddit.com/r/a{}/hot/.json?limit=10'\
                       .format(subreddit), headers=user.json())
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get(title))
    except Exception:
        print(None)

if __name__ == __main__:
    top_ten(argv[1])



