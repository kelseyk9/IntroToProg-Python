# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Kelsey Kawaguchi,11.06.2019,Added code to complete assignment 05
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
strLine = ""  # A string of data to be removed from the list
strID = "" # A string of data ID to represent task priority
strTask = "" # A string of data to represent the task
strChoice = "" # A Capture the user option selection
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
lstRow = () # All of the rows



# -- Processing and Input/Output -- #
# Step 1 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 2 - Load any data you have in a text file called ToDoList.txt 
    #Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Open file to read
        objFile = open(strFile,"r")
        for row in objFile:
            lstRow = row.strip()
            print(lstRow)
        continue
    # Step 3 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: open file to write then add info
        objFile = open(strFile,"a")
        strID = input("Enter task priority: ")
        strTask = input("Enter task to complete: ")
        dicRow = {"Priority":strID,"Task":strTask}
        lstTable.append(dicRow)
        continue
    # Step 4 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Open the file, then remove row of data
        strLine = input("Identify which task or priority you want to remove: ")    
        with open(strFile,"r+") as objFile:
            new_objFile = objFile.readlines()
            objFile.seek(0)
            for line in new_objFile:
                if strLine not in line:
                    objFile.write(line)
            objFile.truncate()
        continue
    # Step 5 - Save tasks to file
    elif (strChoice.strip() == '4'):
        # TODO: save data file
        objFile = open(strFile,"a")
        for row in lstTable:
            objFile.write("\n"+ row['Priority'] + "," + row['Task'].strip())
        objFile.close
        print("Data is now saved!")
        continue
    # Step 6 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Exit the program
        print("End of Session")
        break  
