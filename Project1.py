# File: Project1.py
# Student: Crystal Le
# UT EID: CL44964
# Course Name: CS303E
# 
# Date Created: 10/04/2021
# Date Last Modified: 10/06/2021
# Description of Program: The program prints out the calendar for the month
# in the year of 2022 for the number the user inputted. It also has a parameter check to
# ensure the user is inputting integers between [1 and 12. 

def monthName(n):
    if (n ==1):
        return "January"
    elif (n == 2):
        return "February"
    elif (n == 3):
        return "March"
    elif (n == 4):
        return "April"
    elif (n == 5):
        return "May"
    elif (n == 6):
        return "June"
    elif (n == 7):
        return "July"
    elif (n == 8):
        return "August"
    elif (n == 9):
        return "September"
    elif (n == 10):
        return "October"
    elif (n == 11):
        return "November"
    else:
        return "December"
    
def daysInMonth(n):
    if (n ==1 or n ==3 or n ==5 or n ==7 or n== 8 or n ==10 or n ==12):
        return 31
    elif (n == 4 or n ==6 or n ==9 or n == 11):
        return 30
    else:
        return 28

def makeCalendar(n):
    print()
    centerMonth = (monthName(user) + " 2022").center(20) 
    print(centerMonth)
    print("Su Mo Tu We Th Fr Sa")
    #print first line with startDay
    if (n ==1):
        firstDay= 6
    elif (n == 2):
        firstDay= 2
    elif (n == 3):
        firstDay= 2
    elif (n == 4):
        firstDay= 5
    elif (n == 5):
        firstDay= 0
    elif (n == 6):
        firstDay= 3
    elif (n == 7):
        firstDay= 5
    elif (n == 8):
        firstDay= 1
    elif (n == 9):
        firstDay= 4
    elif (n == 10):
        firstDay= 6
    elif (n == 11):
        firstDay= 2
    else:
        firstDay= 4
    startDay1 = 1
    day1 = 1
    while startDay1 <= firstDay:
        print("   ", end = "")
        startDay1+=1
    while firstDay <= 6:
        print(format(day1, "2d"), "", end = "")
        day1+=1
        firstDay+=1
    print()
    #days in calendar after first line is done
    startDay2 = 0
    for day2 in range(day1, daysInMonth(n) + 1):
            print(format(day2, "2d"), "", end = "")
            startDay2 +=1
            if startDay2 ==7:
                startDay2 = 0
                print()
    
#program where the user is prompted to input and check parameters        
user = int(input("Enter the number of a month [1..12]: "))
while (True):
    if (( user <= 0) or (user > 12)):
        print("Month must be between 1 and 12. Try again!")
        user = int(input("Enter the number of a month [1..12]: "))
    else:
        n = makeCalendar(user)
        print("\n")
        break

    

