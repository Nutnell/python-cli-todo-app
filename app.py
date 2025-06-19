import argparse
from datetime import datetime, date
import sys

from task import Task
from utils import load_tasks, save_tasks

def add_task_command(args):
  tasks = load_tasks
  due_date_str = args.due_date
  if due_date_str:
    try:
      datetime.strptime(due_date_str, "%Y-%m-%d")
    except ValueError:
      print(f"Invalid date format '{due_date_str}'. Please use YYYY-MM-DD.")
      return
  new_task = Task(
    title=args.title,
    description=args.description
    due_date=due_date_str
  )
  tasks.append(new_task)
  save_tasks(tasks)
  print(f"Task added: {new_task.title} (ID: {new_task.id})")
  
 