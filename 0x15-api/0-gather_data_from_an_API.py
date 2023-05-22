#!/usr/bin/python3
"""
Requests from API
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    task = get('https://jsonplaceholder.typicode.com/todos/')
    task_data = task.json()
    completed = 0
    total = 0
    tasks = []
    user = get('https://jsonplaceholder.typicode.com/users')
    user_data = user.json()

    for i in user_data:
        if i.get('id') == int(argv[1]):
            employee = i.get('name')

    for i in task_data:
        if i.get('userId') == int(argv[1]):
            total += 1

            if i.get('completed') is True:
                completed += 1
                tasks.append(i.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(employee, completed,
                                                          total))

    for i in tasks:
        print("\t {}".format(i))
