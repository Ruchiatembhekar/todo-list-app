# To-Do List Application

A simple console-based to-do list manager built with Python for the Python Developer Internship.

## Features

### Basic Features (Meeting Requirements)
- ✅ Add new tasks
- ✅ View all tasks  
- ✅ Remove tasks
- ✅ Persistent storage using text files
- ✅ File handling with proper context managers

### Advanced Features (Bonus)
- 🔍 Search tasks by keyword
- 🗑️ Remove tasks by number or name
- 🧹 Clear all tasks option
- 💾 Auto-save functionality
- 🛡️ Error handling and input validation
- 📊 Task counter display

## How to Run

1. Make sure you have Python installed on your system
2. Download the `todo.py` file
3. Open terminal/command prompt
4. Navigate to the folder containing `todo.py`
5. Run the command:
   ```bash
   python todo.py
   ```

## Usage

When you run the application, you'll see a menu with the following options:

1. **Add Task** - Add a new task to your list
2. **View All Tasks** - Display all current tasks with numbers
3. **Remove Task (by number)** - Remove a specific task using its number
4. **Remove Task (by name)** - Remove a task by typing its exact name
5. **Search Tasks** - Find tasks containing specific keywords
6. **Clear All Tasks** - Remove all tasks (with confirmation)
7. **Exit** - Save and quit the application

## File Storage

- Tasks are automatically saved to `tasks.txt` in the same directory
- The file is created automatically if it doesn't exist
- Tasks persist between program runs

## Technical Implementation

### Key Concepts Covered:
- **File Handling**: Using `open()`, `with` statements, and context managers
- **Lists**: Using `append()`, `pop()`, `insert()`, and list comprehensions
- **String Manipulation**: Using `.strip()`, `.lower()`, and string formatting
- **Error Handling**: Try-catch blocks for file operations and user input
- **Data Structures**: Lists for storing tasks, enumeration for numbering

### Interview Questions Addressed:

1. **File Operations**: Uses `open()` with context managers (`with` statement)
2. **File Modes**: Implements both read ('r') and write ('w') modes
3. **String Methods**: Uses `.strip()` to remove whitespace from input and file lines
4. **List Operations**: Demonstrates `append()`, `pop()`, `insert()`, and indexing
5. **Context Managers**: All file operations use `with` statements for proper resource management
6. **File Processing**: Implements line-by-line file reading with proper handling
7. **Error Handling**: Handles FileNotFoundError when file doesn't exist

## Code Structure

```
TodoApp Class:
├── __init__()          # Initialize and load tasks
├── load_tasks()        # Load tasks from file
├── save_tasks()        # Save tasks to file  
├── add_task()          # Add new task
├── view_tasks()        # Display all tasks
├── remove_task()       # Remove by number
├── remove_task_by_name() # Remove by name
├── search_tasks()      # Search functionality
├── clear_all_tasks()   # Clear all tasks
├── display_menu()      # Show menu options
└── run()              # Main application loop
```

## Example Usage

```
Welcome to your Personal To-Do List Manager!

==================================================
           TO-DO LIST MANAGER
==================================================
1. Add Task
2. View All Tasks
3. Remove Task (by number)
4. Remove Task (by name)  
5. Search Tasks
6. Clear All Tasks
7. Exit
==================================================

Enter your choice (1-7): 1
Enter new task: Buy groceries
Task 'Buy groceries' added successfully!
Tasks saved to tasks.txt
```

## Learning Outcomes

This project demonstrates:
- Practical file I/O operations
- List manipulation and management
- User input validation and error handling
- Menu-driven console application development
- Code organization with classes and methods
- Persistent data storage

---
