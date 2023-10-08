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
        username = employee_data["username"]

        # Fetch TODO list
        todo_response = requests.get(todo_url)
        todo_list = todo_response.json()

        # Prepare data in JSON format
        user_data = {
            str(user_id): [{"task": task["title"], "completed": task["completed"], "username": username} for task in todo_list]
        }

        # Create a JSON file for the user
        with open(f"{user_id}.json", "w") as json_file:
            json.dump(user_data, json_file)

        print(f"Data has been exported to {USER_ID}.json")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_json(employee_id)
