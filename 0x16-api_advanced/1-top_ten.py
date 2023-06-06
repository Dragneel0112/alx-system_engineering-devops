#!/usr/bin/python3
'''
Queries Reddit Api
'''
import requests


def top_ten(subreddit):
    '''
    Queries Reddit Api for top ten hot posts in selected subreddit
    Args:
        subreddit(str) - The name of the subreddit to check
    '''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    data = requests.get(url, headers={'User-agent': 'Dragneel'},
                        allow_redirects=False)
    if data.status_code == 200:
        post_list = data.json().get('data').get('children')
        count = 0
        for post in post_list:
            if count == 10:
                break
            print(post.get("data").get("title"))
            count = count + 1
    else:
        print("None")
