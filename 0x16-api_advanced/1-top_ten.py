#!/usr/bin/python3
"""
 function that queries the Reddit API and
 prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts
      listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent":
               "python:subreddit.top.ten:v1.0 (by /u/yourusername)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            articles = data.get('data', {}).get('children', [])
            if not articles:
                print(None)
                return
            for article in articles:
                print(article['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        print(None)
