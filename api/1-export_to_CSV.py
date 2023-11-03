import csv
import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        return

    employee_id = sys.argv[1]

    # Employee data
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return
    employee_data = employee_response.json()

    # Fetching todos data
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Failed to fetch todos for user {employee_data['name']}.")
        return
    todos_data = todos_response.json()

    # Exporting to CSV file
    csv_file = f"{employee_id}.csv"
    with open(csv_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos_data:
            csv_writer.writerow([employee_id], employee_data['username'], task['completed'], task['title'])

    print(f"Data exported to {csv_file}.")

if __name__ == "__main":
    main()