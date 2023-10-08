""" Exporting to JSON """

import json
import requests
import sys

def export_to_json(employee_id):
    # Define the API endpoints for employee details and TODO list
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    try:
        # Fetch employee details
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()
        USER_ID= employee_data["id"]
        USERNAME = employee_data["username"]

        # Fetch TODO list
        todo_response = requests.get(todo_url)
        todo_list = todo_response.json()

        # Prepare data in JSON format
        user_data = {
            str(USER_ID): [{"task": task["TASK_TITLE"], "completed": task["TASK_COMPLETED_STATUS"], "username": USERNAME} for task in todo_list]
        }

        # Create a JSON file for the user
        with open(f"{USER_ID}.json", "w") as json_file:
            json.dump(user_data, json_file)

        print(f"Correct USER_ID: OK")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)