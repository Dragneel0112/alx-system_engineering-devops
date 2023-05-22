#!/usr/bin/python3

"""
Exports data in the JSON format from API
"""

from requests import get
from sys import argv
import json

if __name__ == "__main__":
    todos_url = get('https://jsonplaceholder.typicode.com/todos/')
    todos_data = todos_url.json()

    task = []
    user_url = get('https://jsonplaceholder.typicode.com/users')
    user_data = user_url.json()

    for i in user_data:
        if i['id'] == int(argv[1]):
            user_name = i['username']
            id_no = i['id']

    task = []

    for i in todos_data:

        new_dict = {}

        if i['userId'] == int(argv[1]):
            new_dict['task'] = i['title']
            new_dict['completed'] = i['completed']
            new_dict['username'] = user_name
            task.append(new_dict)

    final_dict = {}
    final_dict[id_no] = task
    json_obj = json.dumps(final_dict)

    with open(argv[1] + ".json",  "w") as f:
        f.write(json_obj)
