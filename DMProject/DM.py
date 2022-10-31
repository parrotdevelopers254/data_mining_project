#opening my csv file(dataset)
myFile = open('table111.csv', 'r')
#splitbylines
listOfLines = myFile.read().splitlines()
#print(listOfLines[0])
#print(listOfLines[1])
#print(listOfLines[len(listOfLines)-1])
'''
Date,Industry_aggregation_NZSIOC,Industry_code_NZSIOC,Industry_name_NZSIOC,Units,Variable_code,Variable_name,Variable_category,Value,Industry_code_ANZSIC06
01/01/2008,Level 1,99999,All industries,Dollars (millions),H01,Total income,Financial performance,"757,504","ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"
31/12/2008,Level 4,AA211,Forestry and Logging,Percentage,H41,Liabilities structure,Financial ratios,64,ANZSIC06 group A030
'''
###SINGLE_LINE###
aLine = listOfLines[1]
lineItems = aLine.split(',')
print(lineItems)
date = lineItems[0]
data = lineItems[5]
print("date=", date)
print("data=", data)
dateSplit = date.split('/')
year = dateSplit[0]
month = dateSplit[1]
print("year=", year)
print("month=", month)
###SINGLE_LINE###
oldMonth = month
sum = 0
count = 0
listOfAverages = []
for i in range(1, len(listOfLines), 1):
    aLine = listOfLines[i]
    #print(aLine)
    lineItems = aLine.split(',')
    #print(lineItems)
    date = lineItems[0]
    data = lineItems[5]
    #print("date=", date)
    #print("data=", data)
    dateSplit = date.split('/')
    year = dateSplit[2]
    month = dateSplit[1]
    if month == oldMonth:
        sum = sum + int(data)
        count +=1
        avg = sum / count
    #print('sum=', sum, 'count=', count, 'avg=', avg)
    if month != oldMonth or i == 366:
        #print('year', year, 'month=', oldMonth, 'avg= %.2f' %avg)
        subList = [year, oldMonth, avg]
        listOfAverages.append(subList)
        sum = float(data)
        count = 1
        oldMonth = month

for i in range(0, len(listOfAverages), 1):
    print(listOfAverages[i])
