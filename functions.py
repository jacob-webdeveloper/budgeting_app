import csv

def add_goal(filename):
    goal = input("Enter a Budgeting Goal: ")
    amount = input("Enter the amount of savings needed: ")
    with open("goals.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([goal, amount])


    

    

