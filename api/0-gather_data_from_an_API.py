#!/usr/bin/python3
"""
Script that, using REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import json
from sys import argv
from urllib import request


def get_todos_by_userid():
    employee_id = argv[1]

    todos_json = request.urlopen('https://jsonplaceholder.typicode.com/' +
                                 f'todos?userId={employee_id}')

    user_json = request.urlopen('https://jsonplaceholder.typicode.com/' +
                                f'users/{employee_id}')

    todos = json.loads(todos_json.read())
    employee = json.loads(user_json.read())
    employee_name = employee['name']

    number_of_completed_tasks = sum([i['completed'] for i in todos])
    number_of_all_tasks = len(todos)

    # print title
    print(f'Employee {employee_name} is done with ', end="")
    print(f'tasks({number_of_completed_tasks}/{number_of_all_tasks}):')

    # print all completed tasks
    for task in todos:
        if task['completed']:
            print('\t ', task['title'])


if __name__ == "__main__":
    get_todos_by_userid()
