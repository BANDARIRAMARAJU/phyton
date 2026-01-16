"""CSV==>Comma seperated values
As the part of programming,it is very common requirement to write and read data wrt csv
files. Python provides csv module to handle csv files."""
 
import csv
with open("emp.csv","w",newline='') as f:
    w=csv.writer(f) # returns csv writer object
    w.writerow(["ENO","ENAME","ESAL","EADDR"])
    n=int(input("Enter Number of Employees:"))
    for i in range(n):
        eno=input("Enter Employee No:")
        ename=input("Enter Employee Name:")
        esal=input("Enter Employee Salary:")
        eaddr=input("Enter Employee Address:")
        w.writerow([eno,ename,esal,eaddr])
    print("Total Employees data written to csv file successfully")
