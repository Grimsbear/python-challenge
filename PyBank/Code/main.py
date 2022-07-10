# import dependendenices 
import os
import csv

from numpy import average

# route to resources
bankdata = os.path.join("..","Resources","budget_data.csv")

# open csv file
with open(bankdata) as csv_file:

    csvreader = csv.reader(csv_file)
    #print(csvreader)
    csv_header = next(csv_file)

    months = []
    Net = 0

    for row in csvreader:

        Net = Net + int(row[1])

        if row[0] not in months:

            months.append(row[0])

    print(f"Total Months: {len(months)}")
    print(f"Net Total: ${Net}")