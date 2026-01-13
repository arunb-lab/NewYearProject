import json
import os

# File where tasks will be stored
DATA_FILE = "todo_list.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    print("\n--- YOUR TO-DO LIST ---")
    if not tasks:
        print("Your list is empty.")
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else " "
        print(f"{i}. [{status}] {task['title']}")
    print("-----------------------\n")

def main():
    tasks = load_tasks()
    
    while True:
        show_tasks(tasks)
        print("Commands: [a]dd, [d]elete, [c]heck/uncheck, [q]uit")
        choice = input("Action: ").lower()

        if choice == 'a':
            title = input("Enter task description: ")
            tasks.append({"title": title, "done": False})
        
        elif choice == 'd':
            idx = int(input("Enter number to delete: ")) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
        
        elif choice == 'c':
            idx = int(input("Enter number to toggle: ")) - 1
            if 0 <= idx < len(tasks):
                tasks[idx]["done"] = not tasks[idx]["done"]
        
        elif choice == 'q':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        
        save_tasks(tasks)

if __name__ == "__main__":
    main()