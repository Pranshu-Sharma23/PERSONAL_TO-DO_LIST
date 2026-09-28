# Personal To-Do Manager

## 1. Project Overview

Personal To-Do Manager is a beginner-friendly Python console application for creating, organizing, searching, updating, and completing personal tasks.

The project uses only Python data structures, especially lists, during program execution. It does not use JSON, CSV, a database, or external storage.

## 2. Features

- Add tasks
- View all tasks
- Edit tasks
- Delete tasks
- Mark tasks as completed
- Search tasks by title
- Filter tasks by category
- Filter tasks by priority
- Filter tasks by status
- View task statistics
- Input validation
- Error handling
- Unit testing

## 3. Functional Modules

1. Task Management
2. Task Status Management
3. Priority and Category Management
4. Search and Filtering
5. Reporting and Statistics

## 4. Technologies Used

- Python 3
- Python lists
- Functions
- Classes
- Exception handling
- unittest

No external packages are required.

## 5. Project Structure

```text
Personal-To-Do-Manager/
├── main.py
├── task.py
├── task_manager.py
├── search.py
├── reports.py
├── storage.py
├── utils.py
├── tests/
│   └── test_tasks.py
├── README.md
├── statement.md
└── docs/
    └── project_report.pdf
```

## 6. How to Run

1. Install Python 3.
2. Open a terminal in the project folder.
3. Run:

```bash
python main.py
```

## 7. How to Run Tests

Run:

```bash
python -m unittest discover -s tests -v
```

## 8. Important Storage Decision

Tasks are stored only in Python lists while the program is running.

Therefore, when the program is closed, the tasks are cleared. This is intentional for the beginner version and avoids JSON, CSV, and databases.

## 9. Future Enhancements

Possible future improvements include a graphical interface, permanent storage, reminders, and user accounts. These are not part of the current implementation.
