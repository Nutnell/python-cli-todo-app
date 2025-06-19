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
  
def list_tasks_command(args):
  tasks = load_tasks
  if not tasks:
    print("No tasks available.")
    return
  
  if args.today:
    today = date.today()
    filtered_tasks = [task for task in tasks if task.due_date == today and not task.completed]
    if not filtered_tasks:
      print(f"No pending tasks due today ({today.strftime('%Y-%m-%d')}).")
      return
    print(f"\n--- Pending Tasks Due Today ({today.strftime('%Y-%m-%d')}) ---")
    for task in filtered_tasks:
      print(task)
      
  else:
    print("\n--- All Tasks ---")
    tasks.sort(key=lambda t: (t.completed, t.id))
    for task in tasks:
      print(task)
  print("-----------------\n")  
  
def complete_task_command(args):
  tasks = load_tasks
  task_found = False
  for task in tasks:
    if task.id == args.task_id: 
      if not task.completed:        
        task.mark_complete()
        save_tasks(tasks)
        task_found = True
        break
      else:
        print(f"Task ID {args.task_id}: '{task.title}' is already completed.")
        task_found = True
        break
  if not task_found:
    print(f"Error: Task with ID {args.task_id} not found.")
    