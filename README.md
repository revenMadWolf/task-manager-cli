# Task Manager CLI

A command-line task manager built in Python that allows users to efficiently manage tasks using a simple terminal interface.

This project demonstrates core programming concepts such as file handling, data structures, modular design, and user input validation.

---

## Features

* Add new tasks
* View all tasks
* Edit existing tasks
* Delete tasks
* Mark tasks as complete
* Search tasks by keyword
* Filter tasks by status (Complete / Incomplete)
* Persistent storage using JSON

---

## How to Run

1. Make sure Python is installed on your system
2. Clone this repository:

   ```
   git clone <your-repository-link>
   ```
3. Navigate to the project folder:

   ```
   cd task-manager-cli
   ```
4. Run the program:

   ```
   python main.py
   ```

---

## Example Usage

```
(1) Add Task
(2) Edit Task
(3) View Task
(4) Delete Task
(5) Mark Task as Complete
(6) Search Task
(7) Filter Task
(8) View Menu
(9) Exit

Select an option: 1
Enter task title: Study Programming
Enter task description: Practice Python daily
Task Added!
```

---

## Project Structure

* `main.py` — Handles user interaction and menu system
* `functions.py` — Contains core logic and task operations
* `tasks.json` — Stores task data persistently

---

## Data Format (JSON)

Tasks are stored in the following format:

```json
[
    {
        "title": "Study Programming",
        "description": "Practice Python daily",
        "status": "Incomplete"
    }
]
```

---

## Future Improvements

* Add task priorities (High / Medium / Low)
* Add due dates for tasks
* Convert to a graphical user interface (GUI)
* Refactor into an object-oriented design (OOP)

---

## Author

* Thisew Basnayake
