##########################################################
# CST8333 2015F Final Project - Programmer.py            #
#                                                        #
# Created by Richard Barney                              #
# November 30, 2015                                      #
# This class allows the creation of a Programmer and     #
# inherits from the Employee class. Programmers include  #
# two new parameters - hoursWorked and rateOfPay.        #
#                                                        #
##########################################################
# import statements
from Employee import Employee
# class Programmer inherits from class Employee
class Programmer(Employee):
    
    # constructor
    def __init__(self, employeeID, firstName, lastName, birthYear, birthMonth,
                 birthDay, startingDate, hoursWorked, rateOfPay):
        # call superclass constructor
        Employee.__init__(self, employeeID, firstName, lastName, birthYear, birthMonth,
                 birthDay, startingDate)
        # new variables hoursWorked and rateOfPay
        self.hoursWorked = hoursWorked
        self.rateOfPay = rateOfPay
        # calculate weekly pay and weekly tax based on hoursWorked and rateOfPay
        self.calcWeeklyPay()
        self.calcWeeklyTax(self.weeklyPay)
    
    # calculate the Programmer's weekly pay, which is the hours worked
    # times the rate of pay
    def calcWeeklyPay(self):
        self.weeklyPay = str(float(self.hoursWorked) * float(self.rateOfPay))
        
    # String method, calls Employee's String method and adds the weekly
    # pay and weekly tax
    def __str__(self):
        return super(Programmer, self).__str__() +"\t$" +self.weeklyPay + "\t$" +self.weeklyTax