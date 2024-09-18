#!/usr/bin/python3
"""Top Ten"""
import requests


def top_ten(subreddit):
    """Print the titles of the top 10 hot posts of a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Python/requests:API_advanced:v1.0\
                (by /u/yourusername)'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            
            if not posts:
                print("None")
            else:
                for post in posts:
                    print(post.get('data', {}).get('title'))
        except ValueError:
            print("None")
    else:
        print("None")
