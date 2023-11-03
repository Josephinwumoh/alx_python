"""Exporting data in JSON format
"""

import json
import requests

if __name__ == "__main__":
    api_request_users = requests.get("https://jsonplaceholder.typicode.com/users")
    api_request_todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    users_data = api_request_users.json()
    todos_data = api_request_todos.json()

    filename = "todo_all_employees.json"

    result = {}
    for user in users_data:
        user_id = user["id"]
        username = user["username"]
        user_todos = [
            {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": username,
            }
            for todo in todos_data
            if todo["userId"] == user_id
        ]
        result[user_id] = user_todos

    with open(filename, "w") as outfile:
        json.dump(result, outfile)