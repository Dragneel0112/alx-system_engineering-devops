#!/usr/bin/python3
"""
Exports data in the CSV format from API
"""

from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    todos_url = get('https://jsonplaceholder.typicode.com/todos/')
    todos_data = todos_url.json()

    task = []
    user_url = get('https://jsonplaceholder.typicode.com/users')
    user_data = user_url.json()

    for i in user_data:
        if i['id'] == int(argv[1]):
            employee = i['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        data = csv.writer(file, quoting=csv.QUOTE_ALL)

        for i in todos_data:

            task = []
            if i['userId'] == int(argv[1]):
                task.append(i['userId'])
                task.append(employee)
                task.append(i['completed'])
                task.append(i['title'])

                data.writerow(task)
