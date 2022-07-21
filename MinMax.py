# File: MinMax.py
# Student: Crystal Le
# UT EID: CL44964
# Course Name: CS303E
# 
# Date Created: 09/29/2021
# Date Last Modified: 09/30/2021
# Description of Program: This program returns the maximum integer and
# minimum integer the user inputs until he/she enters 'stop'. 

#function minMax is a function that decides whether or not
#to replace the max and minimum stored integer the user enters.
def minMax(usernum, max1, min1):
    usernum = int(user)
    if usernum > max1:
        max1 = usernum
    if usernum < min1:
        min1 = usernum
    return min1, max1

#This asks the user to input an integer
user = input("Enter an integer or 'stop' to end: ")

if (user == 'stop'):
        print("You didn't enter any numbers")
        exit
else:
    max1 = int(user)
    min1 = int(user)
    while (True):
        user = input("Enter an integer or 'stop' to end: ")
    
        if (user == 'stop'):
            print("The maximum is ", max1)
            print("The minimum is ", min1)
            break
        else:
            usernum = int(user)
            min1, max1 = minMax(usernum, max1, min1)
            











            


        

    

