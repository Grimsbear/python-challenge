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

    months = 0
    Net = 0
    profit = []
    Max = 0
    Min = 100000000
    Date1 = str
    Date2 = str


    for row in csvreader:

        Net = Net + int(row[1])
        months = months + 1
        profit.append(int(row[1]))
        #print(row[1])

        if int(row[1]) >= int(Max):

            Max = row[1]
            Date1 = row[0]

        if int(row[1]) <= int(Min):

            Min = row[1]
            Date2 = row[0]

    average = (profit[-1] - profit[0]) / len(profit)
    average = '{:.2f}'.format(average)

    print("Finacial Analysis")
    print("----------------------")
    print(f"Total Months: {months}")
    print(f"Net Total: ${Net}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase: {Date1}, ${Max}")
    print(f"Greatest Decrease: {Date2}, ${Min}")

    output_path = os.path.join("..","analysis","pybank_result.csv")

    with open(output_path, 'w') as csvfile:

        csvwriter = csv.writer(csvfile, delimiter=',')

        csvwriter.writerow(["Finacial Analysis"])
        csvwriter.writerow(["----------------------"])
        csvwriter.writerow([f"Total Months: {months}"])
        csvwriter.writerow([f"Net Total: ${Net}"])
        csvwriter.writerow([f"Average Change: ${average}"])
        csvwriter.writerow([f"Greatest Increase: {Date1}, ${Max}"])
        csvwriter.writerow([f"Greatest Decrease: {Date2}, ${Min}"])