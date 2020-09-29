#The total number of months included in the dataset


#The net total amount of "Profit/Losses" over the entire period


#The average of the changes in "Profit/Losses" over the entire period


#The greatest increase in profits (date and amount) over the entire period


#The greatest decrease in losses (date and amount) over the entire period

import os
import csv

budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")

# Open and read csv
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

# calculate total length of months
months = []
total_months = []

for row in csv_reader:
    months.append(rows[0])

    print(f"total months: len {len(months)}")

    


