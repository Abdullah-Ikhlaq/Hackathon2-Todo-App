from todo import TodoManager


def main():
    """Main application loop with menu interface"""
    todo_manager = TodoManager()

    while True:
        print("\nWelcome to the Todo App!")
        print("------------------------")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Complete")
        print("0. Exit")
        print("------------------------")

        try:
            choice = input("Select an option: ").strip()

            if choice == "0":
                print("Goodbye!")
                break
            elif choice == "1":
                from cli import add_task_cli
                add_task_cli(todo_manager)
            elif choice == "2":
                from cli import view_tasks_cli
                view_tasks_cli(todo_manager)
            elif choice == "3":
                from cli import update_task_cli
                update_task_cli(todo_manager)
            elif choice == "4":
                from cli import delete_task_cli
                delete_task_cli(todo_manager)
            elif choice == "5":
                from cli import mark_task_complete_cli
                mark_task_complete_cli(todo_manager)
            else:
                print("Invalid option. Please select 0-5.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected error occurred: {e}")