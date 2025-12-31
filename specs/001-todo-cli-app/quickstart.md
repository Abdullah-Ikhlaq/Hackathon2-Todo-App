# Quickstart Guide: Todo CLI App

## Setup

1. Ensure Python 3.13+ is installed on your system
2. Install UV package manager: `pip install uv` (or follow official UV installation instructions)
3. Clone or create the project directory
4. Navigate to the project root directory

## Project Initialization

1. Initialize the project with UV:
   ```bash
   uv init
   ```

2. Create the required directory structure:
   ```
   project-root/
   ├── constitution.txt
   ├── README.md
   ├── specs_history/
   └── src/
       ├── __init__.py
       ├── main.py
       ├── todo.py
       └── cli.py
   ```

## Running the Application

1. To run the Todo CLI application:
   ```bash
   uv run src/main.py
   ```

2. The application will display a menu with the following options:
   - 1: Add Task
   - 2: View Tasks
   - 3: Update Task
   - 4: Delete Task
   - 5: Mark Complete
   - 0: Exit

## Basic Usage

1. **Adding a Task**: Select option 1, then enter the task title and description when prompted.

2. **Viewing Tasks**: Select option 2 to see all tasks with their ID, completion status, title, and description.

3. **Updating a Task**: Select option 3, enter the task ID, then provide new title/description (press Enter to skip updating a field).

4. **Deleting a Task**: Select option 4, enter the task ID, and confirm the deletion.

5. **Marking Complete**: Select option 5 and enter the task ID to toggle its completion status.

6. **Exiting**: Select option 0 to exit the application.

## Example Session

```
Welcome to the Todo App!
------------------------
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete
0. Exit
------------------------
Select an option: 1
Enter task title: Buy groceries
Enter task description: Milk, bread, eggs
Task added successfully with ID 1.

Select an option: 2
[1] [ ] Buy groceries: Milk, bread, eggs

Select an option: 5
Enter task ID to mark complete: 1
Task 1 marked as complete.

Select an option: 2
[1] [X] Buy groceries: Milk, bread, eggs

Select an option: 0
Goodbye!
```