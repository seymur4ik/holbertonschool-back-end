#!/usr/bin/python3
"""
Script that, using REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import json
from sys import argv
from urllib import request


def write_user_tasks_to_file():
    employee_id = argv[1]

    todos_json = request.urlopen('https://jsonplaceholder.typicode.com/' +
                                 f'todos?userId={employee_id}')

    user_json = request.urlopen('https://jsonplaceholder.typicode.com/' +
                                f'users/{employee_id}')

    todos = json.loads(todos_json.read())
    employee = json.loads(user_json.read())
    employee_name = employee['username']

    data_string = ""

    for task in todos:
        status = task['completed']
        title = task['title']

        data_string += (
                f'"{employee_id}",'
                f'"{employee_name}",'
                f'"{status}",'
                f'"{title}"\n'
        )

    filename = argv[1] + '.csv'
    with open(filename, 'w') as afile:
        afile.write(data_string)


if __name__ == "__main__":
    if len(argv) == 2:
        write_user_tasks_to_file()
