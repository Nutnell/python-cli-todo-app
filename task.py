from datetime import datetime, date


class Task:
    _assigned_id = 1


def __init__(self, title, description="", due_date=None, completed=False, task_id=None):

    if task_id is not None:
        self.id = task_id

    if task_id >= Task._assigned_id:
        Task._assigned_id = task_id + 1
    else:
        self_id = Task._assigned_id
        Task._assigned_id = + 1

    self.title = title
    self.description = description
    self.completed = completed
    
    if due_date:
      try:
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
      except ValueError:
        self.due_date=None
        print(f"Warning: Invalid date format for task '{title}'")
      else:
        self.due_date=None

def mark_complete(self):
  self.completed=True
  print(f"Task {self.id}: '{self.title}' marked as completed.")