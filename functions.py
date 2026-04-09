def add_task():
    with open("tasks.txt","a") as f:
        task = input("Enter task title: ")
        description = input("Enter task description: ")
        f.write(f"{task},{description}\n")

def view_task():
    with open("tasks.txt","r") as f:
       tasks = f.readlines()
       num = 1
       for task in tasks:
            t = task.split(",")
            print(f"{num} {t[0]}  {t[1]}",end="")
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
