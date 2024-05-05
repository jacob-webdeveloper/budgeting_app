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


def view(filename):
    with open("goals.csv", "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            print(f"You have ${row[1]} remaining in you {row[0]} goal.")


    

    

