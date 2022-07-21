# File: Benford.py
# Student: Crystal Le
# UT EID: CL44964
# Course Name: CS303E
# 
# Date Created: 11/11/2021
# Date Last Modified: 11/11/2021
# Description of Program: Runs through the 2009 Census and gives out the number of unique populations
# and their leading digit count frequency dependent on the total number of cities through the exisiting text
# file and its new outfile. 

import os.path

def benfordsLaw():
    filename = input("Enter the name of a file of census data: ")
    #if file does not exist then the program will end
    if not os.path.isfile(filename):
        print("File does not exist")
        return

    #if file is accurate and exists, the following will run
    infile = open(filename, "r")
    outfile = open("benford.txt", "w")
    #skipping first line of titles
    data = infile.readline().split()
    #first line with data
    data = infile.readline().split()
    cityCount = 0
    #empty set for Unique Population and empty dictionary for Leading Digits
    uniquePop = set()
    leadingDigitCounts = {}
    while data:
        if len(data) == 3:
            uniquePop.add(data[2])
            if data[2][0] in leadingDigitCounts:
                leadingDigitCounts[data[2][0]] +=1
            else:
                leadingDigitCounts[data[2][0]] = 1
        elif len(data) == 4:
            uniquePop.add(data[3])
            if data[3][0] in leadingDigitCounts:
                leadingDigitCounts[data[3][0]] +=1
            else:
                leadingDigitCounts[data[3][0]] = 1
        elif len(data) == 5:
            uniquePop.add(data[4])
            if data[4][0] in leadingDigitCounts:
                leadingDigitCounts[data[4][0]] +=1
            else:
                leadingDigitCounts[data[4][0]] = 1
        elif len(data) == 6:
            uniquePop.add(data[5])
            if data[5][0] in leadingDigitCounts:
                leadingDigitCounts[data[5][0]] +=1
            else:
                leadingDigitCounts[data[5][0]] = 1
        elif len(data) == 7:
            uniquePop.add(data[6])
            if data[6][0] in leadingDigitCounts:
                leadingDigitCounts[data[6][0]] +=1
            else:
                leadingDigitCounts[data[6][0]] = 1
        elif len(data) == 8:
            uniquePop.add(data[7])
            if data[7][0] in leadingDigitCounts:
                leadingDigitCounts[data[7][0]] +=1
            else:
                leadingDigitCounts[data[7][0]] = 1
        cityCount+=1
        data = infile.readline().split()
        
    #writing into the outfile: benford.txt
    outfile.write("Total number of cities: " + str(cityCount))
    outfile.write("\nUnique population counts: " + str(len(uniquePop)))
    outfile.write("\nFirst digit frequency distributions:")
    outfile.write("\nDigit\tCount\tPercentage")
    #First Digit Frequency Table 
    totalCount = 0
    for key in leadingDigitCounts:
        totalCount +=leadingDigitCounts[key]
    for num in range(10):
        for key in leadingDigitCounts:
            if (str(num) == key):
                percentage = (leadingDigitCounts[key]/totalCount)*100
                outfile.write("\n")
                outfile.write( str(num) + "\t" + str(leadingDigitCounts[key]) + "\t" + format(percentage,".1f"))

    #output message when outfile is written successfully
    print("Output written to benford.txt")
    #closing out both files
    infile.close()
    outfile.close()
    
benfordsLaw()




