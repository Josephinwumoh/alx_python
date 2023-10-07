import requests
import sys

def gather_todo_progress(employee_id):
    # Define the API endpoints for employee details and TODO list
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    try:
        # Fetch employee details
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()
        employee_name = employee_data["name"]

        # Fetch TODO list
        todo_response = requests.get(todo_url)
        todo_list = todo_response.json()

        # Calculate progress
        total_tasks = len(todo_list)
        completed_tasks = sum(1 for task in todo_list if task["completed"])

        # Display progress in the required format
        print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
        for task in todo_list:
            if task["completed"]:
                print(f"    {task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    gather_todo_progress(employee_id)