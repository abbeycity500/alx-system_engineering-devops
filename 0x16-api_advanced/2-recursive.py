#!/usr/bin/python3
"""This module contain a recursive function"""

import requests

def recurse(subreddit, hot_list=[], after="", count=0):
    """Return a list of all hot articles for a given subreddit"""

    url = ("https:www.reddit.com/r/{}/hot/.json".format(subreddit))
    headers = {
        "User-Agent" : "0x16-api_advanced:project:\
                        v1.0.0 (by /u/firdaus_cartoon_jr)"
    }

    params={
        "after": after,
        "count": counti,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params, allow_redirect=False)

    if response.status_code == 404:
        return None

        results = response.json().get("data")
        after = results.get("after")
        count += results.get("dist")
        for c in results.get("children"):
            hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list


