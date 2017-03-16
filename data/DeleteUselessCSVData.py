import csv
startingYear = 1953
for i in range (0, 55):
    FileName = 'eng-daily-0101'+str(startingYear+i)+'-1231'+str(startingYear+i)+'.csv'
    lineNumber = 1
    with open (FileName) as csvFile , open(str(startingYear+i) +'.csv','w') as newcsvFile:
        for row in csvFile:
            if (lineNumber > 25):
                newcsvFile.write(row)
            lineNumber += 1


