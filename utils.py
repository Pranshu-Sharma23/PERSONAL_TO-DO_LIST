def print_header(title):
    print("\n" + "=" * 55)
    print(title.center(55))
    print("=" * 55)


def pause():
    input("\nPress Enter to continue...")


def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def get_priority():
    while True:
        priority = input("Priority (High/Medium/Low): ").strip().capitalize()
        if priority in ("High", "Medium", "Low"):
            return priority
        print("Please enter High, Medium, or Low.")
