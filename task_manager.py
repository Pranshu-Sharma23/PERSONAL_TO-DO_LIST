from task import Task
from reports import calculate_statistics, print_statistics


class TaskManager:
    """Controls all task operations using an in-memory Python list."""

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, category, priority, due_date):
        task = Task(self.next_id, title, category, priority, due_date)
        self.tasks.append(task.to_dict())
        self.next_id += 1

    def find_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def edit_task(self, task_id, title, category, priority, due_date):
        task = self.find_task(task_id)
        if task is None:
            return False

        task["title"] = title
        task["category"] = category
        task["priority"] = priority
        task["due_date"] = due_date
        return True

    def delete_task(self, task_id):
        task = self.find_task(task_id)
        if task is None:
            return False

        self.tasks.remove(task)
        return True

    def complete_task(self, task_id):
        task = self.find_task(task_id)
        if task is None:
            return False

        task["status"] = "Completed"
        return True

    def search_by_title(self, keyword):
        keyword = keyword.lower()
        return [
            task for task in self.tasks
            if keyword in task["title"].lower()
        ]

    def filter_by_category(self, category):
        category = category.lower()
        return [
            task for task in self.tasks
            if task["category"].lower() == category
        ]

    def filter_by_priority(self, priority):
        return [
            task for task in self.tasks
            if task["priority"] == priority
        ]

    def filter_by_status(self, status):
        return [
            task for task in self.tasks
            if task["status"] == status
        ]

    def show_statistics(self):
        statistics = calculate_statistics(self.tasks)
        print_statistics(statistics)
