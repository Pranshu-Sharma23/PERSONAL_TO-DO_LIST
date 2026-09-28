def calculate_statistics(tasks):
    total = len(tasks)
    completed = sum(1 for task in tasks if task["status"] == "Completed")
    pending = total - completed
    high_priority = sum(1 for task in tasks if task["priority"] == "High")

    completion_percentage = (completed / total * 100) if total else 0

    categories = []
    for task in tasks:
        if task["category"] not in categories:
            categories.append(task["category"])

    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "high_priority": high_priority,
        "completion_percentage": completion_percentage,
        "category_count": len(categories),
    }


def print_statistics(statistics):
    print("\n--- TASK STATISTICS ---")
    print(f"Total tasks          : {statistics['total']}")
    print(f"Completed tasks      : {statistics['completed']}")
    print(f"Pending tasks        : {statistics['pending']}")
    print(f"High-priority tasks  : {statistics['high_priority']}")
    print(f"Categories used      : {statistics['category_count']}")
    print(f"Completion percentage: {statistics['completion_percentage']:.2f}%")
