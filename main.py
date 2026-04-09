print("Welcome TO Task Manager\n")

choices = {1:"Add Task",2:"View Task",3:"Delete Task",4:"Mark Task as Complete"}

def display_menu():
    for num in choices:
        print(num,choices[num])
    print("\n")

def get_choice(question):
    try:
        choice_num = int(input(question))
    except ValueError:
        print("Invalid Input")
        return get_choice(question)
    return choice_num

display_menu()
n = get_choice("Enter Number: ")
print(n)