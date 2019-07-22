class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date

class TodoList:
    tasks = []
    def __init__(self):
        pass
    
    def add_task(self, new_task):
        self.tasks.append(new_task)


task1 = Task("Cook Food", "April 21, 2019")
task2 = Task("Do Laundry", "May 2, 2019")
task3 = Task("Eat", "June 19, 2019")

my_list = TodoList()
my_list.add_task(task1)
my_list.add_task(task2)
my_list.add_task(task3)