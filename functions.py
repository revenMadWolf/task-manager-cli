def add_task():
    with open("tasks.txt","a") as f:
        task = input("Enter task title: ")
        description = input("Enter task description: ")
        f.write(f"{task},{description},Incomplete\n")

def view_task():
    with open("tasks.txt","r") as f:
       tasks = f.readlines()
       num = 1
       for task in tasks:
            t = task.split(",")
            print(f"{num} {t[0]}  {t[1]}  {t[2]}",end="")
            num += 1

def delete_task():
    view_task()
    removing_task = int(input("Enter removing task number: ")) - 1
    with open("tasks.txt","r+") as f:
        tasks = f.readlines()
        tasks.pop(removing_task)
    with open("tasks.txt","w") as f:
        f.writelines(tasks)
    print("Task removed!")

def mark_complete():
    view_task()
    marking_task = int(input("Enter Completing task number: ")) - 1
    with open("tasks.txt","r+") as f:
        tasks = f.readlines()
        complete_task = tasks[marking_task]
        t = complete_task.split(",")
        t[2] = "complete"
        complete_task = f"{t[0]},{t[1]},{t[2]}\n"
        tasks[marking_task] = complete_task
    with open("tasks.txt","w") as f:
        f.writelines(tasks)
    print("Task Completed!")
