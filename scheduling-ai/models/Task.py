from datetime import datetime

from typing import Optional


class Task:
  """
  A class to represent a task with name, priority, scheduled time, duration, and an ID.
  """

  # Class variable to keep track of assigned IDs (starts at 1)
  next_id = 1

  def __init__(self, user_id: int, name: str, priority: str = "P2", scheduled_time: Optional[datetime] = None, duration: int = 2) -> None:
    """
    Initializes a Task object.

    Args:
      name: The name of the task (text, required).
      priority: The priority of the task (e.g., "P0", "P1", "P2", "P3", defaults to "P2").
      scheduled_time: The scheduled time for the task (datetime object, optional).
      duration: The estimated duration of the task (numeric, defaults to 2 hours).
    """

    if not name:
      raise ValueError("Task name cannot be empty")

    self.id = Task.next_id  # Assign unique ID
    Task.next_id += 1  # Increment for future tasks
    self.user = user_id
    self.name: str = name
    self.priority: str = priority
    self.scheduled_time: Optional[datetime] = scheduled_time
    self.duration: int = duration

  def set_scheduled_time(self, scheduled_time: datetime) -> None:
    """
    Sets the scheduled time for the task.

    Args:
      scheduled_time: The scheduled time (datetime object).
    """
    self.scheduled_time = scheduled_time

  def __str__(self) -> str:
    """
    Returns a string representation of the Task object.
    """
    scheduled_str = self.scheduled_time.strftime("%Y-%m-%d %H:%M:%S") if self.scheduled_time else "Not Scheduled"
    return f"Task: {self.id} - {self.name}\n  Priority: {self.priority}\n  Scheduled Time: {scheduled_str}\n  Duration: {self.duration} hours"
