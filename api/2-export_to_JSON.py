"""This program fetches employee data and exports it to both CSV and JSON format
"""
import json  # Import the json module
import requests
import sys

def main():
    employee_id = sys.argv[1]

    # Employee data
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return
    employee_data = employee_response.json()

    # Fetching todos data
    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Failed to fetch todos for user {employee_data['name']}.")
        return
    todos_data = todos_response.json()

    # Creating a list to store task records
    task_records = []

    for task in todos_data:
        task_record = {
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_data['username']
        }
        task_records.append(task_record)

    # Creating a dictionary with the user ID as the key and the list of task records as the value
    export_data = {
        employee_id: task_records
    }

    # Exporting to JSON file
    json_file = f"{employee_id}.json"
    with open(json_file, 'w') as jsonfile:
        json.dump(export_data, jsonfile, indent=4)  # Use json.dump to write data in JSON format

    print(f"Data exported to {json_file}.")

if __name__ == "__main":
    main()