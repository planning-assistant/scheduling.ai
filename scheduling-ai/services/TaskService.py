from typing import List
from repositories import TaskRepository
from models import Task

class TaskService:
  """
  A class for handling task management business logic.
  """

  def __init__(self, repository: TaskRepository) -> None:
    self._repository = repository

  def add_task(self, user_id: str, task: Task) -> None:
    """
    Adds a new task for the user to the repository.

    Args:
      user_id: The ID of the user for whom the task is being added.
      task: The Task object to add.
    """

    # Simulate associating the task with a user (replace with actual logic)
    task.user_id = user_id
    self._repository.add_task(task)

  def get_all_tasks(self) -> List[Task]:
    """
    Returns a list of all stored tasks (ignoring user for demonstration).
    """
    return self._repository.get_all_tasks()

  # ... You can add additional methods for task management (optional)
