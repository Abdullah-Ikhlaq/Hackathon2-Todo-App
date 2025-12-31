from typing import Optional
from todo import Task


def get_task_input() -> tuple[str, str]:
    """Get title and description input from user"""
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    return title, description


def get_task_id() -> Optional[int]:
    """Get task ID input from user with validation"""
    try:
        task_id_input = input("Enter task ID: ").strip()
        if task_id_input.isdigit():
            return int(task_id_input)
        else:
            print("Invalid ID. Please enter a number.")
            return None
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return None


def confirm_action(action: str) -> bool:
    """Get confirmation from user before performing an action"""
    confirmation = input(f"Are you sure you want to {action}? (y/n): ").strip().lower()
    return confirmation in ['y', 'yes']


def display_tasks(tasks):
    """Display all tasks with proper formatting"""
    if not tasks:
        print("No tasks found.")
        return
    
    for task in tasks:
        status = "[X]" if task.completed else "[ ]"
        print(f"[{task.id}] {status} {task.title}: {task.description}")


def display_task(task: Task):
    """Display a single task with proper formatting"""
    status = "[X]" if task.completed else "[ ]"
    print(f"[{task.id}] {status} {task.title}: {task.description}")


def add_task_cli(todo_manager):
    """Handle the add task CLI flow"""
    try:
        title, description = get_task_input()

        # Validate title
        if not title or not title.strip():
            print("Error: Title cannot be empty or whitespace.")
            return False

        task_id = todo_manager.add_task(title, description)
        print(f"Task added successfully with ID {task_id}.")
        return True
    except ValueError as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred while adding task: {e}")
        return False


def view_tasks_cli(todo_manager):
    """Handle the view tasks CLI flow"""
    try:
        tasks = todo_manager.get_all_tasks()

        if not tasks:
            print("No tasks found.")
            return

        display_tasks(tasks)
    except Exception as e:
        print(f"An error occurred while viewing tasks: {e}")


def mark_task_complete_cli(todo_manager):
    """Handle the mark task complete CLI flow"""
    try:
        task_id = get_task_id()
        if task_id is None:
            return False

        success = todo_manager.mark_task_complete(task_id)
        if success:
            print(f"Task {task_id} marked as {'complete' if todo_manager.get_task_by_id(task_id).completed else 'incomplete'}.")
            return True
        else:
            print(f"Task with ID {task_id} not found.")
            return False
    except Exception as e:
        print(f"An error occurred while marking task complete: {e}")
        return False


def update_task_cli(todo_manager):
    """Handle the update task CLI flow with Enter-to-skip functionality"""
    try:
        task_id = get_task_id()
        if task_id is None:
            return False

        # Check if task exists
        task = todo_manager.get_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return False

        # Get new title, allowing Enter to skip
        new_title_input = input(f"Enter new title (current: '{task.title}', press Enter to skip): ").strip()
        new_title = new_title_input if new_title_input else task.title

        # Get new description, allowing Enter to skip
        new_description_input = input(f"Enter new description (current: '{task.description}', press Enter to skip): ").strip()
        new_description = new_description_input if new_description_input else task.description

        success = todo_manager.update_task(task_id, new_title, new_description)
        if success:
            print(f"Task {task_id} updated successfully.")
            return True
        else:
            print(f"Failed to update task {task_id}.")
            return False
    except Exception as e:
        print(f"An error occurred while updating task: {e}")
        return False


def delete_task_cli(todo_manager):
    """Handle the delete task CLI flow with confirmation"""
    try:
        task_id = get_task_id()
        if task_id is None:
            return False

        # Check if task exists
        task = todo_manager.get_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return False

        # Confirm deletion
        if not confirm_action(f"delete task {task_id}"):
            print("Deletion cancelled.")
            return False

        success = todo_manager.delete_task(task_id)
        if success:
            print(f"Task {task_id} deleted successfully.")
            return True
        else:
            print(f"Failed to delete task {task_id}.")
            return False
    except Exception as e:
        print(f"An error occurred while deleting task: {e}")
        return False