#!/usr/bin/python3
"""
Requests from API
"""

from sys import argv
import requests


if __name__ == '__main__':

    u_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}/'.format(u_id)
    todos_url = url + 'todos'
    user = requests.get(url).json()
    todos = requests.get(todos_url).json()

    completed_todos = [todo for todo in todos if todo.get('completed') is True]

    print('Employee {} is done with tasks({}/{}):'.format(user.get('name'),
                                                          len(completed_todos),
                                                          len(todos)))

    for todo in completed_todos:
        print('\t {}'.format(todo.get('title')))
