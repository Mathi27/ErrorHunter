class TodoList:
    def __init__(self):
        self.tasks = set()

    def add_task(self, task):
        self.tasks.add(task)
        print(f"Task '{task}' added.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed.")
        else:
            print(f"task'{task}'not found in the list")

    def display_tasks(self):
        if self.tasks:
            print("your task:")
            for task in self.tasks:
                print(f"- {task}")
        else:
            print("no task in the list")

 
todo = TodoList()
todo.add_task("Complete Python project")
todo.add_task("Read a book")
todo.display_tasks()
todo.remove_task("Exercise")  
