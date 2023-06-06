#!/usr/bin/python3
'''
Queries Reddit Api
'''
import requests


after = ""


def recurse(subreddit, hot_list=[]):
    '''
    Queries Reddit Api for recursively for titles
    Args:
        subreddit(str) - The name of the subreddit to check
    '''
    global after
    header = {"User-Agent": "Dragneel"}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    if after:
        url = url + "?after=" + after
    r = requests.get(url, headers=header, allow_redirects=False)
    if r.status_code != 200:
        return None
    after = r.json().get("after", "")
    for i in r.json().get("data", None).get("children", None):
        hot_list.append(i.get("data", None).get("title", None))
    if after:
        return recurse(subreddit, hot_list)
    return hot_list

if __name__ == "__main__":
    pass
