##########################################################
# CST8333 2015F Final Project - Executive.py             #
#                                                        #
# Created by Richard Barney                              #
# November 30, 2015                                      #
# This class allows the creation of a Executive and      #
# inherits from the Employee class. Executives include   #
# one new parameter - yearlyPay.                         #
#                                                        #
##########################################################
# import statements
from Employee import Employee
# class Executive inherits from class Employee
class Executive(Employee):
    
    # constructor
    def __init__(self, employeeID, firstName, lastName, birthYear, birthMonth,
                 birthDay, startingDate, yearlyPay):
        # call superclass constructor
        Employee.__init__(self, employeeID, firstName, lastName, birthYear, birthMonth,
                 birthDay, startingDate)
        # new variable yearlyPay
        self.yearlyPay = yearlyPay
        # calculate weekly pay and weekly tax based on yearlyPay
        self.calcWeeklyPay()
        self.calcWeeklyTax(self.weeklyPay)
        
    # calculate the Executive's weekly pay, which is the yearly pay
    # divided by 52 and only include two decimal places
    def calcWeeklyPay(self):
        self.weeklyPay = '%.2f' % (int(self.yearlyPay) / 52.0)
    
    # String method, calls Employee's String method and adds the weekly
    # pay and weekly tax
    def __str__(self):
        return super(Executive, self).__str__() +"\t$" +self.weeklyPay + "\t$" +self.weeklyTax