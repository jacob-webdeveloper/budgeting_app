import csv

def add_goal(filename):
    goal = input("Enter a Budgeting Goal: ")
    amount = input("Enter the amount of savings needed: ")
    with open("goals.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([goal, amount])

def goal_progress(filename):
    with open("goals.csv", "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            print(f"Your {row[0]} has {row[1]} dollars remaining")

    

    

