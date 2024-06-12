from models import Task  # Import the Task class from the models module

class TaskRepository:
  """
  A class for storing and managing tasks (in-memory for demonstration).
  """

  def __init__(self) -> None:
    self._tasks = []  # List to store tasks

  def add_task(self, task: Task) -> None:
    """
    Adds a new task to the list.

    Args:
      task: The Task object to add.
    """
    self._tasks.append(task)

  def get_all_tasks(self) -> list[Task]:
    """
    Returns a list of all stored tasks.
    """
    return self._tasks

  #... You can add additional methods for searching, filtering, etc. (optional)