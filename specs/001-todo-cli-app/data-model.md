# Data Model: Todo CLI App

## Entities

### Task
Represents a single todo item with the following attributes:

- **id**: int, auto-incremented unique identifier
- **title**: str, non-empty/non-whitespace task title
- **description**: str, optional task description (can be empty)
- **completed**: bool, completion status (default False)

### TodoManager
Manages the collection of tasks with the following responsibilities:

- **tasks**: List[Task], in-memory storage of all tasks
- **next_id**: int, tracks the next ID to assign (always highest used + 1)
- **add_task(title: str, description: str)**: Adds a new task with auto-assigned ID
- **get_all_tasks()**: Returns all tasks
- **get_task_by_id(task_id: int)**: Returns a specific task by ID
- **update_task(task_id: int, title: str, description: str)**: Updates task details
- **delete_task(task_id: int)**: Removes a task by ID
- **mark_task_complete(task_id: int)**: Toggles completion status of a task

## Validation Rules

1. **Title validation**: Title must be non-empty and non-whitespace
2. **ID validation**: IDs must be positive integers and unique
3. **Task existence**: Operations by ID must validate that the task exists
4. **Input type validation**: All inputs must be validated for correct types

## State Transitions

- **Task completion**: A task can transition between completed=False and completed=True states via the mark_task_complete operation
- **Task lifecycle**: A task moves from created → active → (updated/deleted) states