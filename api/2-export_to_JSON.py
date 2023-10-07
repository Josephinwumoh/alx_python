"""Get the employee data and export them to
CSV and JSON format
"""

import requests
import csv
import sys
import json


def my_todo_list(employee_id):
    """Defining the API endpoint for employee"""
    employee_url =  f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    try:
        """ Getting the employee details"""
        response_employee = requests.get(employee_url)
        response_employee.raise_for_status()
        employee_data = response_employee.json()

        """ Get emloyee list"""
        response_todo = requests.get(todo_url)
        response_todo.raise_for_status()
        todo_data = response_todo.json()

        return employee_data, todo_data
    
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
        sys.exit(1)

def export_to_csv(employee_id, employee_name, todo_data):
    csv_filename = f"{employee_id}.csv"

    with open(csv_filename, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)

        """ Writing the CSV header """
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        """ Writing the tasks data """
        for todo in todo_data:
            csv_writer.writerow([employee_id, employee_name, todo["completed"], todo["title"]])

def export_to_json(employee_id, employee_name, todo_data):
    json_filename = f"{employee_id}.json"
    json_data = {
        "USER_ID": [
            {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": employee_name
            }
            for todo in todo_data
        ]
    }
    with open(json_filename, "w") as json_file:
        json.dump(json_data, json_file)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

        employee_id = int(sys.argv[1])
        employee_data, todo_data = get_employee_data(employee_id)

        """Extracting employee info"""
        employee_name = employee_data.get("name")

        """Exporting data to CSV"""
        export_to_csv(employee_id, employee_name, todo_data)
        print(f"Data export to {employee_id}.csv")

        """Exporting data to JSON"""
        export_to_json(employee_id, employee_name, todo_data)
        print(f"Data exported to {employee_id}.json")