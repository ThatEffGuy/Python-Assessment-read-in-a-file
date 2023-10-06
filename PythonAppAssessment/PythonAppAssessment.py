#Craig Ferguson
#Marks Assessment Program
#Date: 13/01/21
#Purpose: read in a marks csv file

#Library
import csv

#declare lists
surnameList  = []
forenameList = []
marksList    = []

#methods functions
def fillLists():
    with open ("marks.csv", "r") as csvFile:
        csvReader = csv.reader(csvFile)
        for row in csvReader:
            surnameList.append(row[0])
            forenameList.append(row[1])
            marksList.append(int(row[2]))
        #endfor
    #endwith
    return surnameList, forenameList, marksList
#End fill lists

#Find highest mark
def findMaximum(marksList):
    maxMark = None
    maxPostition = None
    if len(marksList)>0:
        maxMarks = marksList[0]
        for index in range(len(marksList)):
            if marksList[index]> maxMarks:
                maxMarks = marksList[index]
                maxPosition = index
            #end if
        #end for
    #end if
    return maxMarks, maxPosition
#end find Max mark

def writeToFile(maxMarks,maxPosition):

    #write to File highest mark
    topName = surnameList[maxPosition] + " " + forenameList[maxPosition]
    print (topName + " had the highest marks of " + str(maxMarks))
    with open ("highestmark.txt","w") as f:
        f.write(topName + " had the highest marks of " + str(maxMarks))
    #end with
#end writeToFile

#main program
surnameList, forenameList, marksList = fillLists()
maxMarks, maxPosition = findMaximum(marksList)
writeToFile(maxMarks, maxPosition)