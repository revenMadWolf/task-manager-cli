import functions

print("Welcome TO Task Manager\n")

choices = {1:"Add Task",2:"View Task",3:"Delete Task",4:"Mark Task as Complete",5:"View menu",6:"Exit"}

def display_menu(options):
    for num in options:
        print(num,choices[num])
    print("\n")

def get_choice(question):
    try:
        choice_num = int(input(question))
    except ValueError:
        print("Invalid Input")
        return get_choice(question)
    return choice_num

display_menu(choices)

while True:
    choice = get_choice("Select an option: ")

    if choice == 1:
        functions.add_task()
    elif choice == 2:
        functions.view_task()
    elif choice == 3:
        functions.delete_task()
    elif choice == 4:
        functions.mark_complete()
    elif choice == 5:
        display_menu(choices)
    elif choice == 6:
        exit()