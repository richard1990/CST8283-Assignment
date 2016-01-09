##########################################################
# CST8333 2015F Final Project - Employee.py              #
#                                                        #
# Created by Richard Barney                              #
# November 30, 2015                                      #
# This class allows the creation of an Employee. It      #
# requires fields such as first and last name, date of   #
# birth, and starting date.                              #
#                                                        #
##########################################################
class Employee:
    
    # constructor
    def __init__(self, employeeID, firstName, lastName, birthYear, birthMonth,
                 birthDay, startingDate):
        self.employeeID = employeeID
        self.firstName = firstName
        self.lastName = lastName
        self.birthYear = birthYear
        self.birthMonth = birthMonth
        self.birthDay = birthDay
        self.startingDate = startingDate

    # calcuate weekly pay, inherited classes will customize this method
    def calcWeeklyPay(self):
        return ""
    
    # calculate the weekly tax by passing the weekly pay as a parameter.
    # if the weeky pay is greater than $2000, then tax is 0.3%, if weekly
    # pay is less than $1000, then there is no tax, and if weekly pay is
    # between $1000 and $2000, tax is 0.2%. weeklyTax will only contain
    # two decimal places
    def calcWeeklyTax(self, weeklyPay):
        if float(weeklyPay) > 2000:
            self.weeklyTax = '%.2f' % (float(weeklyPay) * 0.3)
        elif float(weeklyPay) < 1000:
            self.weeklyTax = "0"
        else:
            self.weeklyTax = '%.2f' % (float(weeklyPay) * 0.2)

    # String method, returns all fields
    def __str__(self):
        return self.employeeID + "\t\t" +self.firstName +" " +self.lastName +"\t\t" +self.birthYear +"-" +self.birthMonth +"-" +self.birthDay +"\t" +self.startingDate