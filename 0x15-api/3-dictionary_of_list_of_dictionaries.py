#!/usr/bin/python3

"""
Exports data from API as dictionary
"""

from requests import get
import json

if __name__ == "__main__":
    todos_url = get('https://jsonplaceholder.typicode.com/todos/')
    todos_data = todos_url.json()

    task = []
    user_url = get('https://jsonplaceholder.typicode.com/users')
    user_data = user_url.json()

    new_dict = {}

    for j in user_data:

        task = []
        for i in todos_data:

            new_dict2 = {}

            if j['id'] == i['userId']:

                new_dict2['username'] = j['username']
                new_dict2['task'] = i['title']
                new_dict2['completed'] = i['completed']
                task.append(new_dict2)

        new_dict[j['id']] = task

    with open("todo_all_employees.json",  "w") as f:

        json_obj = json.dumps(new_dict)
        f.write(json_obj)
