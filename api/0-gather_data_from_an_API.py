import requests, sys

def get_employee_data(employee_id):
    # URL to fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    # URL to fetch employee TO DO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    try:
        # Fetch employee data
        response_employee = requests.get(employee_url)
        response_employee.raise_for_status()
        employee_data = response_employee.json()
        
        # Fetch employee TO DO list
        response_todos = requests.get(todos_url)
        response_todos.raise_for_status()
        todos_data = response_todos.json()
        
        return employee_data,todos_data
    
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
        sys.exit(1)
        
def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
        
    employee_id = int(sys.argv[1])
    employee_data, todos_data = get_employee_data(employee_id)
    
    # Extract employee information
    employee_name = employee_data.get("name")
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo["completed"])
    
    # Print employee TO DO list progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    
    # Print titles of completed tasks
    for todo in todos_data:
        if todo["completed"]:
            print(f"\t {todo['title']}")

if __name__ == "__main__":
    main()