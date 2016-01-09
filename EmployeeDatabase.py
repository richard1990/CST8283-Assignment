##########################################################
# CST8333 2015F Final Project - EmployeeDatabase.py      #
#                                                        #
# Created by Richard Barney                              #
# November 30, 2015                                      #
# This module allows one to add, modify, or delete       #
# employees from a database. Users can also view all     #
# employees in the database.                             #
#                                                        #
##########################################################
# import statements
from Programmer import Programmer
from Executive import Executive
from datetime import date
from random import randint
# import MySQL Connector/Python, "a standardized database 
# driver for Python platforms and development", downloaded
# from Oracle's website at http://dev.mysql.com/downloads/connector/python/
import mysql.connector

# list to hold the employees, kept outside the function
# below to use with unit testing
listEmployees = []

# the function below is taken from an answer provided to 
# Stack Overflow to stop a Python module from being
# executed when imported into another module/class, I
# did this so stop the whole program from running when the
# EmployeeDatabaseTest class imports this module.
# user166390. (2011, June 29). Why is Python running my 
#    module when I import it, and how do I stop it? [Webpage].
#    Retrieved from http://stackoverflow.com/a/6523852.
def main():
    pass
if __name__ == "__main__":
    # list to hold the employee IDs to prevent duplicates
    employeeIDArr = []
    # menu options initialized with garbage value
    menuOption = "n"
    secondMenuOption = "n"
    # boolean to assist with input validation
    validateInputBoolean = True
    # obtain today's date with date object
    todaysDate = date.today()
    # String header used when displaying employees and when writing to file
    sHeader = "Employee ID\tFull name\t\tBirthday\tStart date\tWeekly pay\tWeekly tax"
    # db's name is employees
    DB_NAME = 'employees'
    # setup the connection and create the cursor
    cnx = mysql.connector.connect(user='scott', password='tiger', host='127.0.0.1')
    cursor = cnx.cursor()
    
    # create database first
    try:
        print("Creating the MySQL database...")
        cursor.execute("DROP DATABASE IF EXISTS " +DB_NAME)
        cursor.execute("CREATE DATABASE " +DB_NAME)
        cursor.execute("USE " +DB_NAME)
        cnx.database = DB_NAME
        # create positions table
        cursor.execute("CREATE TABLE Positions ("
                        "posID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                        "posName VARCHAR(30) NOT NULL"
                        ")")
        # create employee table
        cursor.execute("CREATE TABLE Employees ("
                        "empID INT NOT NULL PRIMARY KEY,"
                        "firstName VARCHAR(30) NOT NULL,"
                        "lastName VARCHAR(30) NOT NULL,"
                        "birthDate VARCHAR(10) NOT NULL,"
                        "startDate VARCHAR(10) NOT NULL,"
                        "weeklyPay VARCHAR(10) NOT NULL,"
                        "weeklyTax VARCHAR(10) NOT NULL,"
                        "posID INT NOT NULL,"
                        "FOREIGN KEY (posID) REFERENCES Positions(posID)"
                        ")")
        # insert data into the Positions table
        cursor.execute("INSERT INTO Positions(posName) VALUES('Programmer')")
        cursor.execute("INSERT INTO Positions(posName) VALUES('Executive')")    
        print("Database created.\n")
    # code for this except statement was taken from Oracle's official
    # exception documentation for MySQL Connector/Python.
    # Oracle. (2015). 10.12.2 Exception errors.Error. [Webpage]. Retrieved
    #    from https://dev.mysql.com/doc/connector-python/en/connector-python-api-errors-error.html.
    except mysql.connector.Error as ex:
        print("Something went wrong: {}".format(ex))
        
    print("Welcome to the Employee Database!")
    while menuOption != "0":
        menuOption = input("Enter:\n\t1 to add an employee"
                           +"\n\t2 to modify an employee"
                           +"\n\t3 to delete an employee"
                           +"\n\t4 to display all employees"
                           +"\n\t0 to quit\n")
        # 1 adds an employee
        if menuOption == "1":        
            # get the first and last name as Strings
            firstName = input("Enter the employee's first name: ")
            lastName = input("Enter the employee's last name: ")
            # while validateInputLoop is True, keep asking the user to
            # enter the a valid birth year
            while validateInputBoolean:
                # validate input by exception handling using 'try' and 'except'
                try:
                    birthYear = input("Enter the year the employee was born: ")
                    # set validateInputLoop to False if input was valid
                    validateInputBoolean = False
                    # ask user to re-enter birth year if it is less than 1900 or
                    # if employee is less than 17 years old
                    while int(birthYear) < 1900 or (todaysDate.year - int(birthYear)) < 17:
                        birthYear = input("Invalid input - Please re-enter the year the employee was born: ")
                        # set validateInputLoop to False if input was valid
                        validateInputBoolean = False
                except ValueError:
                    print("ERROR - invalid input!")
                    validateInputBoolean = True
            # set validateInputBoolean to True again for re-validation of input
            validateInputBoolean = True
            
            # while validateInputLoop is True, keep asking the user to
            # enter the employee's birth month as a number between 1
            # and 12 to ensure the user is entering a valid integer
            # and not a String
            while validateInputBoolean:
                # validate input by exception handling using 'try' and 'except'
                try:
                    birthMonth = input("Enter the month the employee was born (1-12): ")
                    # set validateInputLoop to False if input was valid
                    validateInputBoolean = False
                    # if the number entered by user is less than 1 or greater than
                    # 12, ask user to enter input again using built-in function int()
                    while int(birthMonth) < 1 or int(birthMonth) > 12:
                        birthMonth = input("Invalid input - Please re-enter the month the employee was born (1-12): ")
                        # set alidateInputLoop to False if input was valid
                        validateInputBoolean = False
                # if the user did not enter a number, display error message
                # and set validateInputLoop to True and ask for input again
                except ValueError:
                    print("ERROR - invalid input!")
                    validateInputBoolean = True
            # if month is <10 add a 0
            if int(birthMonth) < 10:
                birthMonth = "0" +str(birthMonth)
            # set validateInputBoolean to True again for re-validation of input
            validateInputBoolean = True
            
            # while validateInputLoop is True, keep asking the user to
            # enter the day the employee was born
            while validateInputBoolean:
                # validate input by exception handling using 'try' and 'except'
                try:
                    birthDay = input("Enter the day the employee was born (1-31): ")
                    # set validateInputLoop to False if input was valid
                    validateInputBoolean = False
                    # keep asking the user to re-enter the birth day if
                    # the number entered by user is less than 1 or greater than
                    # 12, or if the day entered does not correspond to the month
                    # (e.g. entering 30 for February or 29 when February of the year
                    # the employee was born only had 28 days)
                    while int(birthDay) < 1 or ((int(birthMonth) == 1 or int(birthMonth) == 3
                        or int(birthMonth) == 5 or int(birthMonth) == 7
                        or int(birthMonth) == 8 or int(birthMonth) == 10
                        or int(birthMonth) == 12) and int(birthDay) > 31) or ((int(birthMonth) == 4
                        or int(birthMonth) == 6 or int(birthMonth) == 9 or int(birthMonth) == 11)
                        and int(birthDay > 30)) or ((int(birthMonth) == 2 and int(birthYear) % 4 != 0) and
                        int(birthDay) > 28) or ((int(birthMonth) == 2 and int(birthYear) % 4 == 0) and
                        int(birthDay) > 29):
                        birthDay = input("Invalid input - Please re-enter the day the employee was born (1-31): ")
                        # set validateInputLoop to False if input was valid
                        validateInputBoolean = False
                # if the user did not enter a number, display error message
                # and set validateInputLoop to True and ask for input again
                except ValueError:
                    print("ERROR - invalid input.")
                    validateInputBoolean = True
            # if day is <10 add a 0
            if int(birthDay) < 10:
                birthDay = "0" +str(birthDay)
            # set validateInputBoolean to True again for re-validation of input
            validateInputBoolean = True
        
            # generate a random number between 1 and 99999 inclusive and make sure
            # it does not already exist in the array of employee IDs, and if it does
            # generate a new employee ID, makes use of the random module method
            # randint that generates a random integer between the range entered, inclusive
            randomNum = randint(1, 99999)
            for i in range(len(employeeIDArr)):
                while employeeIDArr[i] == randomNum:
                    randomNum = randint(1, 99999)
            
            # if the employee ID has less than 5 digits, pad it with zeroes, then
            # add it to the array of employee IDs
            employeeID = str('%05d' % randomNum)
            employeeIDArr.append(employeeID)
            
            # loop to ask user if the employee is a programmer or executive
            while True:
                secondMenuOption = input("Enter:\n\t1 to add an executive"
                                         +"\n\t2 to add a programmer\n")
            
                # if employee is an executive, get the executive's yearly salary
                if secondMenuOption == "1":
                    while validateInputBoolean:
                        try:
                            yearlySalary = input("Enter the executive's yearly salary: ")
                            # set validateInputLoop to False if input was valid
                            validateInputBoolean = False
                            while int(yearlySalary) < 1:
                                yearlySalary = input("Invalid input - Enter a valid yearly salary: ")
                                # set validateInputLoop to False if input was valid
                                validateInputBoolean = False
                        except ValueError:
                            print("ERROR - invalid input.")
                            validateInputBoolean = True
                            
                    newEmployee = Executive(employeeID, firstName, lastName, birthYear, birthMonth,
                                            birthDay, str(todaysDate), yearlySalary)
                    break
                
                # if employee is a programmer, get the programmer's weekly hours
                # worked and hourly rate of pay
                if secondMenuOption == "2":
                    while validateInputBoolean:
                        # get hours worked
                        try:
                            hoursWorked = input("Enter the amount of hours employee will be working per week: ")
                            # set validateInputLoop to False if input was valid
                            validateInputBoolean = False
                            while int(hoursWorked) < 5:
                                hoursWorked = input("Invalid input - Enter a valid amount of hours: ")
                                # set validateInputLoop to False if input was valid
                                validateInputBoolean = False
                        except ValueError:
                            print("ERROR - invalid input.")
                            validateInputBoolean = True
                            
                    # set validateInputBoolean to True again for data validation
                    validateInputBoolean = True
                    
                    while validateInputBoolean:
                        # get rate of pay
                        try:
                            rateOfPay = input("Enter the employee's hourly rate of pay: ")
                            # set validateInputLoop to False if input was valid
                            validateInputBoolean = False
                            while int(rateOfPay) < 11:
                                rateOfPay = input("Invalid input - Enter a valid rate of pay: ")
                                # set validateInputLoop to False if input was valid
                                validateInputBoolean = False
                        except ValueError:
                            print("ERROR - invalid input.")
                            validateInputBoolean = True
                        
                    # set validateInputBoolean to True again for data validation
                    validateInputBoolean = True
                    newEmployee = Programmer(employeeID, firstName, lastName, birthYear, birthMonth,
                                           birthDay, str(todaysDate), hoursWorked, rateOfPay)
                    break
            
            # add the new employee to the list of employees
            listEmployees.append(newEmployee)
            print(str(firstName) +" " +str(lastName) +" has been added to the database.")
            # set validateInputBoolean to True again for re-validation of input
            validateInputBoolean = True
            # put employee into the MySQL database
            try:
                # create the INSERT statement as a String using parameter markers,
                # taken from Oracle's official documentation.
                # Oracle. (2015). 5.3 Inserting Data Using Connector/Python. [Webpage].
                #     Retrieved from https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html.
                addEmployee = "INSERT INTO Employees(empID, firstName, lastName, birthdate, startDate, weeklyPay, weeklyTax, posID) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
                # put data into a variable, then execute
                if secondMenuOption == "1":
                    employeeData = (employeeID, firstName, lastName, str(birthYear +"-" +birthMonth +"-" +birthDay),
                                    str(todaysDate), str(newEmployee.weeklyPay), str(newEmployee.weeklyTax), "1")
                else:
                    employeeData = (employeeID, firstName, lastName, str(birthYear +"-" +birthMonth +"-" +birthDay),
                                    str(todaysDate), str(newEmployee.weeklyPay), str(newEmployee.weeklyTax), "2")
                cursor.execute(addEmployee, employeeData)
            except mysql.connector.Error as ex:
                print("Something went wrong: {}".format(ex))   
                         
        # 2 modifies an employee, currently this only allows the modification
        # of an employee's last name
        if menuOption == "2":
            # boolean to determine if employee was changed
            booleanEmployeeChanged = False
            # if list is empty, do nothing
            if (len(listEmployees) == 0):
                print("There are no employees in the database.")
            else:
                print("The following employees are currently in the database:")
                # iterate thru list and display all employees
                for i in listEmployees:
                    print(i)
                # get the employee ID of the employee to be edited
                employeeID = input("Enter the employee's ID of the employee that you want to modify: ")
                # iterate thru list and if the employee ID matches an employee's ID,
                # ask what to modify
                for i in range(len(listEmployees)):
                    if employeeID == listEmployees[i].employeeID:
                        while True:
                            modifyOption = input("Enter:\n\t1 to modify last name\n\t2 to modify pay\n")
                            # 1 modifies last name
                            if modifyOption == "1":
                                lastName = input("Enter a new last name: ")
                                listEmployees[i].lastName = lastName
                                # modify the row in the db
                                try:
                                    modEmployee = "UPDATE Employees SET lastName = %s WHERE empID = %s"
                                    cursor.execute(modEmployee, (lastName, employeeID,))
                                except mysql.connector.Error as ex:
                                    print("Something went wrong: {}".format(ex))
                                print("Employee has been modified.\n")
                                booleanEmployeeChanged = True
                                break
                            # 2 modifies pay
                            if modifyOption == "2":
                                # if the object in the list is an Executive, change the yearly salary
                                if isinstance(listEmployees[i], Executive):
                                    while validateInputBoolean:
                                        try:
                                            yearlySalary = input("Enter the executive's new yearly salary: ")
                                            # set validateInputLoop to False if input was valid
                                            validateInputBoolean = False
                                            while int(yearlySalary) < 1:
                                                yearlySalary = input("Invalid input - Enter a valid yearly salary: ")
                                                # set validateInputLoop to False if input was valid
                                                validateInputBoolean = False
                                        except ValueError:
                                            print("ERROR - invalid input.")
                                            validateInputBoolean = True
                                    # update the pay with the new value
                                    listEmployees[i].yearlyPay = yearlySalary
                                    listEmployees[i].calcWeeklyPay()
                                    listEmployees[i].calcWeeklyTax(listEmployees[i].weeklyPay)    
                                    # modify the row in the db
                                    try:
                                        modEmployee = "UPDATE Employees SET weeklyPay = %s, weeklyTax = %s WHERE empID = %s"
                                        cursor.execute(modEmployee, (listEmployees[i].weeklyPay, listEmployees[i].weeklyTax, employeeID,))
                                    except mysql.connector.Error as ex:
                                        print("Something went wrong: {}".format(ex))
                                    # set validateInputBoolean to True again for data validation
                                    validateInputBoolean = True
                                    # set booleanEmployeeChanged to True to know an employee was modified
                                    booleanEmployeeChanged = True
                                    print("Employee modified.\n")
                                    break
                                # if the object is not an Executive, it is a Programmer object,
                                # so change hourly pay rate and hours worked
                                else:
                                    # get hours worked
                                    while validateInputBoolean:
                                        try:
                                            hoursWorked = input("Enter the new amount of hours employee will be working per week: ")
                                            # set validateInputLoop to False if input was valid
                                            validateInputBoolean = False
                                            while int(hoursWorked) < 5:
                                                hoursWorked = input("Invalid input - Enter a valid amount of hours: ")
                                                # set validateInputLoop to False if input was valid
                                                validateInputBoolean = False
                                        except ValueError:
                                            print("ERROR - invalid input.")
                                            validateInputBoolean = True
                                    # set validateInputBoolean to True again for data validation
                                    validateInputBoolean = True
                                    # get rate of pay
                                    while validateInputBoolean:
                                        try:
                                            rateOfPay = input("Enter the employee's new hourly rate of pay: ")
                                            # set validateInputLoop to False if input was valid
                                            validateInputBoolean = False
                                            while int(rateOfPay) < 11:
                                                rateOfPay = input("Invalid input - Enter a valid rate of pay: ")
                                                # set validateInputLoop to False if input was valid
                                                validateInputBoolean = False
                                        except ValueError:
                                            print("ERROR - invalid input.")
                                            validateInputBoolean = True
                                    # update the pay with the new value
                                    listEmployees[i].hoursWorked = hoursWorked
                                    listEmployees[i].rateOfPay = rateOfPay
                                    listEmployees[i].calcWeeklyPay()
                                    listEmployees[i].calcWeeklyTax(listEmployees[i].weeklyPay)    
                                    # modify the row in the db
                                    try:
                                        modEmployee = "UPDATE Employees SET weeklyPay = %s, weeklyTax = %s WHERE empID = %s"
                                        cursor.execute(modEmployee, (listEmployees[i].weeklyPay, listEmployees[i].weeklyTax, employeeID,))
                                    except mysql.connector.Error as ex:
                                        print("Something went wrong: {}".format(ex))
                                    # set validateInputBoolean to True again for data validation
                                    validateInputBoolean = True
                                    # set booleanEmployeeChanged to True to know an employee was modified
                                    booleanEmployeeChanged = True
                                    print("Employee modified.\n")
                                    break
                if booleanEmployeeChanged == False:
                    print("No employee modified. Make sure you entered a valid employee ID.\n")
            
        # 3 deletes an employee
        if menuOption == "3":
            # boolean used to determine if employee was deleted
            employeeDeleted = False
            # if list is empty, do nothing
            if (len(listEmployees) == 0):
                print("There are no employees in the database.")
            else:
                print("The following employees are currently in the database:")
                # iterate thru list and display employees
                for i in listEmployees:
                    print(i)
                # ask uer to enter employee ID of employee they wish to delete
                employeeID = input("Enter the employee ID of the employee you wish to delete: ")
                # the code below on how to iterate through a list was based on 
                # code provided by the website "Learn Python the Hard Way"
                # Learn Python the Hard Way. (2015). Exercise 32: Loops and Lists. [Webpage].
                #    Retrieved from http://learnpythonthehardway.org/book/ex32.html.
                for i in range(len(listEmployees)):
                    # if the employee ID entered matches an employee ID in the list,
                    # delete that corresponding employee
                    if employeeID == listEmployees[i].employeeID:
                        del listEmployees[i]
                        employeeDeleted = True
                        # delete from MySQL db, based on code from MySQL Tutorial.com
                        # MySQL Tutorial. (2014). Python MySQL Delete Data. [Webpage]. Retrieved
                        #     from http://www.mysqltutorial.org/python-mysql-delete-data/.
                        try:
                            delEmployee = "DELETE FROM Employees WHERE empID = %s"
                            cursor.execute(delEmployee, (employeeID,))
                        except mysql.connector.Error as ex:
                            print("Something went wrong: {}".format(ex))
                        print("Employee deleted.\n")
                if employeeDeleted == False:
                    print("No employee deleted. Make sure you enter a valid employee ID.")
                    
        # 4 displays all employees
        if menuOption == "4":
            print("There are " +str(listEmployees.__len__()) +" employees currently in the database.")
            # if there is at least 1 employee in the database, display all employees
            if (len(listEmployees) > 0):
                print(sHeader)
                for i in listEmployees:
                    print(i)
                print("Displaying employees in MySQL database:")
                cursor.execute("SELECT * FROM EMPLOYEES")
                result = cursor.fetchall()
                print(result)
    
    # save data to a TXT file when quitting, the code below was based on
    # code from Python's official documentation
    # Python Software Foundation. (2015). 7.2. Reading and Writing Files. [Webpage].
    #    Retrieved from https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files.
    print("Saving data to text file before quitting...")
    try:
        # open the file as EmployeeDatabase.txt and write each index within
        # listEmployees List seperated by a new line, then close the file
        file = open('EmployeeDatabase.txt','w')
        file.write(sHeader +"\n")
        for i in listEmployees:
            file.write(str(i) +"\n")
        file.close
    except IOError:
        print("ERROR - Could not save to file.")
    print("Closing database connection...")
    # close db connection
    try:
        cnx.close()
    except mysql.connector.Error as ex:
        print("Error - Could not close database!{}".format(ex))
    print("Goodbye.")
    
    main()