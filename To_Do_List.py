class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, name, description):
        self.tasks[name] = description

    def update_task(self, name, new_description):
        if name in self.tasks:
            self.tasks[name] = new_description
            print("Task updated successfully.")
        else:
            print("Task not found.")

    def remove_task(self, name):
        if name in self.tasks:
            del self.tasks[name]
            print("Task removed successfully.")
        else:
            print("Task not found.")

    def display_all_tasks(self):
        if self.tasks:
            print("Your Tasks:")
            for idx, (name, description) in enumerate(self.tasks.items(), start=1):
                print(f"{idx}. {name}: {description}")
        else:
            print("No tasks found.")


def main():
    task_manager = TaskManager()
    menu_options = {
        '1': ("Add Task", lambda: task_manager.add_task(input("Enter task name: "), input("Enter task description: "))),
        '2': ("Update Task", lambda: task_manager.update_task(input("Enter task name to update: "), input("Enter new task description: "))),
        '3': ("Remove Task", lambda: task_manager.remove_task(input("Enter task name to remove: "))),
        '4': ("Display All Tasks", task_manager.display_all_tasks),
        '5': ("Exit", exit)
    }

    while True:
        print("\nMenu:")
        for key, (option, _) in menu_options.items():
            print(f"{key}. {option}")
        choice = input("Enter your choice: ")

        selected_option = menu_options.get(choice)
        if selected_option:
            _, action = selected_option
            action()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

