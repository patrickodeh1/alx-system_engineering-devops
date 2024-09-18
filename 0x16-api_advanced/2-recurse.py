#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Return a list of titles of all hot posts for a given
    subreddit recursively."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Python/requests:API_advanced:v1.0\
               (by /u/yourusername)'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        after = data.get('after')
        posts = data.get('children', [])
        for post in posts:
            hot_list.append(post.get('data', {}).get('title'))
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    return None
