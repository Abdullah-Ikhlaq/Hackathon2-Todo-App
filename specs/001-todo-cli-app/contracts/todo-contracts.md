# Todo CLI App - Internal Interface Contracts

## Task Management Interface

### Task Class
```python
@dataclass
class Task:
    id: int
    title: str
    description: str
    completed: bool = False
```

### TodoManager Class Interface

#### add_task(title: str, description: str) -> int
- **Purpose**: Add a new task to the collection
- **Precondition**: title is non-empty and non-whitespace
- **Postcondition**: Task is added with unique auto-incremented ID
- **Returns**: The ID of the newly created task
- **Exceptions**: ValueError if title is invalid

#### get_all_tasks() -> List[Task]
- **Purpose**: Retrieve all tasks in the collection
- **Returns**: List of all Task objects in the order they were added

#### get_task_by_id(task_id: int) -> Optional[Task]
- **Purpose**: Retrieve a specific task by its ID
- **Returns**: Task object if found, None otherwise

#### update_task(task_id: int, title: str, description: str) -> bool
- **Purpose**: Update the title and/or description of an existing task
- **Precondition**: task with task_id exists
- **Postcondition**: Task details are updated
- **Returns**: True if update successful, False otherwise

#### delete_task(task_id: int) -> bool
- **Purpose**: Remove a task from the collection
- **Precondition**: task with task_id exists
- **Postcondition**: Task is removed from collection
- **Returns**: True if deletion successful, False otherwise

#### mark_task_complete(task_id: int) -> bool
- **Purpose**: Toggle the completion status of a task
- **Precondition**: task with task_id exists
- **Postcondition**: Task's completed status is toggled
- **Returns**: True if operation successful, False otherwise