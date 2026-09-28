class ListStorage:
    """Simple in-memory storage implemented with a Python list.

    No JSON, CSV, database, or external file storage is used.
    """

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def get_all(self):
        return self.items

    def clear(self):
        self.items.clear()
