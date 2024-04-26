#!/usr/bin/python3
"""
Script that, using REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import json
from sys import argv
from urllib import request


def export_to_json():
    employee_id = argv[1]

    todos_json = request.urlopen('https://jsonplaceholder.typicode.com/' +
                                 f'todos?userId={employee_id}')

    user_json = request.urlopen('https://jsonplaceholder.typicode.com/' +
                                f'users/{employee_id}')

    todos = json.loads(todos_json.read())
    employee = json.loads(user_json.read())
    username = employee['username']

    todos_dict = {employee_id: []}

    for task in todos:
        todos_dict[employee_id].append({
                "task": task['title'],
                "completed": task['completed'],
                "username": username
            })
    filename = argv[1] + ".json"

    with open(filename, "w") as afile:
        json.dump(todos_dict, afile)


if __name__ == "__main__":
    if len(argv) == 2:
        export_to_json()
