# File: EasterSunday.py
# Student: Crystal Le
# UT EID: CL44964
# Course Name: CS303E
# 
# Date Created: 09/10
# Date Last Modified: 09/10
# Description of Program: This program prompts user to insert a year and it will
# compute the date of Easter Sunday for a specified year.

y = int( input("Enter year: "))
a = y % 19
b = y // 100
c = y % 100
d = b // 4
e = b % 4
g = (8 * b + 13) // 25
h = (19 * a + b - d - g + 15) % 30
j = c // 4
k = c % 4
m = (a + 11 * h) // 319
r = (2 * e + 2 * j - k - h + m + 32) % 7
n = (h - m + r + 90) // 25
p = (h - m + r + n + 19) % 32
print("In", y, "Easter Sunday is on month", n, "and day", p) 



