#!/usr/bin/python3
"""Count occurrence"""
import requests


def count_words(subreddit, word_list, hot_list=[], after="", word_count={}):
    """Count the occurrence of keywords in the titles of all
    hot posts for a subreddit."""
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

        word_list = [word.lower() for word in word_list]

        for post in posts:
            title = post.get('data', {}).get('title', '').lower()
            for word in word_list:
                if word in title.split():
                    word_count[word] = word_count.get(word, 0)\
                          + title.split().count(word)

        if after:
            return count_words(subreddit, word_list,
                               hot_list, after, word_count)

        sorted_words = sorted(word_count.items(), key=lambda
                              kv: (-kv[1], kv[0]))
        for word, count in sorted_words:
            if count > 0:
                print(f"{word}: {count}")
    else:
        return
