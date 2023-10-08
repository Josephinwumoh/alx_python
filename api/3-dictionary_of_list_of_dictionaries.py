#!/usr/bin/python3
"""
Export data in the JSON format.
"""

import json
import requests

if __name__ == "__main__":
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    users_data = users_response.json()
    todos_data = todos_response.json()

    all_employee_tasks = {}

    for user in users_data:
        user_id = user.get('id')
        username = user.get('username')

        user_tasks = []

        for task in todos_data:
            if task.get('userId') == user_id:
                user_task = {
                    'username': username,
                    'task': task.get('title'),
                    'completed': task.get('completed')
                }
                user_tasks.append(user_task)

        all_employee_tasks[user_id] = user_tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_employee_tasks, json_file)
