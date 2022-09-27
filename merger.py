import csv
ds1 = []
ds2 = []
with open("Data Merging/dataset_1.csv") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        ds1.append(row)
with open("Data Merging/dataset_2.csv") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        ds2.append(row)
header1 = ds1[0]
header2 = ds2[0]
finalHeader = header1+header2
planetData1 = ds1[1:]
planetData2 = ds2[1:]
finalPlanetData = []
print(len(planetData1))
print(len(planetData2))
for index, row in enumerate(planetData1):
    finalPlanetData.append(planetData1[index] + planetData2[index])
with open('finalData.csv',"a+") as x:
    csvwriter = csv.writer(x)
    csvwriter.writerow(finalHeader)
    csvwriter.writerows(finalPlanetData)