""" Gathering data from an API """

import requests
import sys

def Etodo(id):
    """Define the API endpoints for employee details and TODO list"""
    id_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"

    try:
        """ Get the employee data"""
        response_id = requests.get(id_url)
        id_data = response_id.json()
        employee_name = id_data["name"]

        """ Todo Lists """
        todo_response = requests.get(todo_url)
        todo_list = todo_response.json()

        """ What should be completed """
        total_tasks = len(todo_list)
        completed_tasks = sum(1 for task in todo_list if task["completed"])

        """ Show the completed tasks"""
        print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
        for task in todo_list:
            if task["completed"]:
                print(f" \t {task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <id>")
        sys.exit(1)

    id = int(sys.argv[1])
    Etodo(id)