class Task:
    """Represents one task in the To-Do Manager."""

    def __init__(self, task_id, title, category, priority, due_date):
        self.id = task_id
        self.title = title
        self.category = category
        self.priority = priority
        self.due_date = due_date
        self.status = "Pending"

    def to_dict(self):
        """Convert the task to a dictionary for storage in a Python list."""
        return {
            "id": self.id,
            "title": self.title,
            "category": self.category,
            "priority": self.priority,
            "due_date": self.due_date,
            "status": self.status,
        }
