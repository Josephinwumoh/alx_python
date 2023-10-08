import requests
import json
import sys

def export_to_json(id):
    # Define the API endpoints for employee details and TODO list
    id_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"

    try:
        # Fetch employee details
        response_id = requests.get(id_url)
        employee_data = response_id.json()
        user_id = employee_data["id"]
        username = employee_data["username"]

        # Fetch TODO list
        todo_response = requests.get(todo_url)
        todo_list = todo_response.json()

        """ Prepare the completed task """
        user_data = {
            str(user_id): [{"task": task["title"], "completed": task["completed"], "username": username} for task in todo_list]
        }

        # Create a JSON file for the user
        with open(f"{user_id}.json", "w") as json_file:
            json.dump(user_data, json_file)

        print(f"Data has been exported to {user_id}.json")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <id>")
        sys.exit(1)

    id = int(sys.argv[1])
    export_to_json(id)
