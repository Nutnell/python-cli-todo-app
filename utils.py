import json
import os
from datetime import datetime, date
from task import Task

TASKS_FILE="tasks.json"

def load_task():
    tasks=[]
    if not os.path.exists(TASKS_FILE):
        print(f"Info: '{TASKS_FILE}' not found. Creating an empty tasks' list")
        Task.reset_assigned_id()
        return tasks

    try:
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            content=f.read().strip()
            if not content:
                print(f"Info: '{TASKS_FILE}' not found. Creating an empty tasks' list")
                Task.reset_assigned_id()
                return tasks

            data= json.loads(content)
            for task_data in data:
                task=Task(
          title=task_data["title"],
          description=task_data.get("description", ""),
          due_date=task_data.get("due_date"),
          completed=task_data["completed"],
          task_id=task_data["id"]
        )
                tasks.append(task)

        Task.reset_assigned_id(tasks)
        print(f"Info: Successfully loaded {len(tasks)} tasks from '{TASKS_FILE}'.")
    except json.JSONDecodeError as e:
        print(
            f"Error: Could not decode JSON from '{TASKS_FILE}'. File might be corrupted. Error {e}"
        )
        Task.reset_assigned_id()
        return []
    except FileNotFoundError:
        print(f"Error: '{TASKS_FILE}' not found")
        Task.reset_assigned_id()
        return []
    except Exception as e:
        print(f"An unexpected error occured while loading tasks: {e}")
        Task.reset_assigned_id()
        return []
    return tasks
    
