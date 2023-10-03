import requests
import csv
import sys
import os


def my_todo_list(employee_id):
    """Defining the API endpoint for employee"""
    employee_url =  f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    try:
        """ Getting the employee details"""
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()
        employee_name = employee_data.get("name")

        """Getting Todo list"""
        todo_response = requests.get(todo_url)
        todo_list = todo_response.json()

        """Creating a CSV file with the user ID as variable """
        filename = f"{employee_id}.csv"
        with open(filename, mode='w', newline='') as scv_file:
            fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for task in todo_list:
                writer.writerow({
                    "USER_ID": employee_id,
                    "USERNAME": employee_name,
                    "TASK_COMPLETED_STATUS": str(task["completed"]),
                    "TASK_TITLE": task["title"]
                })
        
        print(f"Data exported to {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    """Checking if CSV file exists"""
    filename = f"{employee_id}.csv"
    if os.path.exists(filename):
        my_todo_list(employee_id)
    else:
        print(f"CSV file for employee {employee_id} does not exist.")
