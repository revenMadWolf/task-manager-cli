import json

def load_tasks(path="tasks.json"):
    try:
        with open(path,"r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Task file does not exist...")
        print("Creating file...")
        with open(path,"w") as f:
            print("File created!")
            json.dump([],f)
            return []

def save_tasks(tasks,path="tasks.json"):
    with open(path,"w") as f:
        json.dump(tasks,f,indent=4)

def add_task():
    task = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    tasks = load_tasks()
    tasks.append({"title":task,"description":description,"status":"Incomplete"})
    save_tasks(tasks)
    print("Task Added!")

def view_task():
    tasks = load_tasks()
    if len(tasks) == 0:
        print("No Tasks available!")
        return
    for num,task in enumerate(tasks):
        print(f"\n[{num + 1}] {task['title']}")
        print(f"    Description: {task['description']}")
        print(f"    Status: {task['status']}")

def delete_task():
    tasks = load_tasks()
    removing_task = get_task_num(tasks,"Enter deleting task number: ")
    tasks.pop(removing_task)
    save_tasks(tasks)
    print("Task removed!")

def mark_complete():
    tasks = load_tasks()
    marking_task = get_task_num(tasks,"Enter Completing task number: ")
    tasks[marking_task]["status"] = "Complete"
    save_tasks(tasks)
    print("Task Completed!")

def get_task_num(tasks,question):
    entered_num = input(question)
    try:
        entered_num = int(entered_num)
    except ValueError:
        print("Invalid input!")
        return get_task_num(tasks,question)

    if entered_num > len(tasks) or entered_num <= 0:
        print("Invalid input!")
        return get_task_num(tasks,question)
    else:
        return entered_num - 1

