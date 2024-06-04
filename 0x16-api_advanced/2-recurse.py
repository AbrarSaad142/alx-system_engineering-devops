#!/usr/bin/python3
"""
 recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot articles for
      a given subreddit recursively."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent":
               "python:subreddit.hot.articles:v1.0 (by /u/yourusername)"}
    params = {"after": after}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            articles = data.get('data', {}).get('children', [])
            if not articles:
                return hot_list
            for article in articles:
                hot_list.append(article['data']['title'])
            after = data['data'].get('after')
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
