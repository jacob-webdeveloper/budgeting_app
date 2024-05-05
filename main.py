
print("Welcome to your budgeting app")

def create_menu():
    print("1. Enter 1 to set a savings goal")
    print("2. Enter 2 to add progress towards a savings goal")
    print("3. Enter 3 to add expenses")
    print("4. Enter 4 to remove expenses")
    print("5. Enter 5 to view expenses")
    print("6. Enter 6 to exit")

    user_choice = input("Enter your selection: ")
    return user_choice

choice = ""

while choice != "6":
    choice = create_menu()

    if (choice == "1"):
        print("You have selected 1")
    elif choice == "2":
        print("You have selected 2")
    elif choice == "3":
        print("You have selected 3")
    elif choice == "4":
        print("You have selected 4")
    elif choice == "5":
        print("You have selected 5")
    elif choice == "6":
        print("You have selected 6")
    else:
        print("Please only enter the options shown above.")


print("Thankyou for using the budgeting app")