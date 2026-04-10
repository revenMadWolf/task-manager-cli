import functions

print("Welcome TO Task Manager\n")

choices = {
    1: "Add Task",
    2: "Edit Task",
    3: "View Task",
    4: "Delete Task",
    5: "Mark Task as Complete",
    6: "Search Task",
    7: "Filter Task",
    8: "View Menu",
    9: "Exit"
}
def display_menu(options):
    for num,option in options.items():
        print(f"({num})",option)
    print()

def get_choice(question):
    try:
        choice_num = int(input(question))
    except ValueError:
        print("Invalid Input!")
        return get_choice(question)
    return choice_num

display_menu(choices)

while True:
    print()
    choice = get_choice("Select an option: ")

    if choice == 1:
        functions.add_task()
    elif choice == 2:
        functions.edit_task()
    elif choice == 3:
        functions.view_task()
    elif choice == 4:
        functions.delete_task()
    elif choice == 5:
        functions.mark_complete()
    elif choice == 6:
        functions.search_from_keyword()
    elif choice == 7:
        functions.filter_func()
    elif choice == 8:
        display_menu(choices)
    elif choice == 9:
        print("Exiting...")
        break
    else:
        print("Invalid Input!")