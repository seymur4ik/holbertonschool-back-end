#!/usr/bin/python3
"""
Script that, using REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import json
from urllib import request


def export_to_json():

    user_json = request.urlopen('https://jsonplaceholder.typicode.com/users')

    all_users = json.loads(user_json.read())

    todos_dict = {}

    for user in all_users:
        user_id = user['id']
        username = user['username']
        todos_json = request.urlopen('https://jsonplaceholder.typicode.com/' +
                                     f'todos?userId={user_id}')
        todos_list = json.loads(todos_json.read())

        todos_dict[user_id] = []

        for task in todos_list:
            todos_dict[user_id].append({
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": username
                })

    with open("todo_all_employees.json", "w") as afile:
        json.dump(todos_dict, afile)


if __name__ == "__main__":
    export_to_json()
