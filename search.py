def search(tasks, keyword):
    """Return tasks whose title contains the supplied keyword."""
    keyword = keyword.lower()
    return [task for task in tasks if keyword in task["title"].lower()]


def filter_tasks(tasks, field, value):
    """Generic list-based filter for a supported task field."""
    return [
        task for task in tasks
        if task.get(field, "").lower() == value.lower()
    ]
