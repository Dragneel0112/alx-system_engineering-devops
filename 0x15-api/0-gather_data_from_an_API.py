#!/usr/bin/python3
"""
Requests from API
"""

from json import load
import requests
from sys import argv


if __name__ == "__main__":

    def api_request(resource, param=None):
        """
        Retrieve information from API
        """
        url = 'https://jsonplaceholder.typicode.com/'
        url += resource
        if param:
            url += ('?' + param[0] + '=' + param[1])

        # Request url
        r = requests.get(url)

        # Extract json response
        r = r.json()
        return r

    user = api_request('users', ('id', argv[1]))
    tasks = api_request('todos', ('userId', argv[1]))
    tasks_completed = [task for task in tasks if task['completed']]

    print('Employee {} is done with tasks({}/{}):'.format(user[0]['name'],
                                                          len(tasks_completed),
                                                          len(tasks)))
    for task in tasks_completed:
        print('\t {}'.format(task['title']))
