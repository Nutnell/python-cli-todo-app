# Python CLI To-Do Application

## Project Description

This is a simple command-line interface (CLI) To-Do application built with Python. It allows users to manage their tasks directly from the terminal, including adding new tasks, listing existing ones, marking tasks as complete, and deleting them. All tasks are persisted to a `tasks.json` file, so your tasks are saved even after closing the application.

## Features

* **Add Tasks:** Add new tasks with a title, optional description, and optional due date.
    * `python app.py add "Task Title"`
    * `python app.py add "Task Title" -d "Task description"`
    * `python app.py add "Task Title" --due YYYY-MM-DD`
    * `python app.py add "Task Title" -d "Description" --due YYYY-MM-DD`

        ![Terminal window showing a user adding a new task using the add command in the Python CLI To-Do application. The screen displays the command input and confirmation message Task added successfully. The environment is a typical command-line interface with a neutral tone focused on productivity.]('Add'-Task-functionality.png)


* **List Tasks:** View all tasks, showing their ID, title, description, due date, and completion status.
    * `python app.py list`

        ![Terminal window displaying the output of the list command in the Python CLI To-Do application. The screen shows a table with columns for task ID, title, description, due date, and completion status. Example tasks are listed with their details, and completed tasks are clearly marked.]('List'-Task-Functionality.png)

* **List Tasks Due Today:** Filter and display only pending tasks that are due on the current day.
    * `python app.py list --today`

        ![Terminal window displaying the output of the list command filtered to show only tasks due today in the Python CLI To-Do application. The screen presents a table with columns labeled ID, Title, Description, Due Date, and Status. One task with a due date matching the current day is listed, one row showing task details and whether the task is completed or pending.]('Due-today'-Task-functionality.png)

* **Complete Tasks:** Mark a task as completed using its unique ID.
    * `python app.py complete <task_id>`

        ![Terminal window displaying how the mark a Task as complete works and the output of the list command after marking task 5 as completed]('Complete'-Task-functionality.png)

* **Delete Tasks:** Permanently remove a task using its unique ID.
    * `python app.py delete <task_id>`

        ![Terminal window displaying how the delete Task works and the output of the list command after deleting task 2]('Delete'-Task-functionality.png)

* **Data Persistence:** Tasks are automatically saved to and loaded from `tasks.json`.
        ![A screenshot of tasks loaded in the json file](tasks-json.png)

* **Robust Error Handling:** Gracefully handles non-existent or corrupted data files.

## Installation

To set up and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/nutnell/python-cli-todo-app.git](https://github.com/nutnell/python-cli-todo-app.git)
    cd python-cli-todo-app
    ```
    

2.  **Create and activate a Python virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    venv\Scripts\activate.bat
    ```

3.  **No external dependencies:** This project uses only Python's standard library. No `pip install` commands are necessary beyond `pip install --upgrade pip` for good measure.

## Usage

Once installed and the virtual environment is activated, you can run the application using `python app.py` followed by the desired command and its arguments.

**General Help:**
```bash
python app.py --help
