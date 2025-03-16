# task-tracker-cli
CLI app to track your tasks and manage your to-do list.

https://roadmap.sh/projects/task-tracker

**Example**
The list of commands and their usage is given below:

# Adding a new task
```task-cli add "Buy groceries"```
**Output: Task added successfully (ID: 1)**

# Updating and deleting tasks
```
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1
```

# Marking a task as in progress or done
```
task-cli mark-in-progress 1
task-cli mark-done 1
```

# Listing all tasks
```
task-cli list
```

# Listing tasks by status
```
task-cli list done
task-cli list todo
task-cli list in-progress
```

# Task Properties
**Each task should have the following properties:**

id: A unique identifier for the task
description: A short description of the task
status: The status of the task (todo, in-progress, done)
createdAt: The date and time when the task was created
updatedAt: The date and time when the task was last updated
