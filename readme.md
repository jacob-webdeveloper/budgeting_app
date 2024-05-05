### Features of App
my plan is to create a budgeting app. It will allow you to set certain goals to save towards and you will be able to add/remove expenses and assign them into different categories.

**Feature 1**
To be able to set savings goals that you can work towards

**Feature 2**
To be able to add expenses that you spent and add them to a category

**Feature 3**
To be able to remove expenses that you refunded etc.

**Feature 4**
To be able to view the expenses in a certain category.

if (not os.path.isfile(file_name)):
    print("Creating file as it doesn't exist")
    # Create the file
    todo_file = open(file_name, "w")
    # we will enter the headings into the file
    todo_file.write("title,completed\n")
    # Close the file
    todo_file.close()