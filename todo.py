import os

class TodoApp:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from file if it exists"""
        try:
            with open(self.filename, 'r') as file:
                self.tasks = [line.strip() for line in file.readlines() if line.strip()]
            print(f"Loaded {len(self.tasks)} tasks from {self.filename}")
        except FileNotFoundError:
            print(f"No existing task file found. Starting with empty list.")
            self.tasks = []
    
    def save_tasks(self):
        """Save tasks to file"""
        try:
            with open(self.filename, 'w') as file:
                for task in self.tasks:
                    file.write(task + '\n')
            print(f"Tasks saved to {self.filename}")
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def add_task(self, task):
        """Add a new task to the list"""
        if task.strip():
            self.tasks.append(task.strip())
            self.save_tasks()
            print(f"Task '{task}' added successfully!")
        else:
            print("Task cannot be empty!")
    
    def view_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("\nNo tasks found! Your to-do list is empty.")
            return
        
        print(f"\n--- Your To-Do List ({len(self.tasks)} tasks) ---")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
        print("-" * 40)
    
    def remove_task(self, task_number):
        """Remove a task by its number"""
        try:
            if 1 <= task_number <= len(self.tasks):
                removed_task = self.tasks.pop(task_number - 1)
                self.save_tasks()
                print(f"Task '{removed_task}' removed successfully!")
            else:
                print("Invalid task number!")
        except (ValueError, IndexError):
            print("Please enter a valid task number!")
    
    def remove_task_by_name(self, task_name):
        """Remove a task by its name"""
        task_name = task_name.strip().lower()
        for i, task in enumerate(self.tasks):
            if task.lower() == task_name:
                removed_task = self.tasks.pop(i)
                self.save_tasks()
                print(f"Task '{removed_task}' removed successfully!")
                return
        print(f"Task '{task_name}' not found!")
    
    def search_tasks(self, keyword):
        """Search for tasks containing a keyword"""
        keyword = keyword.strip().lower()
        matching_tasks = []
        
        for i, task in enumerate(self.tasks, 1):
            if keyword in task.lower():
                matching_tasks.append((i, task))
        
        if matching_tasks:
            print(f"\n--- Search Results for '{keyword}' ---")
            for task_num, task in matching_tasks:
                print(f"{task_num}. {task}")
            print("-" * 40)
        else:
            print(f"No tasks found containing '{keyword}'")
    
    def clear_all_tasks(self):
        """Clear all tasks"""
        if self.tasks:
            confirm = input(f"Are you sure you want to delete all {len(self.tasks)} tasks? (y/N): ")
            if confirm.lower() == 'y':
                self.tasks.clear()
                self.save_tasks()
                print("All tasks cleared!")
            else:
                print("Operation cancelled.")
        else:
            print("No tasks to clear!")
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*50)
        print("           TO-DO LIST MANAGER")
        print("="*50)
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Remove Task (by number)")
        print("4. Remove Task (by name)")
        print("5. Search Tasks")
        print("6. Clear All Tasks")
        print("7. Exit")
        print("="*50)
    
    def run(self):
        """Main application loop"""
        print("Welcome to your Personal To-Do List Manager!")
        
        while True:
            self.display_menu()
            
            try:
                choice = input("\nEnter your choice (1-7): ").strip()
                
                if choice == '1':
                    task = input("Enter new task: ")
                    self.add_task(task)
                
                elif choice == '2':
                    self.view_tasks()
                
                elif choice == '3':
                    self.view_tasks()
                    if self.tasks:
                        try:
                            task_num = int(input("Enter task number to remove: "))
                            self.remove_task(task_num)
                        except ValueError:
                            print("Please enter a valid number!")
                
                elif choice == '4':
                    self.view_tasks()
                    if self.tasks:
                        task_name = input("Enter task name to remove: ")
                        self.remove_task_by_name(task_name)
                
                elif choice == '5':
                    keyword = input("Enter keyword to search: ")
                    self.search_tasks(keyword)
                
                elif choice == '6':
                    self.clear_all_tasks()
                
                elif choice == '7':
                    print("\nThank you for using To-Do List Manager!")
                    print("Your tasks have been saved. Goodbye!")
                    break
                
                else:
                    print("Invalid choice! Please enter a number between 1-7.")
            
            except KeyboardInterrupt:
                print("\n\nProgram interrupted. Your tasks have been saved. Goodbye!")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

# Simple version for basic requirements
def simple_todo():
    """Simple version that meets the basic requirements"""
    tasks = []
    filename = "simple_tasks.txt"
    
    # Load existing tasks
    try:
        with open(filename, 'r') as file:
            tasks = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        pass
    
    while True:
        print("\n--- Simple To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose option (1-4): ")
        
        if choice == '1':
            task = input("Enter task: ")
            if task.strip():
                tasks.append(task.strip())
                # Save to file
                with open(filename, 'w') as file:
                    for t in tasks:
                        file.write(t + '\n')
                print("Task added!")
        
        elif choice == '2':
            if tasks:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks found!")
        
        elif choice == '3':
            if tasks:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    num = int(input("Enter task number to remove: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        # Save to file
                        with open(filename, 'w') as file:
                            for t in tasks:
                                file.write(t + '\n')
                        print(f"Removed: {removed}")
                    else:
                        print("Invalid number!")
                except ValueError:
                    print("Please enter a valid number!")
            else:
                print("No tasks to remove!")
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    print("Choose version:")
    print("1. Advanced To-Do App (Recommended)")
    print("2. Simple To-Do App (Basic)")
    
    version = input("Enter choice (1 or 2): ").strip()
    
    if version == '2':
        simple_todo()
    else:
        app = TodoApp()
        app.run() 
