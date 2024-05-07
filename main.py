import os.path

from colored import Fore, Back, Style

from functions import add_goal, goal_progress, view_goal, add_expense, remove_expense, view_expense

print(f"{Back.dark_blue}{Fore.cyan + 'Welcome to your budgeting app'}")

def create_menu():
    print("1. Enter 1 to set a savings goal")
    print("2. Enter 2 to add progress towards a savings goal")
    print("3. Enter 3 to view savings goals")
    print("4. Enter 4 to add expenses")
    print("5. Enter 5 to remove expenses")
    print("6. Enter 6 to view expenses")
    print("7. Enter 7 to exit")

    user_choice = input("Enter your selection: ")
    return user_choice

choice = ""

while choice != "7":
    choice = create_menu()

    if (choice == "1"):
        if (not os.path.isfile("goals.csv")):
            goals_file = open("goals.csv", "w")
            goals_file.write("Goal,Amount\n")
            goals_file.close()
        add_goal("goals.csv")

    elif choice == "2":
        if (not os.path.isfile("goals.csv")):
            print("No goals in progress")
        else:
            (os.path.isfile("goals.csv"))
            goal_progress("goals.csv")

    elif choice == "3":
        if (not os.path.isfile("goals.csv")):
            print("No goals in progress")
        else:
            view_goal("goals.csv")

    elif choice == "4":
        if (not os.path.isfile("expenses.csv")):
            goals_file = open("expenses.csv", "w")
            goals_file.write("Expense,Amount\n")
            goals_file.close()
        add_expense("expenses.csv")

    elif choice == "5":
        if (not os.path.isfile("expenses.csv")):
            print("No expenses yet")
        else:
            remove_expense("expenses.csv")

    elif choice == "6":
        if (not os.path.isfile("expenses.csv")):
            print("No expenses yet")
        else:
            view_expense("expenses.csv")

    elif choice == "7":
        print("You have selected 7")
    else:
        print("Please only enter the options shown above.")


print("Thankyou for using the budgeting app")