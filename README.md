# task-tracker-cli
CLI app to track your tasks and manage your to-do list.

https://roadmap.sh/projects/task-tracker

# Python Task Management Application

This Python application allows you to manage a list of tasks stored in a JSON file. You can perform various operations on your tasks, such as adding, updating, deleting, marking as in progress, marking as done, or listing them in different states.

### Features
- **Add a Task**
- **Update a Task**
- **Delete a Task**
- **Mark a Task as In Progress**
- **Mark a Task as Done**
- **List Tasks** (filter by status: `all`, `todo`, `done`, `in-progress`)

### Requirements
- Python 3.x
- `tasks.json` file (included in the repository)

The `tasks.json` file should have the following structure:

```json
{
  "tasks": [
    {
      "id": 1,
      "desc": "Sample task description",
      "status": "todo",
      "createdAt": "2025-03-16T12:34:56",
      "updatedAt": "2025-03-16T12:34:56"
    }
  ]
}
```

### Setup
1. **Clone the repository** or **download the script** and place it in a directory of your choice.
2. Ensure that the `tasks.json` file is present in the same directory as the script.
3. The script will automatically load and save tasks to `tasks.json` on each execution.

### Usage

You can interact with this application via command-line arguments. Below are the available options:

#### 1. **Add a Task**

To add a new task to the list:

```bash
python script.py --add "Task description"
```

Example:
```bash
python script.py --add "Buy groceries"
```

This will add a task with the status `todo`.

#### 2. **Update a Task**

To update the description of an existing task, use the following command:

```bash
python script.py --update "<task_id> <new_description>"
```

Example:
```bash
python script.py --update "1 Buy fresh fruits"
```

This will update task with ID 1, changing its description to "Buy fresh fruits".

#### 3. **Delete a Task**

To delete a task by its ID, use:

```bash
python script.py --delete <task_id>
```

Example:
```bash
python script.py --delete 1
```

This will delete the task with ID 1.

#### 4. **Mark Task as Done**

To mark a task as `done`:

```bash
python script.py --mark-done <task_id>
```

Example:
```bash
python script.py --mark-done 1
```

This will mark the task with ID 1 as `done`.

#### 5. **Mark Task as In Progress**

To mark a task as `in-progress`:

```bash
python script.py --mark-in-progress <task_id>
```

Example:
```bash
python script.py --mark-in-progress 1
```

This will mark the task with ID 1 as `in-progress`.

#### 6. **List Tasks**

You can list tasks based on their status:

- **List all tasks**:

```bash
python script.py --list all
```

- **List tasks with `todo` status**:

```bash
python script.py --list todo
```

- **List tasks with `done` status**:

```bash
python script.py --list done
```

- **List tasks with `in-progress` status**:

```bash
python script.py --list in-progress
```

Example:
```bash
python script.py --list done
```

This will display all tasks with the `done` status.

### Error Handling
If the script encounters any issues with the provided arguments, it will print an error message.

For example:
- If you try to update a task with an invalid ID, you’ll see:
  ```bash
  An item with that I.D. does not exist.
  ```

- If you use an invalid argument format, you will be notified to check the README for correct usage.

### Notes
- The tasks are stored in the `tasks.json` file, and every operation (adding, updating, deleting, etc.) will automatically update the file.
- Task IDs are automatically generated and incremented when new tasks are added.
- The script handles task status changes (`todo`, `done`, `in-progress`).

### Example Usage

```bash
# Add a task
python script.py --add "Complete Python project"

# Update a task
python script.py --update "1 Update task description"

# Mark a task as in progress
python script.py --mark-in-progress 1

# List all tasks
python script.py --list all

# List tasks with "todo" status
python script.py --list todo

# Delete a task
python script.py --delete 1
```

### License
This project is open-source and available for modification and redistribution. Feel free to contribute!

