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
    for num,task in enumerate(tasks):
        print()
        print(f"Task #{num+1}")
        print("Title:",task["title"])
        print("Description:",task["description"])
        print("Status:",task["status"])

def delete_task():
    removing_task = int(input("Enter removing task number: ")) - 1
    tasks = load_tasks()
    tasks.pop(removing_task)
    save_tasks(tasks)
    print("Task removed!")

def mark_complete():
    marking_task = int(input("Enter Completing task number: ")) - 1
    tasks = load_tasks()
    tasks[marking_task]["status"] = "Complete"
    save_tasks(tasks)
    print("Task Completed!")

