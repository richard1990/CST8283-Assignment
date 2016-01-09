##########################################################
# CST8333 2015F Final Project - EmployeeDatabaseTest.py  #
#                                                        #
# Created by Richard Barney                              #
# November 30, 2015                                      #
# This class is used for unit testing my program.        #
#                                                        #
# Code was based on official Python documentation.       #
# Python Software Foundation. (2015). 26.4 unittest      #
#    - Unit testing framework. [Webpage]. Retrieved from #
#    https://docs.python.org/3/library/unittest.html.    #
#                                                        #
##########################################################
# import statements
import unittest
import EmployeeDatabase
from Employee import Employee
from Programmer import Programmer
from Executive import Executive
# class EmployeeDatabaseTest inherits from class unittest.TestCase
class EmployeeDatabaseTest(unittest.TestCase):
   
    # test that the list works properly
    def testList(self):
        list1 = EmployeeDatabase.listEmployees
        list2 = []
        # create three Employee objects
        employeeTest = Employee("12345","Richard","Barney","1993","03","25","2015-11-02")
        executiveTest = Executive("12345","Richard","Barney","1993","03","25","2015-11-02","100000")
        programmerTest = Programmer("12345","Richard","Barney","1993","03","25","2015-11-02","40","40")
        # add the objects to listEmployees within the EmployeeDatabase class
        list1.append(employeeTest)
        list1.append(executiveTest)
        list1.append(programmerTest)
        # add the objects to the local list
        list2.append(employeeTest)
        list2.append(executiveTest)
        list2.append(programmerTest)
        # compare the lists
        self.assertListEqual(list1,list2)
        
    # test that creating an Employee object contains the expected String
    def testEmployee(self):
        employeeTest = Employee("12345","Richard","Barney","1990","03","25","2015-11-02")
        employeeString = "12345\t\tRichard Barney\t\t1990-03-25\t2015-11-02"
        self.assertEqual(employeeString, employeeTest.__str__())
    
    # test that creating an Executive object contains the expected String
    def testExecutive(self):
        executiveTest = Executive("12345","Richard","Barney","1990","03","25","2015-11-02","100000")
        executiveString = "12345\t\tRichard Barney\t\t1990-03-25\t2015-11-02\t$1923.08\t$384.62"
        self.assertEqual(executiveString, executiveTest.__str__())
    
    # test that creating a Programmer object contains the expected String
    def testProgrammer(self):
        programmerTest = Programmer("12345","Richard","Barney","1990","03","25","2015-11-02","40","40")
        programmerString = "12345\t\tRichard Barney\t\t1990-03-25\t2015-11-02\t$1600.0\t$320.00"
        self.assertEqual(programmerString, programmerTest.__str__())
    
# this block of code allows running this program from the command line,
# taken from Python's official PyUnit documentation.
# Python Software Foundation. (2015). 26.4.1. Basic example. [Webpage].
#    Retrieved from https://docs.python.org/3/library/unittest.html#basic-example.
if __name__ == '__main__':
    unittest.main()