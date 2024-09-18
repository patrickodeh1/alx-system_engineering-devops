#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a given
    subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Python/requests:API_advanced:v1.0 \
               (by /u/yourusername)'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    return 0
