import unittest
import os
import json
from datetime import datetime, date

from utils import load_tasks, save_tasks, TASKS_FILE
from task import Task

class TestUtils(unittest.TestCase):
    def setUp(self):
        if os.path.exists(TASKS_FILE):
            os.remove(TASKS_FILE)
        Task.reset_assigned_id()
        print(f"\n--- Running setUp for {self._testMethodName} ---")

    def tearDown(self):
        if os.path.exists(TASKS_FILE):
            os.remove(TASKS_FILE)
        print(f"--- Finished {self._testMethodName} ---\n")

    def test_load_tasks_no_file(self):
        print("Test: Loading tasks with no file present.")
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)
        self.assertEqual(Task._assigned_id, 1)

    def test_load_tasks_empty_file(self):
        print("Test: Loading tasks from an empty file.")
        with open(TASKS_FILE, 'w', encoding='utf-8') as f:
            f.write("")
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)
        self.assertEqual(Task._assigned_id, 1)

    def test_save_and_load_single_task(self):
        print("Test: Saving and loading a single task.")
        original_tasks = [Task("Test Task 1", "Description for Test Task 1")]
        save_tasks(original_tasks)

        loaded_tasks = load_tasks()
        self.assertEqual(len(loaded_tasks), 1)
        self.assertEqual(loaded_tasks[0].id, original_tasks[0].id)
        self.assertEqual(loaded_tasks[0].title, original_tasks[0].title)
        self.assertEqual(loaded_tasks[0].description, original_tasks[0].description)
        self.assertEqual(loaded_tasks[0].completed, original_tasks[0].completed)
        self.assertIsNone(loaded_tasks[0].due_date)
        self.assertEqual(Task._assigned_id, 2)

    def test_save_and_load_multiple_tasks(self):
        print("Test: Saving and loading multiple tasks.")
        task1 = Task("Multi-Task 1", "Desc 1", "2025-01-01", False)
        task2 = Task("Multi-Task 2", "Desc 2", "2025-02-15", True)
        task3 = Task("Multi-Task 3", "Desc 3", "2025-03-30", False)
        original_tasks = [task1, task2, task3]
        save_tasks(original_tasks)

        loaded_tasks = load_tasks()
        self.assertEqual(len(loaded_tasks), 3)

        self.assertEqual(loaded_tasks[0].id, task1.id)
        self.assertEqual(loaded_tasks[0].title, task1.title)
        self.assertEqual(loaded_tasks[0].completed, task1.completed)
        self.assertEqual(loaded_tasks[0].due_date, task1.due_date)

        self.assertEqual(loaded_tasks[1].id, task2.id)
        self.assertEqual(loaded_tasks[1].title, task2.title)
        self.assertEqual(loaded_tasks[1].completed, task2.completed)
        self.assertEqual(loaded_tasks[1].due_date, task2.due_date)

        self.assertEqual(loaded_tasks[2].id, task3.id)
        self.assertEqual(loaded_tasks[2].title, task3.title)
        self.assertEqual(loaded_tasks[2].completed, task3.completed)
        self.assertEqual(loaded_tasks[2].due_date, task3.due_date)

        self.assertEqual(Task._assigned_id, 4)

    def test_load_tasks_invalid_json(self):
        print("Test: Loading tasks from invalid JSON.")
        with open(TASKS_FILE, 'w', encoding='utf-8') as f:
            f.write("{'id': 1, 'title': 'Bad JSON',}")

        import sys
        from io import StringIO
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()

        tasks = load_tasks()

        sys.stdout = old_stdout
        output = mystdout.getvalue()

        self.assertEqual(len(tasks), 0)
        self.assertIn("Error: Could not decode JSON", output)
        self.assertEqual(Task._assigned_id, 1)

    def test_save_tasks_empty_list(self):
        print("Test: Saving an empty list of tasks.")
        save_tasks([])
        self.assertTrue(os.path.exists(TASKS_FILE))
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            self.assertEqual(content, "[]")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

  
