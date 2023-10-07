#!/usr/bin/python3

import requests
import sys

def find_data(id):
    data_url =  f"https://jsonplaceholder.typicode.com/users/{id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
    result = 0

    """ Get the data """
    data = requests.get(data_url)
    todo = requests.get(todo_url)

    """ Parse the data """
    json_result = data.json()
    employee_name = json_result["name"]
    json_todo = todo.json()
    complete_tasks = len(json_todo)

    """ Show the completed tasks"""
    J = []
    for task in todo.json():
        if task["completed"]:
            result += 1
            J.append(task["title"])

    print(f"Employee {employee_name} is done with tasks ({result}/{complete_tasks}):")
    for task_title in J:
        print(f"\t{task_title}")

if __name__ == "__main__":
    id = sys.argv[1]
    find_data(id)