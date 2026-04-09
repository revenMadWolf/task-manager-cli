def load_tasks(path="tasks.txt"):
    with open(path,"r") as f:
        return f.readlines()

def save_tasks(tasks,path="tasks.txt"):
    if tasks is None:
        tasks = []
    with open(path,"w") as f:
        f.writelines(tasks)

def add_task():
    task = input("Enter task title: ")
    description = input("Enter task description: ")
    tasks = load_tasks()
    tasks.append(f"{task},{description},[Incomplete]\n")
    save_tasks(tasks)
    print("Task Added!")

def view_task():
    tasks = load_tasks()
    num = 0
    for task in tasks:
        num += 1
        print(f"({num})",end=" ")
        t = task.strip()
        t = t.split(",")
        for item in t:
            print(item.strip(),end=" | ")
        print()

def delete_task():
    removing_task = int(input("Enter removing task number: ")) - 1
    tasks = load_tasks()
    tasks.pop(removing_task)
    save_tasks(tasks)
    print("Task removed!")

def mark_complete():
    marking_task = int(input("Enter Completing task number: ")) - 1
    tasks = load_tasks()
    complete_task = tasks[marking_task].replace("[Incomplete]","[Complete]")
    tasks[marking_task] = complete_task
    save_tasks(tasks)
    print("Task Completed!")

