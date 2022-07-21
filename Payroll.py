# File: Payroll.py
# Student: Crystal Le
# UT EID: CL44964
# Course Name: CS303E
# 
# Date Created: 09/16/2021
# Date Last Modified: 09/17/2021
# Description of Program: Created a program that is able to calculate an employee's  weekly payroll
# by listing their name, hours worked, pay rate, tax deductions, and net/gross pay. 

emp_name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked in a week: "))
rate = float(input("Enter hourly pay rate: "))
fed_tax = float(input("Enter federal tax withholding rate: "))
state_tax = float(input("Enter state tax withholding rate: "))

# I inserted some calculations for deductions and gross pay
# ahead of time to make my print statements shorter
gross_pay = hours * rate
fed_ded = gross_pay * fed_tax
state_ded = gross_pay * state_tax
total_ded = fed_ded + state_ded

print()
print("Employee Name:", emp_name)
print("Hours Worked:", format(hours,"2.1f"))
print("Pay Rate: $", format(rate, "2.2f"), sep = "")
print("Gross Pay: $", format(gross_pay, "2.2f"), sep = "")
print("Deductions:")
print("  Federal Withholding (", format(fed_tax, "2.1%"), "): $", format(fed_ded, "2.2f"), sep = "")
print("  State Withholding (", format(state_tax, "2.1%"), "): $", format(state_ded, "2.2f"), sep = "")
print("  Total Deduction: $", format((total_ded), "2.2f"), sep = "")
print("Net Pay: $", format((gross_pay - total_ded), "2.2f"), sep = "")



