# Documentation Requirements

### Requirement 3 - References
1. https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
2. https://pypi.org/project/colored/
3. https://www.geeksforgeeks.org/os-path-module-python/
4. https://peps.python.org/pep-0008/

### Requirement 4 - Link to Github
1. https://github.com/jacob-webdeveloper/budgeting_app

### Requirement 5 - Style Guide
- The style guide that I tried to stick to is 'PEP 8'.

### Requirement 6 - Features
There are 8 options/features in my budgeting app.
1. The first feature is to set a savings goal. The first step this feature does is check if a goals.csv file exists, if it doesn't exist, it will create the file and add a title for each column in the top row. If the file does exist then it executes the function add_goal. This function will ask for a goal input and an amount input. Then it will open the goals.csv file and enter the two inputs into the appropriate columns.

2. The second feature is to add progress towards a savings goal. It will first check if the goals.csv file exists. If it does exist then it will open the file and display the current savings goals for the user to choose from. Once the user chooses a goal then the user chooses a dollar amount that they have saved for that particular goal. That amount will then be minused from the total amount left to save. 

3. The third feature is to remove a goal. It will first check if the goals.csv file exists. If it does exist then it will open the file and display the current savings goals for the user to choose from. The user can then choose a goal that they wish to remove, the goal will then be removed from the csv file.

4. The fourth feature is to view the goals in progress. It will first check if the goals.csv file exists. If it does exist then it will open the file and display the current savings goals for the user to view without editing them.

5. The fifth feature is to add an expense. The first step this feature does is check if an expenses.csv file exists, if it doesn't exist, it will create the file and add a title for each column in the top row. If the file does exist then it executes the function add_expense. The function will execute 2 input fields one for the type of expense and a second for the dollar amount spent. The 2 values will then be added under the appropriate columns in the csv file.

6. The sixth feature is to remove an expense from the expenses.csv file. It will first check if the expenses.csv file exists. If it does exist then it will open the file and display the current expenses for the user to choose from. The user can then choose an expense that they wish to remove, the expenses will then be removed from the csv file.

7. The seventh feature is to view the expenses. It will first check if the expenses.csv file exists. If it does exist then it will open the file and display the current expenses for the user to view without editing them. There is also the additional function that it will add up the total of the expenses and display them at the bottom.

8. The eighth feature is simply to exit the app.

## Requirement 7 - Planning
1. Trello Board Starting the project
![First Stage of Development](<docs/Screenshot 2024-05-08 at 8.44.04 pm.png>)

2. Trello Board Mid way throught the project
![Mid Point of Development](<docs/Screenshot 2024-05-08 at 8.44.32 pm.png>)

3. Trello Board at end of project
![End point of development](<docs/Screenshot 2024-05-08 at 8.44.48 pm.png>)

## Requirement 8 - How to use Application
1. To install the application the repository will have to be cloned onto a local directory.
2. The user will have to ensure that they are running a modern version of Python, preferably Python 3.9 or newer. 
3. The user will have to navigate to the local directory that the repository has been cloned in and run the following commands.
4. chmod +x run.sh
5. ./run.sh
6. From here program will automatically start running.

