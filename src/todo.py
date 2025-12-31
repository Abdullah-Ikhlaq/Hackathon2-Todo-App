from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Task:
    id: int
    title: str
    description: str
    completed: bool = False


class TodoManager:
    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def add_task(self, title: str, description: str) -> int:
        """Add a new task with auto-incremented ID"""
        if not title or not title.strip():
            raise ValueError("Title cannot be empty or whitespace")

        task = Task(id=self.next_id, title=title.strip(), description=description, completed=False)
        self.tasks.append(task)
        task_id = self.next_id
        self.next_id += 1
        return task_id

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks"""
        return self.tasks

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Return a specific task by ID"""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: str, description: str) -> bool:
        """Update task details by ID"""
        for task in self.tasks:
            if task.id == task_id:
                task.title = title
                task.description = description
                return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID"""
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                return True
        return False

    def mark_task_complete(self, task_id: int) -> bool:
        """Toggle completion status of a task by ID"""
        for task in self.tasks:
            if task.id == task_id:
                task.completed = not task.completed
                return True
        return False