#!/usr/bin/python3
"""
Requests from API
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    todos_url = get('https://jsonplaceholder.typicode.com/todos/')
    todos_data = todos_url.json()
    todos_completed = 0
    todos_count = 0
    tasks = []
    user_url = get('https://jsonplaceholder.typicode.com/users')
    user_data = user_url.json()

    for i in user_data:
        if i.get('id') == int(argv[1]):
            employee = i.get('name')

    for i in todos_data:
        if i.get('userId') == int(argv[1]):
            todos_count += 1

            if i.get('completed') is True:
                todos_completed += 1
                tasks.append(i.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(employee,
                                                          todos_completed,
                                                          todos_count))

    for i in tasks:
        print("\t {}".format(i))
