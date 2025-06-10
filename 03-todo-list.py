import uuid

class Task:
    def __init__(self, name):
        self.id = uuid.uuid4().hex[:6]
        self.name = name
        self.done = False


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def done_task(self, task_id: str):
        for task in self.tasks:
            if task.id == task_id:
                task.done = not task.done

    def remove_task(self, task_id: str):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)

    def show_tasks(self):
        for task in self.tasks:
            print(f"\n the homework {task.name} - {'Hecho' if task.done else 'No hecho'}({task.id})")


print("""
==== TODO LIST ====

Enter a task name: Example: homework, project, etc.

==== TODO LIST ====
\n""")

name = input("\nEnter a task name: ")
task = Task(name)
todo_list = TodoList()
todo_list.add_task(task)
todo_list.show_tasks()

while True:
    print("\n\n==== TODO LIST ====\n")
    print("1. Add task")
    print("2. Remove task")
    print("3. Done task")
    print("4. Show tasks")
    print("5. Exit")
    option = input("\nChoose an option: ")
    match option:
        case "1":
            name = input("\nEnter a task name: ")
            task = Task(name)
            todo_list.add_task(task)
        case "2":
            task_id = input("\nEnter a task id: ")
            todo_list.remove_task(task_id)
        case "3":
            task_id = input("\nEnter a task id: ")
            todo_list.done_task(task_id)
        case "4":
            todo_list.show_tasks()
        case "5":
            break