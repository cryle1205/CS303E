# File: Project3.py
# Student: Crystal Le
# UT EID: CL44964
# Course Name: CS303E
# 
# Date Created: 11/23/2021
# Date Last Modified: 11/25/2021
# Description of Program: Program takes in a census .csv file to output data based on
# user's inputted commands. Data contains census from 2010 and est 2020 population. 

import os.path
filename = 'populationdata.csv'
infile = open(filename, "r")
data = infile.readline()
data = infile.readline().strip("\n").split(",")


countyList= []
censusDict = {}
totalCensus2010= 0
totalEst2020 = 0
while data:
    if "#" in data[0]:
        exit
    elif len(data[0]) == 0:
        break
    elif len(data)== 4:
        countyName = data[0] + " " + data[1]
        countyList.append(countyName.lower())
        census2010 = int(data[2])
        est2020 = int(data[3])
        censusDict[countyName.lower()]= census2010, est2020
        totalCensus2010 +=census2010
        totalEst2020 += est2020
    else:
        countyName = data[0]
        countyList.append(countyName.lower())
        census2010 = int(data[1])
        est2020 = int(data[2])
        censusDict[countyName.lower()]= census2010, est2020
        totalCensus2010 += census2010
        totalEst2020 += est2020
    data = infile.readline().strip("\n").split(",")   
censusDict["texas"] = totalCensus2010, totalEst2020
#why aren't the totals matching?
#print(totalEst2020) 

def main():
    filename = "populationdata.csv"
    #if file does not exist then the program will end
    if not os.path.isfile(filename):
        print("File does not exist")
        return
    print()
    print("Welcome to the Texas Population Dashboard.")
    print("This provides census data from the 2010 census and")
    print("estimated population data in Texas as of 1/1/2020.")
    print()
    print("Creating dictionary from file:", filename)
    print()
    print("Enter any of the following commands:")
    print("Help - list available commands;")
    print("Quit - exit this dashboard;")
    print("Counties - list all Texas counties;")
    print("Census <countyName>/Texas - population in 2010 census by specified county or statewide;")
    print("Estimated <countyName>/Texas - estimated population in 2020 by specified county or statewide;")
    print("Growth <countyName>/Texas - percent change from 2010 to 2020, by county or statewide.")
    print()


    while(True):
        command = input("Please enter a command: ")
        lowerCommand = command.lower().split()
        if len(lowerCommand) ==1:
            if lowerCommand[0] == "quit":
                print("Thank you for using the Texas Population Database Dashboard.  Goodbye!")
                print()
                break
            elif lowerCommand[0] == "help":
                print("Enter any of the following commands:")
                print("Help - list available commands;")
                print("Quit - exit this dashboard;")
                print("Counties - list all Texas counties;")
                print("Census <countyName>/Texas - population in 2010 census by specified county or statewide;")
                print("Estimated <countyName>/Texas - estimated population in 2020 by specified county or statewide;")
                print("Growth <countyName>/Texas - percent change from 2010 to 2020, by county or statewide.")
                print()
            elif lowerCommand[0] == "counties":
                count=0
                for i in range(len(countyList)):
                    print(countyList[i].title() + ", ", end ="")
                    count+=1
                    if count == 10:
                        print()
                        count=0
                print("\n")
            else:
                print("Command is not recognized.  Try again!")
                print()
        elif len(lowerCommand) == 2:
            if lowerCommand[1] in countyList:
                if lowerCommand[0] == "census":
                    print(lowerCommand[1].capitalize(), "county had" , censusDict[lowerCommand[1]][0] , "citizens in the 2010 Census.")
                    print()
                elif lowerCommand[0] == "estimated":
                    print(lowerCommand[1].capitalize(), "county had estimated population (January, 2020):",  censusDict[lowerCommand[1]][1])
                    print()
                elif lowerCommand[0] == "growth":
                    cgrowth = ((censusDict[lowerCommand[1]][1] - censusDict[lowerCommand[1]][0]) / censusDict[lowerCommand[1]][0]) #* 100.0
                    print(lowerCommand[1].capitalize(), "county had percent population change (2010 to 2020):", format(cgrowth, ".2%"))
                    print()
            elif lowerCommand[1] not in countyList:
                if lowerCommand[1] == "texas":
                    if lowerCommand[0] == "census":
                        print("Texas total population in the 2010 Census:", censusDict["texas"][0])
                        print()
                    elif lowerCommand[0] == "estimated":
                        print("Texas estimated population (January, 2020):", censusDict["texas"][1])
                        print()
                    elif lowerCommand[0] == "growth":
                        tgrowth = ((censusDict["texas"][1] - censusDict["texas"][0]) / censusDict["texas"][0]) #* 100.0
                        print("Texas had percent population change (2010 to 2020):", format(tgrowth, ".2%"))
                        print()
                else:
                    print("County " + lowerCommand[1].capitalize()  + " is not recognized.")
                    print()
        elif len(lowerCommand) == 3:
            fullcname = lowerCommand[1] + " " + lowerCommand[2]
            if fullcname in countyList:
                if lowerCommand[0] == "census":
                    print(fullcname.title(), "county had" , censusDict[fullcname][0] , "citizens in the 2010 Census.")
                    print()
                elif lowerCommand[0] == "estimated":
                    print(fullcname.title(), "county had estimated population (January, 2020):",  censusDict[fullcname][1])
                    print()
                elif lowerCommand[0] == "growth":
                    ngrowth = ((censusDict[fullcname][1] - censusDict[fullcname][0]) / censusDict[fullcname][0]) #* 100.0
                    print(fullcname.title(), "county had percent population change (2010 to 2020):", format(ngrowth, ".2%"))
                    print()
            elif lowerCommand[1] not in countyList:
                print("County " + fullcname.capitalize()  + " is not recognized.")
                print()
            
            
main()
