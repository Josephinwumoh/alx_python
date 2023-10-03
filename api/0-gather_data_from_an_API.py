import requests

import sys

def my_todo_list(Employee_id):
    """Defining the API endpoint for employee"""
    Employee_url =  f"https://jsonplaceholder.typicode.com/users/{my_todo_list}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{my_todo_list}/todos"

    try:
        """ Getting the employee details"""
        Employee_response = requests.get(Employee_url)
        Employee_data = Employee_response.json()
        Employee_name = Employee_data.get("name")

        """Getting Todo list"""
        todo_response = requests.get(todo_url)
        todo_list = todo_response.json()

        """Getting number of completed items"""
        completed_tasks = [task for task in todo_list if task["completed"]]
        total_tasks = len(todo_list)
        num_completed = len(completed_tasks)

        """Get output results"""
        print(f"Employee {Employee_name} is done with tasks({num_completed}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <Employee_id>")
        sys.exit(1)

    Employee_id = int(sys.argv[1])
    my_todo_list(Employee_id)
