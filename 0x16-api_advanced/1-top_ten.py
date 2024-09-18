#!/usr/bin/python3
"""Top Ten"""
import requests


def top_ten(subreddit):
    """Print the titles of the top 10 hot posts of a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Python/requests:API_advanced:v1.0\
                (by /u/yourusername)'}
    try:
        req = requests.get(url, headers=headers, allow_redirects=False)

        if req.status_code == 200:
            for get_data in req.json().get("data").get("children"):
                dat = get_data.get("data")
                title = dat.get("title")
                print(title)
        else:
            print(None)

    except Exception:
        print(None)
