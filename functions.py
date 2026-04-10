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
    display_task(tasks)


def delete_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available!")
        return
    removing_task = get_input_num(tasks, "Enter deleting task number: ")
    tasks.pop(removing_task)
    save_tasks(tasks)
    print("Task removed!")

def mark_complete():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available!")
        return
    marking_task = get_input_num(tasks, "Enter Completing task number: ")
    tasks[marking_task]["status"] = "Complete"
    save_tasks(tasks)
    print("Task Completed!")

def get_input_num(selections, question):
    entered_num = input(question)
    try:
        entered_num = int(entered_num)
    except ValueError:
        print("Invalid input!")
        return get_input_num(selections, question)

    if entered_num > len(selections) or entered_num <= 0:
        print("Invalid input!")
        return get_input_num(selections, question)
    else:
        return entered_num - 1

def search_from_keyword():
    search_result = []
    search_word = input("Enter keyword: ").lower()
    tasks = load_tasks()
    for task in tasks:
        for key,item in task.items():
            if key == "status":
                continue
            if search_word in item.lower():
                search_result.append(task)
                break

    display_task(search_result)



def filter_func():
    all_filters = ["Complete","Incomplete"]
    filtered_list = []
    tasks = load_tasks()
    filter_num = get_input_num(all_filters, "Select Filter,\n[1] Complete \n[2] Incomplete\nSelect: ")
    for task in tasks:
        if task["status"] == all_filters[filter_num]:
            filtered_list.append(task)
    display_task(filtered_list)

def edit_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available!")
        return
    editing_task_num = get_input_num(tasks,"Enter task number for edit: ")
    print("Keep typing area empty if no change is required")
    new_title = input("Enter new title: ")
    new_description = input("Enter new description: ")

    if len(new_title) > 0:
        tasks[editing_task_num]["title"] = new_title
    if len(new_description)> 0:
        tasks[editing_task_num]["description"] = new_description
    print("Changes saved!")
    save_tasks(tasks)

def display_task(tasks):
    if tasks:
        for num,task in enumerate(tasks):
            print(f"\n[{num + 1}] {task['title']}")
            print(f"    Description: {task['description']}")
            print(f"    Status: {task['status']}")
    else:
        print("No tasks available!")