import requests
import random

def get_todo(item_id):
    """Fetches a to-do item from the JSONPlaceholder API."""
    api_url = f"https://jsonplaceholder.typicode.com/todos/{item_id}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def main():
    """Main function to run the script."""
    random_id = random.randint(1, 100)
    todo_item = get_todo(random_id)

    if todo_item:
        print("--- Random To-Do Item ---")
        print(f"User ID: {todo_item.get('userId')}")
        print(f"Title: {todo_item.get('title')}")
        print(f"Completed: {todo_item.get('completed')}")

if __name__ == "__main__":
    main()