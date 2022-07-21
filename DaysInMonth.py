# File: DaysInMonth.py
# Student: Crystal Le   
# UT EID: CL44964
# Course Name: CS303E
# 
# Date Created: 09/23/2021
# Date Last Modified: 09/23/2021
# Description of Program: The program is written to allow users to input any year from
# 1000 and any months (1-12) numerically to find out how many days were in that month dependent
# on the year that was inputted. 

year = int(input("Please enter a year: "))
month = int(input("Please enter a month: "))

#elif statements to convert the numerical number of the month the user inputted
#into a string that contains the name of the month. 
if (month ==1):
    monthName = "January"
elif (month == 2):
    monthName = "February"
elif (month == 3):
    monthName = "March"
elif (month == 4):
    monthName = "April"
elif (month == 5):
    monthName = "May"
elif (month == 6):
    monthName = "June"
elif (month == 7):
    monthName = "July"
elif (month == 8):
    monthName = "August"
elif (month == 9):
    monthName = "September"
elif (month == 10):
    monthName = "October"
elif (month == 11):
    monthName = "November"
else:
    monthName = "December"

#elif statements to calculate the number of days in that month inputted. February will have
#28 days and the leap year calendar dates will be calculated later. 
if (month == 4):
    days = 30
elif (month == 6):
    days = 30
elif (month == 9):
    days = 30
elif (month == 11):
    days = 30
elif (month == 2):
    days = 28
else:
    days = 31
    
#elif statements to calculate whether it is a leap year dependent the year. This
#allows the user to see the accurate number of days in February.   
if(year % 400 == 0):
    leapYear = True
elif (year % 100 == 0):
    leapYear = False
elif (year % 4 == 0):
    leapYear = True
else:
    leapYear = False
    
#print statements that will display the result of how many days in the inputted
#month and year. 
if leapYear:
    if(month == 2):
        print(monthName, year, "has 29 days")
    else:
        print(monthName, year, "has", days, "days")
else:
    print(monthName, year, "has", days, "days")
