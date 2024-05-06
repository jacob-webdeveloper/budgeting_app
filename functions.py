import csv

def add_goal(filename):
    goal = input("Enter a Budgeting Goal: ")
    amount = int(input("Enter the amount of savings needed: "))
    with open("goals.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([goal, amount])



def goal_progress(filename):
    with open("goals.csv", "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            print(f"Your {row[0]} has {row[1]} dollars remaining")
    
    goal_name = input("Enter the goal that you want to add progress towards: ")
    amount_progress = int(input(f"Enter the amount that you want to put towards {goal_name}: "))
    
    goal_lists = []
    with open("goals.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if goal_name != row[0]:
                goal_lists.append(row)
            else:
                original_value = int(row[1])
                new_value = original_value - amount_progress
                goal_lists.append([row[0], int(new_value)])

    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerows(goal_lists)


def view_goal(filename):
    with open("goals.csv", "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            print(f"You have ${row[1]} remaining in you {row[0]} goal.")


def add_expense(filename):
    
    expense = input("Enter what you spent the money on: ")
    amount_spent = int(input(f"Enter the amount that you spent on {expense}: "))

    with open("expenses.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([expense, amount_spent])


def remove_expense(filename):
    expenses_list = []
    with open("expenses.csv", "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            print(f"You spent ${row[1]} on {row[0]}")
        rm_expense = input("What expense would you like to remove?")
    
    with open("expenses.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if rm_expense != row[0]:
                expenses_list.append(row)
    
    with open("expenses.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(expenses_list)
                

def view_expense(filename):
    with open("expenses.csv", "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            print(f"Spent ${row[1]} on {row[0]}")

    

    


    

    

