from task_manager import TaskManager
from utils import print_header, pause, get_non_empty_input, get_priority


def show_menu():
    print("\n1. Add Task")
    print("2. View All Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Mark Task Completed")
    print("6. Search / Filter Tasks")
    print("7. View Statistics")
    print("8. Exit")


def add_task(manager):
    print_header("ADD TASK")
    title = get_non_empty_input("Task title: ")
    category = get_non_empty_input("Category: ")
    priority = get_priority()
    due_date = get_non_empty_input("Due date (DD-MM-YYYY): ")
    manager.add_task(title, category, priority, due_date)
    print("Task added successfully.")


def view_tasks(manager, tasks=None):
    print_header("TASKS")
    items = manager.tasks if tasks is None else tasks
    if not items:
        print("No tasks found.")
        return

    print(f"{'ID':<5}{'Task':<30}{'Category':<15}{'Priority':<10}{'Due Date':<15}{'Status':<12}")
    print("-" * 87)
    for task in items:
        print(
            f"{task['id']:<5}{task['title'][:28]:<30}"
            f"{task['category'][:13]:<15}{task['priority']:<10}"
            f"{task['due_date']:<15}{task['status']:<12}"
        )


def get_task_id():
    while True:
        try:
            task_id = int(input("Enter task ID: "))
            if task_id > 0:
                return task_id
            print("ID must be positive.")
        except ValueError:
            print("Please enter a valid number.")


def edit_task(manager):
    print_header("EDIT TASK")
    view_tasks(manager)
    if not manager.tasks:
        return

    task_id = get_task_id()
    task = manager.find_task(task_id)
    if task is None:
        print("Task not found.")
        return

    print("Press Enter to keep the current value.")
    title = input(f"Title [{task['title']}]: ").strip()
    category = input(f"Category [{task['category']}]: ").strip()
    priority = input(f"Priority [{task['priority']}]: ").strip().capitalize()
    due_date = input(f"Due date [{task['due_date']}]: ").strip()

    if priority and priority not in ("High", "Medium", "Low"):
        print("Invalid priority. Keeping the current priority.")
        priority = task["priority"]

    manager.edit_task(
        task_id,
        title or task["title"],
        category or task["category"],
        priority or task["priority"],
        due_date or task["due_date"],
    )
    print("Task updated successfully.")


def delete_task(manager):
    print_header("DELETE TASK")
    view_tasks(manager)
    if not manager.tasks:
        return

    task_id = get_task_id()
    if manager.delete_task(task_id):
        print("Task deleted successfully.")
    else:
        print("Task not found.")


def complete_task(manager):
    print_header("MARK TASK COMPLETED")
    view_tasks(manager)
    if not manager.tasks:
        return

    task_id = get_task_id()
    if manager.complete_task(task_id):
        print("Task marked as completed.")
    else:
        print("Task not found.")


def search_tasks(manager):
    print_header("SEARCH / FILTER")
    print("1. Search by title")
    print("2. Filter by category")
    print("3. Filter by priority")
    print("4. Filter by status")

    choice = input("Choose an option: ").strip()
    if choice == "1":
        keyword = input("Enter title keyword: ").strip()
        results = manager.search_by_title(keyword)
    elif choice == "2":
        category = input("Enter category: ").strip()
        results = manager.filter_by_category(category)
    elif choice == "3":
        priority = get_priority()
        results = manager.filter_by_priority(priority)
    elif choice == "4":
        status = input("Enter status (Pending/Completed): ").strip().capitalize()
        if status not in ("Pending", "Completed"):
            print("Invalid status.")
            return
        results = manager.filter_by_status(status)
    else:
        print("Invalid option.")
        return

    view_tasks(manager, results)


def main():
    manager = TaskManager()

    while True:
        print_header("PERSONAL TO-DO MANAGER")
        show_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_task(manager)
        elif choice == "2":
            view_tasks(manager)
        elif choice == "3":
            edit_task(manager)
        elif choice == "4":
            delete_task(manager)
        elif choice == "5":
            complete_task(manager)
        elif choice == "6":
            search_tasks(manager)
        elif choice == "7":
            manager.show_statistics()
        elif choice == "8":
            print("\nThank you for using Personal To-Do Manager.")
            break
        else:
            print("Invalid choice. Please select 1-8.")

        pause()


if __name__ == "__main__":
    main()
